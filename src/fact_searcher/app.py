from typing import Optional, List
from fastapi import FastAPI, HTTPException, Depends
from .types import Fact, FactWithoutId, Facts, Position
from .settings import Settings, get_settings
from .fact_searcher import main
import asyncio
import httpx

app = FastAPI(
	openapi_tags=[
		{
			"name": "service:facts_searcher",
		}
	]
)


@app.post("/facts_searcher/city", response_model=Facts, tags=["service:facts_searcher"])
async def search_by_city(places: List[str]):
	cities = await asyncio.gather(
		*map(main, places)
	)
	return [ fact for city in cities for fact in city ]


@app.post("/facts_searcher/add_facts", response_model=Facts, tags=["service:facts_searcher"])
async def add_facts(facts: Facts):
	async with httpx.AsyncClient() as client:
		for fact in facts:
			await client.post(f"{settings.places_url}facts", data=fact.json())