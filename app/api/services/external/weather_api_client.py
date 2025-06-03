import requests

class WeatherAPIClient:
    def __init__(self, api_key: str, base_url: str = "https://api.weatherapi.com/v1"):
        self.api_key = api_key
        self.base_url = base_url

    def get_forecast(self, location_query: str, days: int = 1, aqi: bool = False, alerts: bool = False):
        """
        Get weather forecast for a specific location.
        :param location_query: Location query (Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name)
        :param days: Number of days to forecast (default is 1, max is 14)
        :param aqi: Include air quality index (default is False)
        :param alerts: Include weather alerts (default is False)
        :return: JSON response with weather forecast
        """
        if days < 1 or days > 14:
            raise ValueError("Days must be between 1 and 14.")
        aqi = 'yes' if aqi else 'no'
        alerts = 'yes' if alerts else 'no'
        url = f"{self.base_url}/forecast.json?q={location_query}&days={days}&aqi={aqi}&alerts={alerts}&key={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
