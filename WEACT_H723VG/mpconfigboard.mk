# MCU settings
MCU_SERIES = h7
CMSIS_MCU = STM32H723xx
MICROPY_FLOAT_IMPL = double
AF_FILE = boards/stm32h723_af.csv
#AF_FILE = $(BOARD_DIR)/stm32h723_af.csv

LD_FILES = boards/stm32h723.ld boards/common_basic.ld
TEXT0_ADDR = 0x08000000

ifeq ($(BOARD_VARIANT),OCTOSPI)
# Configure mpconfigboard.h.
CFLAGS += -DWEACT_USE_OCTOSPI
AF_FILE = $(BOARD_DIR)/stm32h723_af.csv
endif

# MicroPython settings
MICROPY_VFS_LFS2 = 1

FROZEN_MANIFEST ?= $(BOARD_DIR)/manifest.py
