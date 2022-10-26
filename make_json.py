import json


class Package:
    name: str = None
    epoch: str = None
    version: str = None
    release: str = None
    arch: str = None
    disttag: str = None
    buildtime: str = None
    source: str = None

    def __init__(self, name: str, epoch: str, version: str, release: str, arch: str, disttag: str, buildtime: str, source: str):
        self.name = name
        self.epoch = epoch
        self.version = version
        self.release = release
        self.arch = arch
        self.disttag = disttag
        self.buildtime = buildtime
        self.source = source


data_sisyphus = []
data_p10 = []

with open('sisyphus_packages', 'r') as fj:
    str_json = fj.readline()
    data = json.loads(str_json)
    size = 0
    for i in data["packages"]:
        pack = Package(i['name'], i['epoch'], i['version'], i['release'], i['arch'], i['disttag'], i['buildtime'], i['source'])
        size += 1
        data_sisyphus.append(pack)
    print(size)

with open('p10', 'r') as fj:
    str_json = fj.readline()
    data = json.loads(str_json)
    size = 0
    for i in data["packages"]:
        pack = Package(i['name'], i['epoch'], i['version'], i['release'], i['arch'], i['disttag'], i['buildtime'], i['source'])
        size += 1
        data_p10.append(pack)
    print(size)