#!/usr/bin/env bash

venv=".tmp/depenv"
generator=".tmp/generator.py"
runtime="org.kde.Sdk//6.11"

mkdir -p $venv
python3 -m venv $venv --upgrade-deps
source "$venv/bin/activate"
pip install requirements-parser
curl -o $generator "https://raw.githubusercontent.com/flatpak/flatpak-builder-tools/refs/heads/master/pip/flatpak-pip-generator.py"
flatpak install -y $runtime
python3 $generator \
    --pyproject-file "pyproject.toml" \
    --output "flatpak/python-modules" \
    --runtime $runtime \
    --prefer-wheels "deno,cryptography"
deactivate
rm -r $venv $generator
