# Startup instructions
## Requirements before starting
* The utility works only on the Linux operating system.
* Script works with python 3 installed
* Requires internet connection to work
## Preparation before launch
* Change to the working directory of the script
* Make sure the folder's permissions allow you to create files in it
* Make sure that the make_json.py and cli_utility.sh files are in the utility folder
* Add launch rights to cli_utility.sh utility
* Make sure you have pip installed
```shell
chmod +x cli_utility.sh
```
## Running the utility
Make sure you are in the script folder.

To run, enter:
```shell
./cli_utitlity.sh
```
## View result
After the script is completed, the result.JSON file will be created and written, which contains
structure that contains:
* All packages that are in p10 but not in sisyphus
* All packages that are in sisyphus but not in p10
* All packages whose version-release is greater in sisyphus than in p10

## Result.json structure
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