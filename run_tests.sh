#!/bin/sh
python -m features.tests.length
python -m features.tests.subdomains
python -m features.tests.top1m
python -m features.tests.tld
python -m features.tests.daysSinceRegistration

if ! [ -x "$(command -v pycodestyle)" ]; then
  echo 'Error: pycodestyle is not installed. Cannot check code sanity' >&2
else
  pycodestyle --show-source --show-pep8 --exclude features/__init__.py,features/tests/ .
fi
