import requests
city = input("enter:")
url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID=8070427dafe4191516ffbb1aee5aea2c".format(
    city)
res = requests.get(url)
data = res.json()
print(res)
print(data)
