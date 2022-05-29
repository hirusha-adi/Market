import utils.filenames as filenames
import json

with open(filenames.settings, "r", encoding="utf-8") as _file:
    data = json.load(_file)


class Web:
    host: str = data["web"]["host"]
    port: int = data["web"]["port"]
    debug: bool = data["web"]["debug"]


class Dekstop:
    pass
