import requests

r = requests.get('http://localhost:8000/hi/ahmed')

print(r.json())