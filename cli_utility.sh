#!/bin/bash

echo 'Packages from branch p10 will be written to file p10'
touch p10
echo 'Packages from the sisyphus branch will be written to the sisyphus file'
touch sisyphus
echo $'result.JSON - a file that reflects all the packages that are in p10 but not in sisyphus.\nAll packages that are in sisyphus but not in p10.\nAll packages whose version-release is greater in sisyphus than in p10'
touch result.JSON
echo 'pip update'
python3.10 -m pip install --upgrade pip
echo 'Connecting a library for version comparison'
pip3 install packaging
echo 'Writing packages from p10 branch to p10 file'
curl https://rdb.altlinux.org/api/export/branch_binary_packages/p10 > p10
echo 'Writing packages from sisyphus branch to sisyphus file'
curl https://rdb.altlinux.org/api/export/branch_binary_packages/sisyphus > sisyphus
echo 'Writing to result.JSON'
python3 make_json.py
echo 'The script has completed its work'
