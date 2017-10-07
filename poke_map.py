import requests
import ssl
import sys
import subprocess
import time
import json
import os
from geopy.distance import vincenty

current_lat_lng = (1.4191240, 103.8394725)
detection_radius = 200

def main():
	list_of_nearby_pokemon_ids = []

	pokemons = getDataFromSGPokeMap()["pokemons"]
	for pokemon in pokemons:
		if is_nearby(pokemon["lat"], pokemon["lng"]):
			list_of_nearby_pokemon_ids.append(str(pokemon["pokemon_id"]))

	if len(list_of_nearby_pokemon_ids) > 0:
		if len(list_of_nearby_pokemon_ids) == 1:
			sound_alert("PO KE MON Alert")
			sound_alert(get_pokemon_name(list_of_nearby_pokemon_ids) + " is nearby.")
			sound_alert(get_pokemon_name(list_of_nearby_pokemon_ids) + " is nearby.")
		else:
			sound_alert("PO KE MON Alert")
			sound_alert("There are " + str(len(list_of_nearby_pokemon_ids)) + " po ke mons nearby.")
			sound_alert("They are " + get_pokemon_name(list_of_nearby_pokemon_ids))

def getDataFromSGPokeMap():
	# current_epoch_time = int(time.time()) - 30
	list_of_pokemon_ids = get_list_of_pokemon_ids().rstrip(',')
	current_epoch_time = 0
	s = requests.Session()
	s.headers = {
		"authority": "sgpokemap.com",
		"method": "GET",
		"path": "/query2.php?since="+str(current_epoch_time)+"&mons="+list_of_pokemon_ids,
		"scheme": "https",
		"accept": "*/*",
		"accept-encoding": "gzip, deflate, sdch, br",
		"accept-language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,ms;q=0.2",
		"cache-control": "no-cache",
		"cookie": "__cfduid=d9d5d3857981c233bb3819b6f4fdbb6431474894290; _ga=GA1.2.522909688.1474894294; _gat=1",
		"pragma": "no-cache",
		"referer": "https://sgpokemap.com/",
		"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36",
		"x-requested-with": "XMLHttpRequest"
	}

	r = s.get("https://sgpokemap.com/query2.php?since="+str(current_epoch_time)+"&mons="+list_of_pokemon_ids, verify=False)

	if r.status_code != 200:
		print "Could not get json."
		sys.exit()
		
	return r.json()

def is_nearby(lat, lng):
	new_lat_lng = (lat, lng)
	return vincenty(current_lat_lng, new_lat_lng).meters <= detection_radius

def sound_alert(message):
	# subprocess.call(["./say.sh", message])
	# subprocess.call(["espeak", message])
	subprocess.call(["espeak", "-s", "160", "-v", "en-us+f2", message])

def get_list_of_pokemon_ids():
	with open(os.path.join(os.path.dirname(__file__), 'list_of_pokemon.json')) as data_file:
                data = json.load(data_file)
	result = ""
	for obj in data:
		result += obj["i"] + ","
	return result

def get_pokemon_name(array):
	with open(os.path.join(os.path.dirname(__file__), 'list_of_pokemon.json')) as data_file:
		data = json.load(data_file)
	result = ""
	for id in array:
		for obj in data:
			if obj["i"] == id:
				result += obj["n"] + ", "
	return result	

main();

