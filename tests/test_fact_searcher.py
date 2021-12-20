from fastapi.testclient import TestClient

from fact_searcher.app import app
from fact_searcher.settings import Settings


client = TestClient(app)


results = [
  {
    "name": "1st of May Library",
    "description": "",
    "pos": [
      37.58384,
      55.71064
    ],
    "fact_id": "1st_of_may_library"
  },
  {
    "name": "613 Bricks",
    "description": "",
    "pos": [
      37.50109,
      55.74195
    ],
    "fact_id": "613_bricks"
  },
  {
    "name": "77 Na Leninskom Interactive Children's Theater",
    "description": "",
    "pos": [
      37.54224,
      55.68642
    ],
    "fact_id": "77_na_leninskom_interactive_children's_theater"
  },
  {
    "name": "A-Ya Musical Drama Theatre For Children",
    "description": "",
    "pos": [
      37.612488,
      55.76556
    ],
    "fact_id": "a-ya_musical_drama_theatre_for_children"
  },
  {
    "name": "A. Goldenveizer's Apartment Museum",
    "description": "",
    "pos": [
      37.58818,
      55.7783
    ],
    "fact_id": "a._goldenveizer's_apartment_museum"
  },
  {
    "name": "A. Golubkina's Museum Workshop",
    "description": "",
    "pos": [
      37.58972,
      55.74319
    ],
    "fact_id": "a._golubkina's_museum_workshop"
  },
  {
    "name": "A. Gorkiy Museum",
    "description": "",
    "pos": [
      37.59834,
      55.75332
    ],
    "fact_id": "a._gorkiy_museum"
  },
  {
    "name": "A. Makarenko Pedagogical Museum",
    "description": "",
    "pos": [
      37.426,
      55.731724
    ],
    "fact_id": "a._makarenko_pedagogical_museum"
  },
  {
    "name": "A. N. Scriabin House Museum",
    "description": "",
    "pos": [
      37.59023,
      55.750732
    ],
    "fact_id": "a._n._scriabin_house_museum"
  },
  {
    "name": "A. Ostrovskiy Moscow Regional State Drama Theatre",
    "description": "",
    "pos": [
      37.76706,
      55.70464
    ],
    "fact_id": "a._ostrovskiy_moscow_regional_state_drama_theatre"
  },
  {
    "name": "A. Ostrovskiy's House Museum",
    "description": "",
    "pos": [
      37.62562,
      55.74061
    ],
    "fact_id": "a._ostrovskiy's_house_museum"
  },
  {
    "name": "A. Vasnetsov's Apartment Museum",
    "description": "",
    "pos": [
      37.647408,
      55.76322
    ],
    "fact_id": "a._vasnetsov's_apartment_museum"
  },
  {
    "name": "A.P. Bogdanov House",
    "description": "",
    "pos": [
      37.63277,
      55.7731
    ],
    "fact_id": "a.p._bogdanov_house"
  },
  {
    "name": "A.R.T.O. Moscow Theatre",
    "description": "",
    "pos": [
      37.63166,
      55.76603
    ],
    "fact_id": "a.r.t.o._moscow_theatre"
  },
  {
    "name": "A3 Gallery",
    "description": "",
    "pos": [
      37.59545,
      55.74394
    ],
    "fact_id": "a3_gallery"
  },
  {
    "name": "Academician I.V. Kurchatov's Memorial House Museum",
    "description": "",
    "pos": [
      37.47528,
      55.801483
    ],
    "fact_id": "academician_i.v._kurchatov's_memorial_house_museum"
  },
  {
    "name": "Academician P. L. Kapitsa's Memorial Museum Office",
    "description": "",
    "pos": [
      37.57604,
      55.70882
    ],
    "fact_id": "academician_p._l._kapitsa's_memorial_museum_office"
  },
  {
    "name": "Adventure Park Master Panin",
    "description": "",
    "pos": [
      37.53716,
      55.73002
    ],
    "fact_id": "adventure_park_master_panin"
  },
  {
    "name": "Afimoll City",
    "description": "",
    "pos": [
      37.539314,
      55.749767
    ],
    "fact_id": "afimoll_city"
  },
  {
    "name": "Agency Art.Ru",
    "description": "",
    "pos": [
      37.63728,
      55.73953
    ],
    "fact_id": "agency_art.ru"
  },
  {
    "name": "Akademicheskiy Park",
    "description": "",
    "pos": [
      37.564438,
      55.691486
    ],
    "fact_id": "akademicheskiy_park"
  },
  {
    "name": "Aksakov House",
    "description": "",
    "pos": [
      37.590443,
      55.74732
    ],
    "fact_id": "aksakov_house"
  },
  {
    "name": "Albatross Art Gallery",
    "description": "",
    "pos": [
      37.71885,
      55.77961
    ],
    "fact_id": "albatross_art_gallery"
  },
  {
    "name": "Albatross Puppet Theater",
    "description": "",
    "pos": [
      37.7872,
      55.79468
    ],
    "fact_id": "albatross_puppet_theater"
  },
  {
    "name": "Aleksandro-Mariinskiy Institute",
    "description": "",
    "pos": [
      37.60123,
      55.74466
    ],
    "fact_id": "aleksandro-mariinskiy_institute"
  },
  {
    "name": "Aleksandrovskiy Sad",
    "description": "",
    "pos": [
      37.61373,
      55.75589
    ],
    "fact_id": "aleksandrovskiy_sad"
  },
  {
    "name": "Alexander Art Gallery and Salon",
    "description": "",
    "pos": [
      37.59949,
      55.75327
    ],
    "fact_id": "alexander_art_gallery_and_salon"
  },
  {
    "name": "Alexander Blok Statue",
    "description": "",
    "pos": [
      37.595867,
      55.75874
    ],
    "fact_id": "alexander_blok_statue"
  },
  {
    "name": "Alexander Goldenweiser's Memorial Flat Museum",
    "description": "",
    "pos": [
      37.613914,
      55.75783
    ],
    "fact_id": "alexander_goldenweiser's_memorial_flat_museum"
  },
  {
    "name": "Alexander Gomelsky Universal Sports Hall CSKA",
    "description": "",
    "pos": [
      37.542854,
      55.78931
    ],
    "fact_id": "alexander_gomelsky_universal_sports_hall_cska"
  },
  {
    "name": "Alexander Nevskiy Cathedral",
    "description": "",
    "pos": [
      37.60013,
      55.7144
    ],
    "fact_id": "alexander_nevskiy_cathedral"
  },
  {
    "name": "Alexander Nevskiy Cathedral in Kozhukhovo",
    "description": "",
    "pos": [
      37.66147,
      55.703175
    ],
    "fact_id": "alexander_nevskiy_cathedral_in_kozhukhovo"
  },
  {
    "name": "Alexander Nevskiy Chapel",
    "description": "",
    "pos": [
      37.63116,
      55.75667
    ],
    "fact_id": "alexander_nevskiy_chapel"
  },
  {
    "name": "Alexey Garin's Art Bureau",
    "description": "",
    "pos": [
      37.60611,
      55.73486
    ],
    "fact_id": "alexey_garin's_art_bureau"
  },
  {
    "name": "Alexey Tolstoy Museum",
    "description": "",
    "pos": [
      37.59627,
      55.75857
    ],
    "fact_id": "alexey_tolstoy_museum"
  },
  {
    "name": "All Russian exhibition center",
    "description": "",
    "pos": [
      37.68224,
      55.7883
    ],
    "fact_id": "all_russian_exhibition_center"
  },
  {
    "name": "All Saints Church",
    "description": "",
    "pos": [
      37.66227,
      55.780903
    ],
    "fact_id": "all_saints_church"
  },
  {
    "name": "All Saints Church at Sokol",
    "description": "",
    "pos": [
      37.58268,
      55.77866
    ],
    "fact_id": "all_saints_church_at_sokol"
  },
  {
    "name": "All-Russia Art Scientific-Restoration Center",
    "description": "",
    "pos": [
      37.67241,
      55.76385
    ],
    "fact_id": "all-russia_art_scientific-restoration_center"
  },
  {
    "name": "All-Russian Museum of Decorative, Applied and Folk Art",
    "description": "",
    "pos": [
      37.61054,
      55.774574
    ],
    "fact_id": "all-russian_museum_of_decorative,_applied_and_folk_art"
  },
  {
    "name": "Alla and Alexander Gallery",
    "description": "",
    "pos": [
      37.57165,
      55.74681
    ],
    "fact_id": "alla_and_alexander_gallery"
  },
  {
    "name": "Alla Bulyanskaya Gallery",
    "description": "",
    "pos": [
      37.611504,
      55.73062
    ],
    "fact_id": "alla_bulyanskaya_gallery"
  },
  {
    "name": "Alla Dukhovoy Theater Todes",
    "description": "",
    "pos": [
      37.634907,
      55.808144
    ],
    "fact_id": "alla_dukhovoy_theater_todes"
  },
  {
    "name": "Alley of Love",
    "description": "",
    "pos": [
      37.667576,
      55.697124
    ],
    "fact_id": "alley_of_love"
  },
  {
    "name": "Alley of the Leaders of Russia",
    "description": "",
    "pos": [
      37.63642,
      55.75735
    ],
    "fact_id": "alley_of_the_leaders_of_russia"
  },
  {
    "name": "Alleya Alisy Seleznevoy",
    "description": "",
    "pos": [
      37.49168,
      55.85958
    ],
    "fact_id": "alleya_alisy_seleznevoy"
  },
  {
    "name": "Allies and Lend-Lease Museum",
    "description": "",
    "pos": [
      37.62325,
      55.73011
    ],
    "fact_id": "allies_and_lend-lease_museum"
  },
  {
    "name": "Alpenrose Gallery",
    "description": "",
    "pos": [
      37.613888,
      55.757812
    ],
    "fact_id": "alpenrose_gallery"
  },
  {
    "name": "Alpert Gallery",
    "description": "",
    "pos": [
      37.688614,
      55.761814
    ],
    "fact_id": "alpert_gallery"
  },
  {
    "name": "Alyoshkinskiy Forest",
    "description": "",
    "pos": [
      37.42859,
      55.87727
    ],
    "fact_id": "alyoshkinskiy_forest"
  },
  {
    "name": "American Art Museum",
    "description": "",
    "pos": [
      37.59259,
      55.75475
    ],
    "fact_id": "american_art_museum"
  },
  {
    "name": "Andrei Mityayev's Museum of the History of Cycling",
    "description": "",
    "pos": [
      37.65608,
      55.79302
    ],
    "fact_id": "andrei_mityayev's_museum_of_the_history_of_cycling"
  },
  {
    "name": "Andrey Bely's Memorial Apartment",
    "description": "",
    "pos": [
      37.59655,
      55.75147
    ],
    "fact_id": "andrey_bely's_memorial_apartment"
  },
  {
    "name": "Andrey Shchukin Theater Arts Workshop",
    "description": "",
    "pos": [
      37.60528,
      55.76148
    ],
    "fact_id": "andrey_shchukin_theater_arts_workshop"
  },
  {
    "name": "Andrey Stratilat Temple",
    "description": "",
    "pos": [
      37.57484,
      55.71204
    ],
    "fact_id": "andrey_stratilat_temple"
  },
  {
    "name": "Andronikov Monastery",
    "description": "",
    "pos": [
      37.670605,
      55.749065
    ],
    "fact_id": "andronikov_monastery"
  },
  {
    "name": "Anna and Yury Mirakov's Gallery",
    "description": "",
    "pos": [
      37.59675,
      55.77344
    ],
    "fact_id": "anna_and_yury_mirakov's_gallery"
  },
  {
    "name": "Anna Golubkina Memorial Studio",
    "description": "",
    "pos": [
      37.58817,
      55.74227
    ],
    "fact_id": "anna_golubkina_memorial_studio"
  },
  {
    "name": "Annunciation Temple",
    "description": "",
    "pos": [
      37.60614,
      55.32609
    ],
    "fact_id": "annunciation_temple"
  },
  {
    "name": "Another Theatre",
    "description": "",
    "pos": [
      37.58575,
      55.77643
    ],
    "fact_id": "another_theatre"
  }
]


def test_get_sights_by_city():
    response = client.post(
        "/facts_searcher/city",
        json=["Moscow"],
    )

    assert response.status_code == 200
    assert response.json() == results
