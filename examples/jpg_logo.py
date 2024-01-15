"""
logo.py

    Draw the MicroPython Logo.

"""

import st7789
import tft_config

tft = tft_config.config(rotation=3)

def main():
    """
    Decode and draw jpg on display
    """

    try:
        tft.init()
        width=tft.width()
        height=tft.height()

        image = f'logo-{width}x{height}.jpg'
        print(f"Loading {image}")
        tft.jpg(image, 0, 0, st7789.SLOW)

        #tft.show()

    finally:
        #tft.deinit()
        pass


main()
