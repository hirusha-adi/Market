import os

_cwd = os.getcwd()

settings: str = os.path.join(
    _cwd,
    "database",
    "settings.json"
)

upoad_folder: str = os.path.join(
    _cwd, 
    "uploads"
)