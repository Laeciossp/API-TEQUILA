import httpx
from typing import List
from models.flight import FlightResponse
from core.config import settings

TEQUILA_API_URL = "https://api.tequila.kiwi.com/v2/search"

async def search_flights(fly_from: str, fly_to: str, date_from: str, date_to: str, limit: int) -> List[FlightResponse]:
    headers = {"apikey": settings.TEQUILA_API_KEY}
    params = {
        "fly_from": fly_from,
        "fly_to": fly_to,
        "date_from": date_from,
        "date_to": date_to,
        "limit": limit,
        "curr": "USD"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(TEQUILA_API_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

    flights = [FlightResponse(
        price=flight["price"],
        departure=flight["route"][0]["local_departure"],
        arrival=flight["route"][-1]["local_arrival"],
        city_from=flight["cityFrom"],
        city_to=flight["cityTo"],
        airline=flight["airlines"][0]
    ) for flight in data.get("data", [])]

    return flights