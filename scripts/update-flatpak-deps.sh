#!/usr/bin/env bash

venv=".tmp/depenv"
generator=".tmp/generator.py"
mkdir -p $venv
python3 -m venv $venv --upgrade-deps
source "$venv/bin/activate"
pip install requirements-parser
curl -o $generator "https://raw.githubusercontent.com/flatpak/flatpak-builder-tools/refs/heads/master/pip/flatpak-pip-generator.py"
python3 $generator \
    --pyproject-file "pyproject.toml" \
    --output "flatpak/python-modules" \
    --runtime "org.kde.Platform//6.10"
deactivate
rm -r $venv
rm $generator
