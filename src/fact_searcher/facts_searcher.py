from requests_html import HTMLSession
from bs4 import BeautifulSoup
from typing import NamedTuple
from pydantic import BaseModel
import asyncio
import googlesearch

class CustomError(Exception):
	def __init__(self, message):
		self.message = message
	pass


class Position(NamedTuple):
	lng: float
	lat: float


class FactWithoutId(BaseModel):
	name: str
	description: str
	pos: Position

class Fact(FactWithoutId):
	fact_id: str


def fact_parser(soup: BeautifulSoup) -> str:
	result = str(soup)
	parenthesis_start = result.find(" (")
	if result.find("</b>") + 4 == parenthesis_start or result.find("</i>") + 4 == parenthesis_start:
		parenthesis_end = result.find(") ")
		result = result.replace(result[parenthesis_start:parenthesis_end + 1], "")
	sup_tags = soup.find_all('sup')
	for sup in sup_tags:
		result = result.replace(str(sup), "")
	link_tags = soup.find_all('a')
	for a in link_tags:
		result = result.replace(str(a), a.text)
	return result

async def extract_coords(link: str, session: HTMLSession) -> list:
	coordinates = session.get(link)
	elements = coordinates.html.xpath("//table//th[text()='Latitude']/following-sibling::td")
	return [elements[1].text, elements[0].text]

async def search_facts(name: str, session: HTMLSession) -> list:
	link = f"https://en.wikipedia.org/wiki/{name}"
	wiki = session.get(link)
	if wiki.status_code == 404:
		search_result = list(googlesearch.search(name + "wikipedia", stop=1))
		if search_result[0].find("wikipedia.org") != -1:
			link = search_result[0]
		else:
			return ""
		wiki = session.get(link)
	try:
		soup = BeautifulSoup(wiki.html.xpath("//div[@class='mw-parser-output']/p[not(@class='mw-empty-elt')]", first=True).html, 'html.parser')
	except:
		print("Wrong wiki page")
		return ""
	return fact_parser(soup)

async def main(city: str) -> list:
	try:
		search = city
		if len(city) < 5:
			search = str('+' * (5 - len(city))) + city
		URL = f"https://www.tripexpress.org/search/?keywords={search}"
		session = HTMLSession()

		city_search = session.get(URL)

		sights = session.get("".join(city_search.html.xpath(f"//a[text()='{city}']")[0].absolute_links))

		##TODO add pages

		sights_cards = sights.html.find(".card")
		places = []
		for card in sights_cards:
			element = card.xpath(f"//div[@class='card-body']//a")[0]
			place_name = element.text
			link2coordinates = "".join(element.absolute_links)
			fact_fields = await asyncio.gather(
				extract_coords(link2coordinates, session),
				search_facts(place_name, session)
			)
			place_pos = Position(*fact_fields[0])
			custom_id = "_".join(place_name.lower().split(" "))
			place = Fact(name=place_name, description=fact_fields[1], pos=place_pos, fact_id=custom_id)
			print(place)
			places.append(place)
	except Exception as err:
		print(err.message)
	return places

asyncio.run(main("Moscow"))