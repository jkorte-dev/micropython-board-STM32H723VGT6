include("$(PORT_DIR)/boards/manifest.py")

freeze("$(BOARD_DIR)/modules")

# drivers
require("ssd1306")
require("neopixel")

# micropython-lib: file utilities
require("upysh")

