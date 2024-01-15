# micropython-board-STM32H723VGT6
![display](images/mpy_stm32h723.png)

Micropython Board Definition for WeAct Studio Board with STM32H723VGT6
[WeActStudio.MiniSTM32H723](https://github.com/WeActStudio/WeActStudio.MiniSTM32H723)



## Current status

> This is work in progess based on micropython v1.21.0 (tagged version)

SPI flash works in soft spi mode only (both single and quad (octospi)). Octospi needs modification of octospi.c (see patch dir. I also modified stm32h723_af.csv to make it compile. This is just a temporary hack.
To compile on unmodified micropython QSPI Flash has to be disabled.


Supported features so far:

- working: USB repl, ST7735 TFT Display, LED, user button, SD card, SPI, I2C, ADC 
- should work (not tested): I2C, UART, TIMER, DAC, RTC CAN, RNG
- not working:  I2S, camera 

Firmware build is based on tagged version of micropython v1.21.0 and includes display driver from Russ Hughes with some fonts and brainelectronic's Winbond flash driver to mount SPI flash connected to SPI1 

## Credits
credits to:
- The micropython team!
- Russ Hughes for his great and fast display driver (in c) [st7789_mpy]( https://github.com/russhughes/st7789_mpy) 
- brainelectronic for the flash driver [micropython-winbond](https://github.com/brainelectronics/micropython-winbond)
- ST7735 display driver (pure python) from boochow [MicroPython-ST7735](https://github.com/boochow/MicroPython-ST7735)

## change log
15.01.2024 initial version.
