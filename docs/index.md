## Gas measurement
Gas meter: BK-G4T 
* Small magnet inserted on last position of counter in digit '6' - [czech trial](http://mujweb.cz/videoservis/sdsmicro.htm)<br>
![gasmeter](gasmeter-6.jpg)
* 3d model of [Reed sensor holder](https://www.thingiverse.com/thing:1949041). You can 3d print it by [3d hubs](https://www.3dhubs.com) if you do not have 3d printer.<br>
![holder](sensor-holder.jpg)
* Reed sensor from [Aliexpress](https://www.aliexpress.com/item/10pcs-KSK-1A-Reed-Switch-2x14mm-Green-Glass-Usually-Open-For-Sensors-100-Original/32424207994.html?spm=a2g0s.9042311.0.0.uL3Znj). Be careful, it is fragile. I destroyed 2 of them just by bending wires.<br>
![reed-switch](reed-switch.jpg)

## Google Docs
Push data to Google docs spreadsheet<br>
[API](https://developers.google.com/sheets/api/quickstart/python)<br>
(c:\Python27>scripts\pip install --upgrade google-api-python-client)<br>
[append](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append)

## Autostart application on rpi after boot
* `sudo vi /etc/rc.local` (or any other editor, **vi** is considered to be clumsy :) )
* add before `'exit 0'`: `/usr/bin/python /home/pi/SeeHome/sensors.py` (considering `SeeHome` as your project folder)

## Git/Github basics
* [Add files](https://help.github.com/articles/adding-a-file-to-a-repository-using-the-command-line/)
`$ git clone https://github.com/afarkari/SeeHome.git`
`$ git add filename`
`$ git commit -m "add change locally and prepare for push"`
`$ git push origin branchname`
`$ git pull origin master`


## Visual Studio & Python
As project is in python 2.7 and you have most probably 3.6 with your PC, you have to manage multiple python environments in Visual Studio.
[VS](https://docs.microsoft.com/en-us/visualstudio/python/python-environments)<br>
But `pip install RPi.GPIO` will not run on Windows machine, this library is ment only for rpi.
