from typing import Optional

from fastapi import FastAPI, HTTPException, Depends
# from reusable_mongodb_connection.fastapi import get_collection

# from .types import Place, PlaceWithoutID, Places
# from .settings import Settings, get_settings
import .facts_searcher
import asyncio

app = FastAPI(
	openapi_tags=[
		{
			"name": "service:facts_searcher",
		}
	]
)


@app.post("/facts_searcher/city", tags=["service:facts_searcher"])
async def search_by_city(places: list[str]):
	cities = await asyncio.gather(
		*map(facts_searcher.main, places)
	)
	return [ fact for city in cities for fact in city ]
