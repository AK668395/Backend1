from flask import Flask, jsonify, request
import requests

# 1. Define 'app' first
app = Flask(__name__)

API_KEY = '332d53ca85c6b6871ff229510817791e'


@app.route('/weather', methods=['GET'])
def get_weather():
  city = request.args.get('city', 'London')

  # TEMPORARY MOCK DATA FOR TESTING
  data = {
      'name': city,
      'main': {'temp': 20.5, 'feels_like': 19.8, 'humidity': 65},
      'weather': [{'description': 'scattered clouds'}],
      'wind': {'speed': 3.6},
  }

  formatted = {
      'city': data['name'],
      'temperature': data['main']['temp'],
      'feels_like': data['main']['feels_like'],
      'humidity': data['main']['humidity'],
      'description': data['weather'][0]['description'],
      'wind_speed': data['wind']['speed'],
  }
  return jsonify(formatted)


# 2. Run the application
if __name__ == '__main__':
  app.run(debug=True)