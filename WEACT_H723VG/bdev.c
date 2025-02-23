#include "spi.h"
#include "octospi.h"
#include "storage.h"
#include "py/obj.h"

#if !MICROPY_HW_ENABLE_INTERNAL_FLASH_STORAGE

#if WEACT_USE_QSPI_FLASH_STORAGE
// QSPI Section
#if MICROPY_HW_SPIFLASH_ENABLE_CACHE
// Shared cache for first and second SPI block devices
static mp_spiflash_cache_t spi_bdev_cache;
#endif

// First external SPI flash uses software QSPI interface
#ifndef WEACT_USE_OCTOSPI
static const mp_soft_qspi_obj_t soft_qspi_bus = {
    .cs  = MICROPY_HW_OSPIFLASH_CS,
    .clk = MICROPY_HW_OSPIFLASH_SCK,
    .io0 = MICROPY_HW_OSPIFLASH_IO0,
    .io1 = MICROPY_HW_OSPIFLASH_IO1,
    .io2 = MICROPY_HW_OSPIFLASH_IO2,
    .io3 = MICROPY_HW_OSPIFLASH_IO3,
};
#endif

// First external SPI flash uses software QSPI interface
const mp_spiflash_config_t spiflash_config = {
    .bus_kind = MP_SPIFLASH_BUS_QSPI,
    #ifdef WEACT_USE_OCTOSPI
    .bus.u_qspi.data = NULL,
    .bus.u_qspi.proto = &octospi_proto,
    #else
    .bus.u_qspi.data = (void *)&soft_qspi_bus,
    .bus.u_qspi.proto = &mp_soft_qspi_proto,
    #endif
    #ifdef MICROPY_HW_SPIFLASH_ENABLE_CACHE
    .cache = &spi_bdev_cache,
    #endif
};

spi_bdev_t spi_bdev;

#else //  normal SPI

static mp_spiflash_cache_t spi_bdev_cache;

//  Hardware SPI currently not working
/*
static const spi_proto_cfg_t spi_bus = {
    .spi = &spi_obj[0], // SPI1 hardware peripheral
    .baudrate = 25000000,
    .polarity = 0,
    .phase = 0,
    .bits = 8,
    .firstbit = SPI_FIRSTBIT_MSB,
};
const mp_spiflash_config_t spiflash_config = {
    .bus_kind = MP_SPIFLASH_BUS_SPI,
    .bus.u_spi.cs = MICROPY_HW_SPIFLASH_CS,
    .bus.u_spi.data = (void *)&spi_bus
    .bus.u_spi.proto = &spi_proto
    .cache = &spi_bdev_cache,
};
*/

// Software SPI
static const mp_soft_spi_obj_t soft_spi_bus = {
    .delay_half = MICROPY_HW_SOFTSPI_MIN_DELAY,
    .polarity = 0,
    .phase = 0,
    .sck = MICROPY_HW_SPIFLASH_SCK,
    .mosi = MICROPY_HW_SPIFLASH_MOSI,
    .miso = MICROPY_HW_SPIFLASH_MISO,
};

const mp_spiflash_config_t spiflash_config = {
    .bus_kind = MP_SPIFLASH_BUS_SPI,
    .bus.u_spi.cs = MICROPY_HW_SPIFLASH_CS,
    .bus.u_spi.data = (void *)&soft_spi_bus,
    .bus.u_spi.proto = &mp_soft_spi_proto,
    .cache = &spi_bdev_cache,
};

spi_bdev_t spi_bdev;
#endif
#endif

