from fast.model import Creature

_cureatures: list[Creature] = [
    Creature(name='yeti', description='Abdominable Snowman', location='Himalayas'),
    Creature(name='sasquatch', description='Bigfoot', location='North America'),
]

def get_creatures() -> list[Creature]:
    return _cureatures