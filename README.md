# static_pokemon_go_alert
Makes use of data from [sgpokemap.com.sg](sgpokemap.com.sg) to alert you of Pokemon nearby. This script is suitable for a Ubuntu machine running in your house so that you can make it say what pokemon is nearby.

Tested only on Ubuntu 14.04 with Python 2.7.6. On other environments, the ```requests``` module for python will behave differently.

## Step 1
Install this first. It is for the audio alert when there is a pokemon. You can use other text-to-speech packages if you like, but you will have to edit the code. You can use ```espeak```, it pronounces pokemon names better.
```
sudo apt-get install gnustep-gui-runtime
```

## Step 2
Next open up the ```poke_map.py``` file with your favourite editor and edit the latitude and longitude values to your own location. You can adjust the range (in metres) too.

## Step 3
To run:
```
python poke_map.py
# Ensure that list_of_pokemon.json is in the same directory.
```

## Step 4
Use Ubuntu's crontab to run this periodically and you have yourself a pokemon alert for your house.
Insert this into your crontab, this will make the script run every 3 minutes from 10am to 10pm.
```
*/3 10-21 * * * python ~/Desktop/static_pokemon_go_alert/poke_map.py
```
