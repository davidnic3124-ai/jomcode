import httpx

response = httpx.Response(201, json={"id":"w1","capacity":20,"title":"Python Basics","start":"2024-2026"})
print(response.status_code)
print(response.json()["id"])
print(response.json()["capacity"])
print(response.json()["title"])
print(response.json()["start"])