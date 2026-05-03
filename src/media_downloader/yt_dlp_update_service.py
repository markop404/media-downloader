import sys
import os
import importlib
import threading
import ast
from textwrap import dedent
from zipfile import ZipFile
from hashlib import sha256

import requests
import pgpy
from packaging import version


class YtDlpUpdateService:
    ASSET_NAME = "yt-dlp"
    MODULE_NAME = "yt_dlp"
    SUMS_ASSET_NAME = "SHA2-256SUMS"
    SIGNATURE_ASSET_NAME = "SHA2-256SUMS.sig"
    API_URL = "https://api.github.com/repos/yt-dlp/yt-dlp/releases/latest"
    API_HEADERS = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    TIMEOUT = (3.05, 6)
    BUNDLED_VERSION = version.parse(importlib.metadata.version(MODULE_NAME))
    LOCK = threading.Lock()
    ZIP_VERSION_FILEPATH = f"{MODULE_NAME}/version.py"
    ZIP_VERSION_ATTRIBUTE = "__version__"
    PUBLIC_KEY = pgpy.PGPKey.from_blob(
        dedent(
            """
            -----BEGIN PGP PUBLIC KEY BLOCK-----
            mQINBGP78C4BEAD0rF9zjGPAt0thlt5C1ebzccAVX7Nb1v+eqQjk+WEZdTETVCg3
            WAM5ngArlHdm/fZqzUgO+pAYrB60GKeg7ffUDf+S0XFKEZdeRLYeAaqqKhSibVal
            DjvOBOztu3W607HLETQAqA7wTPuIt2WqmpL60NIcyr27LxqmgdN3mNvZ2iLO+bP0
            nKR/C+PgE9H4ytywDa12zMx6PmZCnVOOOu6XZEFmdUxxdQ9fFDqd9LcBKY2LDOcS
            Yo1saY0YWiZWHtzVoZu1kOzjnS5Fjq/yBHJLImDH7pNxHm7s/PnaurpmQFtDFruk
            t+2lhDnpKUmGr/I/3IHqH/X+9nPoS4uiqQ5HpblB8BK+4WfpaiEg75LnvuOPfZIP
            KYyXa/0A7QojMwgOrD88ozT+VCkKkkJ+ijXZ7gHNjmcBaUdKK7fDIEOYI63Lyc6Q
            WkGQTigFffSUXWHDCO9aXNhP3ejqFWgGMtCUsrbkcJkWuWY7q5ARy/05HbSM3K4D
            U9eqtnxmiV1WQ8nXuI9JgJQRvh5PTkny5LtxqzcmqvWO9TjHBbrs14BPEO9fcXxK
            L/CFBbzXDSvvAgArdqqlMoncQ/yicTlfL6qzJ8EKFiqW14QMTdAn6SuuZTodXCTi
            InwoT7WjjuFPKKdvfH1GP4bnqdzTnzLxCSDIEtfyfPsIX+9GI7Jkk/zZjQARAQAB
            tDdTaW1vbiBTYXdpY2tpICh5dC1kbHAgc2lnbmluZyBrZXkpIDxjb250YWN0QGdy
            dWI0ay54eXo+iQJOBBMBCgA4FiEErAy75oSNaoc0ZK9OV89lkztadYEFAmP78C4C
            GwMFCwkIBwIGFQoJCAsCBBYCAwECHgECF4AACgkQV89lkztadYEVqQ//cW7TxhXg
            7Xbh2EZQzXml0egn6j8QaV9KzGragMiShrlvTO2zXfLXqyizrFP4AspgjSn/4NrI
            8mluom+Yi+qr7DXT4BjQqIM9y3AjwZPdywe912Lxcw52NNoPZCm24I9T7ySc8lmR
            FQvZC0w4H/VTNj/2lgJ1dwMflpwvNRiWa5YzcFGlCUeDIPskLx9++AJE+xwU3LYm
            jQQsPBqpHHiTBEJzMLl+rfd9Fg4N+QNzpFkTDW3EPerLuvJniSBBwZthqxeAtw4M
            UiAXh6JvCc2hJkKCoygRfM281MeolvmsGNyQm+axlB0vyldiPP6BnaRgZlx+l6MU
            cPqgHblb7RW5j9lfr6OYL7SceBIHNv0CFrt1OnkGo/tVMwcs8LH3Ae4a7UJlIceL
            V54aRxSsZU7w4iX+PB79BWkEsQzwKrUuJVOeL4UDwWajp75OFaUqbS/slDDVXvK5
            OIeuth3mA/adjdvgjPxhRQjA3l69rRWIJDrqBSHldmRsnX6cvXTDy8wSXZgy51lP
            m4IVLHnCy9m4SaGGoAsfTZS0cC9FgjUIyTyrq9M67wOMpUxnuB0aRZgJE1DsI23E
            qdvcSNVlO+39xM/KPWUEh6b83wMn88QeW+DCVGWACQq5N3YdPnAJa50617fGbY6I
            gXIoRHXkDqe23PZ/jURYCv0sjVtjPoVC+bg=
            =bJkn
            -----END PGP PUBLIC KEY BLOCK-----
            """
        )
    )[0]

    def __init__(self, path):
        self.bin_path = os.path.join(path, self.ASSET_NAME)
        self.download_path = self.bin_path + ".update"
        self.version = str(self.BUNDLED_VERSION)

    def start_update(self):
        threading.Thread(target=self.update).start()
    
    def update(self):
        with self.LOCK:
            api_response = requests.get(
                self.API_URL,
                headers=self.API_HEADERS,
                timeout=self.TIMEOUT
            )
            api_response.raise_for_status()
            release_json = api_response.json()
            latest_version = version.parse(release_json.get("tag_name"))
            
            downloaded_version = None
            if os.path.isfile(self.bin_path):
                with ZipFile(self.bin_path, "r") as z:
                    if self.ZIP_VERSION_FILEPATH in z.namelist():
                        tree = ast.parse(
                            z.read(self.ZIP_VERSION_FILEPATH).decode()
                        )
                        for node in ast.walk(tree):
                            if isinstance(node, ast.Assign):
                                for target in node.targets:
                                    if isinstance(target, ast.Name) and target.id == self.ZIP_VERSION_ATTRIBUTE:
                                        try:
                                            downloaded_version = version.parse(ast.literal_eval(node.value))
                                        except:
                                            pass
                                        break
                if downloaded_version != latest_version:
                    os.remove(self.bin_path)
                    downloaded_version = None

            if latest_version != self.BUNDLED_VERSION:
                if not downloaded_version:
                    for asset in release_json.get("assets"):
                        match asset.get("name"):
                            case self.ASSET_NAME:
                                bin_response = requests.get(asset.get("browser_download_url"), timeout=self.TIMEOUT)
                                bin_response.raise_for_status()
                            case self.SUMS_ASSET_NAME:
                                sums_response = requests.get(asset.get("browser_download_url"), timeout=self.TIMEOUT)
                                sums_response.raise_for_status()
                            case self.SIGNATURE_ASSET_NAME:
                                signature_response = requests.get(asset.get("browser_download_url"), timeout=self.TIMEOUT)
                                signature_response.raise_for_status()
                    os.makedirs(
                        os.path.dirname(self.download_path),
                        exist_ok=True
                    )
                    with open(self.download_path, "wb") as f:
                        f.write(bin_response.content)

                    try:
                        sums_file_valid = self.PUBLIC_KEY.verify(
                            sums_response.content,
                            pgpy.PGPSignature.from_blob(signature_response.content)
                        )
                    except (TypeError, ValueError, pgpy.errors.PGPError):
                        sums_file_valid = False
                    if not sums_file_valid:
                        os.remove(self.download_path)
                        return
                    for line in sums_response.content.splitlines():
                        expected_hash, name = line.decode().split(None, 1)
                        if name == self.ASSET_NAME:
                            calculated_hash = sha256(bin_response.content).hexdigest()
                            break
                    else:
                        calculated_hash = None
                    if calculated_hash != expected_hash:
                        os.remove(self.download_path)
                        return

                    os.replace(self.download_path, self.bin_path)

                if self.bin_path not in sys.path:
                    sys.path.insert(0, self.bin_path)
                if self.MODULE_NAME in sys.modules:
                    modules = [m for m in sys.modules.copy() if m.startswith(self.MODULE_NAME)]
                    for module in modules:
                        sys.modules.pop(module)
                importlib.invalidate_caches()
                self.version = str(latest_version)