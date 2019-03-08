#!/bin/sh
python -m features.tests.length
python -m features.tests.subdomains

if ! [ -x "$(command -v pycodestyle)" ]; then
  echo 'Error: pycodestyle is not installed. Cannot check code sanity' >&2
else
  pycodestyle --show-source --show-pep8 --exclude features/__init__.py .
fi
