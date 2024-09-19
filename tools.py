import requests
from pydantic import BaseModel, Field
import datetime

from langchain.agents import tool

from models import OpenMeteoInput


@tool(args_schema=OpenMeteoInput)
def get_current_temperature(latitude: float, longitude: float) -> dict:
    """Fetch current temperature for given coordinates."""

    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    # Parameters for the request
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "forecast_days": 1,
    }

    # Make the request
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        results = response.json()
    else:
        raise Exception(f"API Request failed with status code: {response.status_code}")

    current_utc_time = datetime.datetime.utcnow()
    time_list = [
        datetime.datetime.fromisoformat(time_str.replace("Z", "+00:00"))
        for time_str in results["hourly"]["time"]
    ]
    temperature_list = results["hourly"]["temperature_2m"]

    closest_time_index = min(
        range(len(time_list)), key=lambda i: abs(time_list[i] - current_utc_time)
    )
    current_temperature = temperature_list[closest_time_index]

    return f"The current temperature is {current_temperature}°C"


# # For testing it individually
# if __name__ == "__main__":
#     # The Tool properties:
#     print(f"The function name is: {get_current_temperature.name!r}")
#     print(f"The function description is: {get_current_temperature.description!r}")
#     print(f"The function args are: {get_current_temperature.args!r}")
#
#     temperature = get_current_temperature.run(tool_input={"latitude":4.0, "longitude":-70.0})
#     print(temperature)
