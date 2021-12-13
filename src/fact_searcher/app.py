import asyncio
from typing import List, Optional

import httpx
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .fact_searcher import main
from .settings import Settings, get_settings
from .types import Fact, Facts, FactWithoutId, Position

app = FastAPI(
    openapi_tags=[
        {
            "name": "service:facts_searcher",
        }
    ]
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/facts_searcher/city", response_model=Facts, tags=["service:facts_searcher"])
async def search_by_city(places: List[str]):
    cities = await asyncio.gather(*map(main, places))
    return [fact for city in cities for fact in city]


@app.post(
    "/facts_searcher/add_facts", response_model=Facts, tags=["service:facts_searcher"]
)
async def add_facts(facts: Facts, settings: Settings = Depends(get_settings)):
    async with httpx.AsyncClient() as client:
        for fact in facts:
            await client.post(f"{settings.facts_url}facts", data=fact.json())
