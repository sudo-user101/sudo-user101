Creating a full Python project for the "EV Charger Locator" app involves several components, including data collection, backend development, frontend development, and integration. Below is a basic outline with some code snippets to get you started.

### Step 1: Data Collection

#### 1.1. Data Sources
- Gather data from existing APIs or websites that provide EV charging station locations globally or specifically in South Africa.
- You can use public datasets if available or web scrape if allowed.

#### 1.2. Example API (Fictitious)
Here is a simple example class to simulate fetching data from an API:

```python
import requests

class EVChargerAPI:
    def __init__(self, api_key):
        self.base_url = "https://api.ev-charger-locator.com"
        self.api_key = api_key

    def get_chargers_nearby(self, latitude, longitude, radius=10):
        endpoint = f"{self.base_url}/chargers"
        params = {
            "lat": latitude,
            "lon": longitude,
            "radius": radius,
            "key": self.api_key
        }
        response = requests.get(endpoint, params=params)
        return response.json()

# Note: Replace the URL and key with real ones when they are available.
```

### Step 2: Backend Development

#### 2.1. Set Up Flask Application

Create a simple Flask app to handle API requests and serve data to the frontend.

```python
from flask import Flask, jsonify, request
from ev_charger_api import EVChargerAPI  # Assume this is the class created above

app = Flask(__name__)
api = EVChargerAPI(api_key='your_real_api_key_here')

@app.route('/api/chargers', methods=['GET'])
def get_chargers():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    radius = request.args.get('radius', default=10, type=int)
    
    chargers = api.get_chargers_nearby(latitude, longitude, radius)
    return jsonify(chargers)

if __name__ == '__main__':
    app.run(debug=True)
```

### Step 3: Frontend Development

#### 3.1. Simple HTML and JavaScript Interface

Create a basic HTML page to interact with the backend.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>EV Charger Locator</title>
</head>
<body>
    <h1>Find Nearby EV Charging Stations</h1>
    <form id="locationForm">
        <input type="text" id="latitude" placeholder="Latitude" required>
        <input type="text" id="longitude" placeholder="Longitude" required>
        <input type="number" id="radius" placeholder="Search Radius (km)" required>
        <button type="submit">Find Chargers</button>
    </form>
    <div id="results"></div>

    <script>
        document.getElementById('locationForm').onsubmit = async (e) => {
            e.preventDefault();
            const latitude = document.getElementById('latitude').value;
            const longitude = document.getElementById('longitude').value;
            const radius = document.getElementById('radius').value;

            const response = await fetch(`/api/chargers?latitude=${latitude}&longitude=${longitude}&radius=${radius}`);
            const chargers = await response.json();
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = chargers.map(charger => `<p>${charger.name} - ${charger.address}</p>`).join('');
        };
    </script>
</body>
</html>
```

### Step 4: Additional Features

#### 4.1. Map Integration
- Integrate a map service like Google Maps or Leaflet to visually display charger locations.

#### 4.2. User Authentication
- Allow users to create accounts, save favorite charging stations, and plan trips.

#### 4.3. Eco Travel Planner
- Develop a module to calculate and suggest the most eco-friendly routes, considering charging station locations.

### Step 5: Deployment

- Use a platform like Heroku, AWS, or Azure for deploying the app.
- Ensure that the server is capable of handling requests and is secured properly.

This is a broad outline to get you started on the "EV Charger Locator" project. Depending on your actual data sources and requirements, implementations may vary significantly. Good luck with your project!