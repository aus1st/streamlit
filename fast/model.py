from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    description: str
    location: str

thing = Creature(name='yeti', description='Abdominable Snowman', location='Himalayas')
print('Name is ', thing.name)