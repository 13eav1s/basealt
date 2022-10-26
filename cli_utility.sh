#!/bin/bash

echo 'Пакеты с ветки p10 будут записаны в файл p10'
touch p10
echo 'Пакеты с ветки sisyphus будут записаны в файл sisyphus'
touch sisyphus
echo $'result.JSON - файл, в котором отражены все пакеты, которые есть в p10 но нет в sisyphus.\nВсе пакеты, которые есть в sisyphus но их нет в p10.\nВсе пакеты, version-release  которых больше в sisyphus чем в p10'
touch result.JSON
echo 'Запись пакетов с ветки p10 в файл p10'
curl https://rdb.altlinux.org/api/export/branch_binary_packages/p10 > p10
echo 'Запись пакетов с ветки sisyphus в файл sisyphus'
curl https://rdb.altlinux.org/api/export/branch_binary_packages/sisyphus > sisyphus
echo 'Запись в result.JSON'
python3 make_json.py
echo 'Скрипт завершил свою работу'
