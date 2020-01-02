from requests import get,post

url = ''
json = {}

a = post(url = url, json = json).json
print(a)
