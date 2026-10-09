import os

def api_origin():
     return os.getenv("API_ORIGIN", "http://localhost:8000")

print (api_origin())

#print is only for development purposes. to test our code
