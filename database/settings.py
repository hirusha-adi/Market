import utils.filenames as filenames
import json
from typing import Union

with open(filenames.settings, "r", encoding="utf-8") as _file:
    data = json.load(_file)


class Web:
    web = data["web"]
    host: str = web["host"]
    port: Union[int, str] = web["port"]
    debug: bool = web["debug"]


class Dekstop:
    desktop = data["desktop"]
    top = desktop["top"]
    header = desktop["header"]
    bottom = desktop["bottom"]


class Mongo:
    mongo = data["mongodb"]
    ip: str = mongo["ip"]
    username: str = mongo["username"]
    password: str = mongo["password"]


class Settings:
    settings = data['settings']
    name = settings['name']
    default_image = settings['default_image']
