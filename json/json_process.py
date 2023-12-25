from pathlib import Path
import json

class JSONProcess:
    def __init__(self):
        pass

    def write_json(self, file_path):
        numbers = [1, 2, 3, 4, 5]
        path = Path('./' + file_path)
        contents = json.dumps(numbers)
        path.write_text(contents)
        print('write done')

    def read_json(self, file_path):
        path = Path('./' + file_path)
        contents = path.read_text()
        numbers = json.loads(contents)
        print(numbers)


myJson = JSONProcess()
myJson.read_json('./numbers.json')