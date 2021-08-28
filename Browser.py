import requests
url = 'https://brickset.com/sets/year-2004'
r = requests.get(url)
print(r.text)

print("status code:")
print("\t*", r.status_code)

h = requests.head(url)
print("Header:")
print("**********")
for x in h.headers:
    print("\t ", x, ".", h.headers[x])
print("**********")

headers = {
    'User-Agent' : 'Mobile'
}
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)