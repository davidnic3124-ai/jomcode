import httpx

request = httpx.Request("GET", "https://localhost:8000/workshops", params={"q": "Python", "offset": 0, "limit": 10})
print(request.method)
print(request.url.path)
print(request.url.params["limit"]) 

