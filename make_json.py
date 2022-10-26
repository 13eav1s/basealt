import json
import copy
from typing import List


class Package:
    name: str = None
    epoch = set()
    version = set()
    release = set()
    arch = set()
    disttag = set()
    buildtime = set()
    source = set()

    def __str__(self):
        return self.name

    def __init__(self, name: str, epoch: str, version: str, release: str, arch: str, disttag: str, buildtime: str, source: str):
        self.name = name
        self.epoch.add(epoch)
        self.version.add(version)
        self.release.add(release)
        self.arch.add(release)
        self.disttag.add(release)
        self.buildtime.add(release)
        self.source.add(source)
        copy.copy(self)


def add_to_arr_packs(added_packs_f, array: List[Package], name, epoch, version, release, arch, disttag, buildtime, source):
    if name in added_packs_f:
        i = added_packs_f.index(name)
        array[i].epoch.add(epoch)
        array[i].version.add(version)
        array[i].release.add(release)
        array[i].arch.add(arch)
        array[i].disttag.add(disttag)
        array[i].buildtime.add(buildtime)
        array[i].buildtime.add(source)
    else:
        added_packs_f.append(name)
        pack = Package(name, epoch, version, release, arch, disttag, buildtime, source)
        array.append(copy.copy(pack))


#  Преобразование пакетов из ветки в объекты класса и запись в массив
def add_packs_from_file_to_obj_array(file, array, added_packs):
    with open(file, 'r') as fj:
        str_json = fj.readline()
        data = json.loads(str_json)
        size = 0
        for i in data["packages"]:
            add_to_arr_packs(added_packs, array, i['name'], i['epoch'], i['version'], i['release'], i['arch'],
                             i['disttag'], i['buildtime'], i['source'])
            size += 1
        print(size)


data_sisyphus = []
data_p10 = []
added_packs_sisyphus = []
added_packs_p10 = []

add_packs_from_file_to_obj_array('sisyphus', data_sisyphus, added_packs_sisyphus)
add_packs_from_file_to_obj_array('p10', data_p10, added_packs_p10)
pass

#  Преобразование пакетов из p10 в объекты класса и запись во множество data_p10
# with open('p10', 'r') as fj:
#     str_json = fj.readline()
#     data = json.loads(str_json)
#     size = 0
#     for i in data["packages"]:
#         pack = Package(i['name'], i['epoch'], i['version'], i['release'], i['arch'], i['disttag'], i['buildtime'], i['source'])
#         size += 1
#         data_p10.append(pack)
#     print(size)

#  Вывод пакетов из p10, которых нет в sisyphus
