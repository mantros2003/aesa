from enum import Enum, auto

class Feature(Enum):
    _NOTE = "note"
    _MISC = ""

def get_feature(cmd: str) -> Feature:
    if cmd.strip().startswith(Feature._NOTE.value):
        return Feature._NOTE

    return Feature._MISC
