import httpx
r = httpx.get('http://localhost:8000/hi')
print(r.status_code)
print(r.headers)
print(r.text)
print(r.json())