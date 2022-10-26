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
        self.epoch = {epoch, }
        self.version = {version, }
        self.release = {release, }
        self.arch = {release, }
        self.disttag = {release, }
        self.buildtime = {release, }
        self.source = {source, }


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
        array.append(copy.deepcopy(pack))
        print('adding pack', pack.name, '...', sep='')


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


#  Получение пакетов ветки которых нет в другой
def get_special_packs(branch1_names: List[str], branch2_names: List[str], branch1: List[Package]):
    count_packs = 0
    for pack_name_index in range(len(branch1_names)):
        if not (branch1_names[pack_name_index] in branch2_names):
            print(branch1[pack_name_index])
            count_packs += 1
    print(count_packs)


data_sisyphus = []
data_p10 = []
added_packs_sisyphus = []
added_packs_p10 = []


add_packs_from_file_to_obj_array('test1', data_sisyphus, added_packs_sisyphus)
add_packs_from_file_to_obj_array('test2', data_p10, added_packs_p10)

#  Вывод пакетов которых нет в sisyphus, но есть в p10
get_special_packs(added_packs_p10, added_packs_sisyphus, data_p10)

#  Вывод пакетов которых нет в p10, но есть в sisyphus
get_special_packs(added_packs_sisyphus, added_packs_p10, data_sisyphus)

identical_packages = set(added_packs_p10) & set(added_packs_sisyphus)
pass