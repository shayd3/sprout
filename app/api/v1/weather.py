import os
from fastapi import APIRouter, Depends, HTTPException
from api.services.external.weather_api_client import WeatherAPIClient

router = APIRouter()

def get_weather_client() -> WeatherAPIClient:
    """
    Initialize and return a WeatherAPIClient instance.
    """
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="Weather API key not configured")
    return WeatherAPIClient(api_key=api_key)


@router.get("/current")
async def get_current_weather(
    location: str,
    weather_client: WeatherAPIClient = Depends(get_weather_client)
):
    """
    Get the current weather for a specific location.

    Args:
        location (str): The location for which to get the current weather.
        weather_client (WeatherAPIClient): The weather API client dependency.
    """
    try:
        forecast = weather_client.get_forecast(location_query=location)
        return forecast
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to fetch weather data: {str(e)}")
