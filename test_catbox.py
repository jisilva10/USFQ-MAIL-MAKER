import requests

url = "https://catbox.moe/user/api.php"
files = {'fileToUpload': ('test.txt', 'hello world', 'text/plain')}
data = {'reqtype': 'fileupload'}
response = requests.post(url, files=files, data=data)
print("Response:", response.text)
print("Headers:", response.headers)
