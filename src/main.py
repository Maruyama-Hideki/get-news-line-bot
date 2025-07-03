import requests


url = 'https://www3.nhk.or.jp/news/'
response = requests.get(url)
response.encoding = response.apparent_encoding
print(response.text)