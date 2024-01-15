# mount external flash on spi1 on stm32h723
# used winbond from https://github.com/brainelectronics/micropython-winbond
# mpremote connect /dev/cu.usbmodem3054386A35322 mip install "github:brainelectronics/micropython-winbond"

import os
from machine import SPI, Pin
from winbond import W25QFlash

flash = W25QFlash(spi=SPI(1), cs=Pin('D6'), baud=2000000, software_reset=True)
flash_mount_point = '/external'

try:
    os.mount(flash, flash_mount_point)
except Exception as e:
    if e.errno == 19:
        # [Errno 19] ENODEV aka "No such device"
        # create the filesystem, this takes some seconds (approx. 10 sec)
        print('Creating filesystem for external flash ...')
        print('This might take up to 10 seconds')
        #os.VfsFat.mkfs(flash)
    else:
        # takes some seconds/minutes (approx. 40 sec for 128MBit/16MB)
        print('Formatting external flash ...')
        print('This might take up to 60 seconds')
        # !!! only required on the very first start (will remove everything)
        #flash.format()

        # create the filesystem, this takes some seconds (approx. 10 sec)
        print('Creating filesystem for external flash ...')
        print('This might take up to 10 seconds')
        # !!! only required on first setup and after formatting
        #os.VfsFat.mkfs(flash)
        
    print('Filesystem for external flash created')

    # finally mount the external flash
    #os.mount(flash, flash_mount_point)
     
print(os.listdir('/'))
