import os

_cwd = os.getcwd()

settings: str = os.path.join(
    _cwd,
    "database",
    "settings.json"
)
