from micropython import const
import lvgl as lv
import machine
import lcd_bus
import ili9341
import xpt2046
import touch_cal_data
import task_handler


# ============== Customize settings ============== #
# The following values need to be customized.

# Switch width and height for portrait mode.
DISPLAY_WIDTH = const(320)
DISPLAY_HEIGHT = const(240)
# Try different values from rotation table, see below.
_DISPLAY_ROT = const(0x20)
# Set to True if red and blue are switched.
_DISPLAY_BGR = const(1)
# May have to be set to 0 if both RGB / BGR mode give bad results.
_DISPLAY_RGB565_BYTE_SWAP = const(1)
# Allow touch calibration. Set to True when display works correctly.
_ALLOW_TOUCH_CAL = const(1)

'''
MADCTL_TABLE = {
    (False, 0): 0x80, # mirroring = False
    (False, 90): 0xE0,
    (False, 180): 0x40,
    (False, 270): 0x20,
    (True, 0): 0xC0, # mirroring = True
    (True, 90): 0x60,
    (True, 180): 0x00,
    (True, 270): 0xA0
}
'''


# ============== Display / Indev initialization ============== #
# no need to change anything below here
_SPI_BUS_HOST = const(1)
_SPI_BUS_MOSI = const(13)
_SPI_BUS_MISO = const(12)
_SPI_BUS_SCK = const(14)
_INDEV_BUS_HOST = const(2)
_INDEV_BUS_MOSI = const(32)
_INDEV_BUS_MISO = const(39)
_INDEV_BUS_SCK = const(25)
_INDEV_DEVICE_FREQ = const(2000000)
_INDEV_DEVICE_CS = const(33)
_DISPLAY_BUS_FREQ = const(24000000)
_DISPLAY_BUS_DC = const(2)
_DISPLAY_BUS_CS = const(15)
_DISPLAY_BACKLIGHT_PIN = const(21)

spi_bus = machine.SPI.Bus(
    host=_SPI_BUS_HOST,
    mosi=_SPI_BUS_MOSI,
    miso=_SPI_BUS_MISO,
    sck=_SPI_BUS_SCK
)

indev_bus = machine.SPI.Bus(
    host=_INDEV_BUS_HOST,
    mosi=_INDEV_BUS_MOSI,
    miso=_INDEV_BUS_MISO,
    sck=_INDEV_BUS_SCK
)

indev_device = machine.SPI.Device(
    spi_bus=indev_bus,
    freq=_INDEV_DEVICE_FREQ,
    cs=_INDEV_DEVICE_CS
)

display_bus = lcd_bus.SPIBus(
    spi_bus=spi_bus,
    freq=_DISPLAY_BUS_FREQ,
    dc=_DISPLAY_BUS_DC,
    cs=_DISPLAY_BUS_CS
)

display = ili9341.ILI9341(
    data_bus=display_bus,
    display_width=DISPLAY_WIDTH,
    display_height=DISPLAY_HEIGHT,
    backlight_pin=_DISPLAY_BACKLIGHT_PIN,
    backlight_on_state=ili9341.STATE_PWM,
    color_space=lv.COLOR_FORMAT.RGB565,
    color_byte_order=ili9341.BYTE_ORDER_BGR if _DISPLAY_BGR else ili9341.BYTE_ORDER_RGB,
    rgb565_byte_swap=_DISPLAY_RGB565_BYTE_SWAP
)

# The rotation table MUST be defined
display._ORIENTATION_TABLE = (
    _DISPLAY_ROT, # this value sets the rotation
    0x0, # placeholder
    0x0, # placeholder
    0x0 # placeholder
)

# lv.DISPLAY_ROTATION._0 uses the first value from the
# display._ORIENTATION_TABLE to set display rotation
display.set_rotation(lv.DISPLAY_ROTATION._0)
display.set_power(True)
display.init(1)
display.set_backlight(100)


indev = xpt2046.XPT2046(device=indev_device)

# Calibration data is stored in the non-volatile storage (NVS) of the Esp32
if not indev.is_calibrated and _ALLOW_TOUCH_CAL:
    indev.calibrate()
    indev._cal.save()


task_handler.TaskHandler()