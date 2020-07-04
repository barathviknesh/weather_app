# import requests
# city = input("enter:")
# url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID=8070427dafe4191516ffbb1aee5aea2c".format(
#     city)
# res = requests.get(url)
# data = res.json()
# print(res)
# print(data)
from flask import Flask, render_template, request
import requests

app = Flask(
    __name__,
    template_folder="templates"
)


@app.route("/")
def hello_world():
    return "hello world!"


def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + \
        city + "&units=metric&APPID=8070427dafe4191516ffbb1aee5aea2c"
    json_response = requests.get(url).json()
    weather_description = json_response["weather"][0]["description"]
    temp = json_response["main"]["temp"]
    return {"description": weather_description, "temp": temp}


@app.route("/<location>")
def weather(location):
    weather_details = get_weather(location)
    print(weather_details)
    return render_template("weather.html", weather_details=weather_details, location=location)


# @app.route("/", methods=['POST', 'GET'])
# def weather():
#     try:
#         if request.method == "POST":

#     weather_details = get_weather(location)
#     print(weather_details)
#     return render_template("weather.html", weather_details=weather_details, location=location)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
