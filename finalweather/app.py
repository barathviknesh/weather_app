from flask import Flask, render_template, request
import requests


app = Flask(
    __name__,
    template_folder="client/templates",

)


@app.route("/", methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']

        url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=8070427dafe4191516ffbb1aee5aea2c"
        wx = requests.get(url.format(city)).json()
        weather = {
            'city': city,
            'temperature': wx['main']['temp'],
            'description': wx['weather'][0]['description'],
            'icon': wx['weather'][0]['icon'],
        }
        print(weather)
        return render_template('weather.html', weather=weather)
    else:
        return render_template('weather.html')


app.run(port=5000)
