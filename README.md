# static_pokemon_go_alert
Makes use of data from [sgpokemap.com.sg](sgpokemap.com.sg) to alert you of Pokemon nearby.

Will run fine on Ubuntu. On other environments, the ```requests``` module for python will behave differently.

Install this first. It is for the audio alert when there is a pokemon.
```
sudo apt-get install gnustep-gui-runtime
```

To run:
```
python poke_map.py
# Ensure that list_of_pokemon.json is in the same directory.
```

Use Ubuntu's crontab to run this periodically and you have yourself a pokemon alert for your house.
