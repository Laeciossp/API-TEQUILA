from fastapi import APIRouter, Query
from typing import List
from services.tequila_service import search_flights
from models.flight import FlightResponse

router = APIRouter()

@router.get("/flights", response_model=List[FlightResponse])
async def get_flights(
    fly_from: str = Query(..., description="City code to fly from"),
    fly_to: str = Query(..., description="City code to fly to"),
    date_from: str = Query(..., description="Start date DD/MM/YYYY"),
    date_to: str = Query(..., description="End date DD/MM/YYYY"),
    limit: int = 5
):
    return await search_flights(fly_from, fly_to, date_from, date_to, limit)