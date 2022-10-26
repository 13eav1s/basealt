# Инструкция по запуску
## Требования перед запуском
* Утилита только на опреационной системе Linux
* Скрипт работает при установленном python 3
* Для работы требуется соединение с сетью интернет
## Подготовка перед запуском
* Перейдите в рабочую папку скрипта
* Убедитесь что в права папки разрешают создавать в ней файлы
* Убедитесь что в папке утилиты находятся файлы make_json.py и cli_utility.sh
* Добавьте права на запуск утилите cli_utility.sh
```shell
chmod +x cli_utility.sh
```
## Запуск утилиты
Убедитесь что вы находитесь в папке скрипта.

Для запуска введите:
```shell
./cli_utitlity.sh
```
## Просмотр результата
После завершения работы скрипта будут создан и записан файл result.JSON, в котором находится
структура, которая содержит:
* Все пакеты, которые есть в p10 но нет в sisyphus
* Все пакеты, которые есть в sisyphus но их нет в p10
* Все пакеты, version-release  которых больше в sisyphus чем в p10

## Структура result.JSON
```json
{
    "only_in_p10": [
        {
            "name": "Pocket name",
            "version": "Pocket version",
            "release": "Release code",
            "arch": "array of archs"
        }, 
      {Other packs from only in p10}
    ],
        "only_in_sisyphus": [
          {
            "name": "Pocket name",
            "version": "Pocket version",
            "release": "Release code",
            "arch": "array of archs"
        }, {Other packs from only in sisyphus}
          ],
    "version_release_upper_in_sisyphus": [
        {
            "name": "Pocket name",
            "version": "Pocket version",
            "release": "Release code",
            "arch": "array of archs"
        }, {Other packs from version release upper in sisyphus}
    ]
}
```
