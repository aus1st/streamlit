
responses: dict[str, str |int] = {"ok": '200', "not found": 404}
print(responses)

things1: str  = 'yeti'
things1 = 123

def get_thing() -> str:
    return 'thing'

get_thing()

tuple_thing = ('yeti', 'Abdominable Snowman', 'Himalayas')
print('Name is ', tuple_thing[0])

list_thing = ['yeti', 'Abdominable Snowman', 'Himalayas']
print('Name is ', list_thing[0])

Name=0
Location=1
Descripton = 2
print('name is ', tuple_thing[Name])
print('location is ', tuple_thing[Location])
print('description is ', list_thing[Descripton])