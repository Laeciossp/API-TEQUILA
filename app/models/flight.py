from pydantic import BaseModel

class FlightResponse(BaseModel):
    price: float
    departure: str
    arrival: str
    city_from: str
    city_to: str
    airline: str