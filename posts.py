import requests

r = requests.get("http://localhost/posts/")
print(r.json())