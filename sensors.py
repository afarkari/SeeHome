#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.
import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as io
from time import gmtime, strftime

# Raspberry Pi pin configuration:
lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 4
reed_pin      = 27

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Alternatively specify a 20x4 LCD.
# lcd_columns = 20
# lcd_rows    = 4

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,lcd_columns, lcd_rows, lcd_backlight)

# Print a two line message
lcd.clear()
lcd.message('Reed')

io.setmode(io.BCM)
io.setup(27, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp

global gas_ticks
global gas_total
global time_stamp
gas_ticks, gas_total = 0, 0
time_stamp = time.time()  

def gas_meter(channel):
    global gas_ticks
    global gas_total
    global time_stamp
    if io.event_detected(channel):
        time_now = time.time()  
        if (time_now - time_stamp) >= 5:  # 5 sec to ignore signals (filter)
            gas_ticks += 1
            gas_total += 1
            lcd.set_cursor(0,0)
            lcd.message('N:'+str(gas_ticks)+' T:'+str(gas_total)+'    ')
            time_stamp = time_now 

io.add_event_detect(27, io.RISING, callback=gas_meter)   # io.FALLING / RISING
# io.add_event_detect(27, io.FALLING, callback=gas_meter)

ll=0

while True:
    ll=ll+1
    time_text_long = strftime("%Y/%m/%d %H:%M:%S", gmtime())
    time_text_short = strftime("%H:%M", gmtime())
    lcd.set_cursor(0,1)
    lcd.message(time_text_short+' l:'+str(ll)+'  ')
    f = open('/home/pi/SeeHome/gasmeter.csv', 'a')
    f.write(time_text_long+', '+str(gas_ticks)+'\n')  # python will convert \n to os.linesep
    f.close() 
    gas_ticks = 0
    time.sleep(60*10)  # 60 sec * 10 min
    # time.sleep(6*1)  # 60 sec * 10 min

