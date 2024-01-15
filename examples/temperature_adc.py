from st7735py import TFT
from sysfont import sysfont
from machine import SPI,Pin
import time
import os

spi = SPI(4, baudrate=31250000)
Pin('E10', Pin.OUT) # init backlight

tft=TFT(spi,'E13','D15','E11') # spi, aDC, aReset, aCS
tft.rgb(True)
tft.initr()

# settings for small 0.96'' 80x160 display
tft.invertcolor(True)
tft.rotation(3)

def show(text, pos=(50,50), size=1, clear=True):
    if clear:
        tft.fill(TFT.BLACK)
    tft.text(pos, text, TFT.WHITE, sysfont, size)

adcall = pyb.ADCAll(12, 0x70000) # 12 bit resolution, internal channels
temp = adcall.read_core_temp()
#print(temp)

show("{:.2f} C".format(temp) , (40, 60), 2)

time.sleep(5)

sd=pyb.SDCard()
if sd.present():
    os.mount(sd, '/sd')
    #os.listdir('/sd')
    for f in os.listdir('/sd'):
      show(f, (10,40))
      time.sleep_ms(500)
    

#print(os.statvfs('/'))

flash_stat = os.statvfs('/flash')
show("flash total {:n} kB".format(flash_stat[1]*flash_stat[2]/1024), (10,50))
show("flash  free {:n} kB".format(flash_stat[1]*flash_stat[3]/1024), (10,70), clear=False)

pyb.Switch().callback(lambda: pyb.LED(1).toggle())

while True:
    pass
    