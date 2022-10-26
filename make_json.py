import json
import copy
from typing import List


class Package:
    name: str = None
    epoch = set()
    version: str = None
    release: str = None
    arch = set()
    disttag = set()
    buildtime = set()
    source = set()

    def __str__(self):
        return self.name

    def __init__(self, name: str, epoch: str, version: str, release: str, arch: str, disttag: str, buildtime: str, source: str):
        self.name = name
        self.epoch = {epoch, }
        self.version = version
        self.release = release
        self.arch = {arch, }
        self.disttag = {disttag, }
        self.buildtime = {buildtime, }
        self.source = {source, }


def add_to_arr_packs(added_packs_f, array: List[Package], name, epoch, version, release, arch, disttag, buildtime, source):
    if name in added_packs_f:
        i = added_packs_f.index(name)
        array[i].epoch.add(epoch)
        array[i].version = version
        array[i].release = release
        array[i].arch.add(arch)
        array[i].disttag.add(disttag)
        array[i].buildtime.add(buildtime)
        array[i].buildtime.add(source)
    else:
        added_packs_f.append(name)
        pack = Package(name, epoch, version, release, arch, disttag, buildtime, source)
        array.append(copy.deepcopy(pack))


#  Преобразование пакетов из ветки в объекты класса и запись в массив
def add_packs_from_file_to_obj_array(file, array, added_packs):
    with open(file, 'r') as fj:
        str_json = fj.readline()
        data = json.loads(str_json)
        size = 0
        last_procent = -1
        all_size = int(data['length'])
        for i in data['packages']:
            add_to_arr_packs(added_packs, array, i['name'], i['epoch'], i['version'], i['release'], i['arch'],
                             i['disttag'], i['buildtime'], i['source'])
            size += 1
            procent = int(size / all_size * 100)
            if procent != last_procent:
                print('\r', procent, '%', sep='', end='')
            last_procent = procent
    print()


#  Получение пакетов ветки которых нет в другой
def get_special_packs(branch_name: str, branch1_names: List[str], branch2_names: List[str], branch1: List[Package], result_dict: dict):
    count_packs = 0
    for pack_name_index in range(len(branch1_names)):
        if not (branch1_names[pack_name_index] in branch2_names):
            dict_line = {
                'name': branch1[pack_name_index].name,
                'version': branch1[pack_name_index].version,
                'release': branch1[pack_name_index].release,
                'arch': list(branch1[pack_name_index].arch)
            }
            result_dict[branch_name].append(dict_line)
            count_packs += 1
    print('number of packages', count_packs)


def write_json(data, filename):
    # data = json.dumps(data)
    # data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


data_sisyphus = []
data_p10 = []
added_packs_sisyphus = []
added_packs_p10 = []

#  Словарь, который будет переведен в JSON
result_json = {
    'only_in_p10': [],
    'only_in_sisyphus': [],
    'version_release_upper_in_sisyphus': []
}

print('______________________________Adding p10 packages____________________________')
add_packs_from_file_to_obj_array('p10', data_p10, added_packs_p10)
print('__________________________Adding sisyphus packages___________________________')
add_packs_from_file_to_obj_array('sisyphus', data_sisyphus, added_packs_sisyphus)

#  Вывод пакетов которых нет в sisyphus, но есть в p10
print('____________Write packages that are not in sisyphus, but are in p10___________')
print('Wait, please...')
get_special_packs('only_in_p10', added_packs_p10, added_packs_sisyphus, data_p10, result_json)

#  Вывод пакетов которых нет в p10, но есть в sisyphus
print('___________writing packages that are not in p10, but are in sisyphus__________')
print('Wait, please...')
get_special_packs('only_in_sisyphus', added_packs_sisyphus, added_packs_p10, data_sisyphus, result_json)

identical_packages = set(added_packs_p10) & set(added_packs_sisyphus)

#  Добавление идентичных пакетов для сравнения версий
ident_packs_p10 = []
ident_packs_sisyphus = []
print('____Adding version-release packages which are more in sisyphus than in p10____')
print('Wait, please...')
col_packs = 0
for pack in identical_packages:
    p10_new = data_p10[added_packs_p10.index(pack)]
    sisyphus_new = data_sisyphus[added_packs_sisyphus.index(pack)]
    if sisyphus_new.version > p10_new.version:
        col_packs += 1
        sisyphus_new_dict = {
            'name': sisyphus_new.name,
            'version': sisyphus_new.version,
            'release': sisyphus_new.release,
            'arch': list(sisyphus_new.arch)
        }
        result_json['version_release_upper_in_sisyphus'].append(sisyphus_new_dict)
print('number of packages:', col_packs)
#  Запись полученного словаря в json
write_json(result_json, 'result.JSON')
