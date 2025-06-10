# 🌱 Sprout
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-in%20development-yellow.svg)
![Plants](https://img.shields.io/badge/plants-🌱-green.svg)

A comprehensive indoor and outdoor plant watering tracker and predictor that helps you keep your plants healthy and thriving.


## 🚀 Getting Started

1. Install depedencies with uv:
```bash
uv sync
```

2. Setup Environmnet Variables
```bash
cp .env.example .env
```

3. Sign up for a free account at WeatherAPI.com
Add your API key to .env:
```
WEATHER_API_KEY=<https://weatherapi.com api key>
```

To run project locally, run:
```bash
uv run fastapi dev --app app
```

## API Documentation
Once the server is running, visit:

Interactive API Docs: http://localhost:8000/docs
ReDoc Documentation: http://localhost:8000/redoc
