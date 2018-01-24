RaspberryPi-Radio
=================
Touch screen Internet streaming radio for the Raspberry Pi using the [Adafruit PiTFT 2.8" Touchscreen](https://adafruit.com/product/1601)

---

##### Forked from uktechreviews/RaspberryPi-Radio
Primarily changed interface, added station menu so you don't have to seek through 100+ stations, parse and display station info coming from stream. Better experience for people who want a lot of stations. 

---

[The original uktechreviews tutorial for setting up and installing the Radio Player can be found here](https://learn.adafruit.com/raspberry-pi-radio-player-with-touchscreen?view=all)

`pi-radio.pls` is a playlist file of internet radio streams  
`stations.txt` is the list of radio stations for display

To make the radio start on boot:
```
sudo chmod +x /path/to/start_script.a
```

Edit `/etc/rc.local` and paste
```
sudo /path/to/start_script.a &
```
before `end`

This will cause `start_script.a` to run on boot, which starts mpc with the radio playlist and launches starts the radio interface.

