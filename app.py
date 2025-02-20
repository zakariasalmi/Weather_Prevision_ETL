from flask import Flask, jsonify, render_template
import json 

app= Flask(__name__)


with open("data/weather_data.json","r", encoding="utf-8") as file:
    weather_data= json.load(file)
        

@app.route("/")
def home():
    return render_template("index.html", data= weather_data)


@app.route("/api/weather")
def get_weather():
    return jsonify(weather_data)


if __name__ == "__main__":
    app.run(debug=True)