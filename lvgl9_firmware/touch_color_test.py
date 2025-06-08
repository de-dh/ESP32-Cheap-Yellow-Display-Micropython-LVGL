from micropython import const
import lvgl as lv
import time
import machine
import lcd_bus
import ili9341
import xpt2046
import touch_cal_data
import task_handler
from machine import Timer

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
_DISPLAY_WIDTH = const(320)
_DISPLAY_HEIGHT = const(240)
_DISPLAY_BACKLIGHT_PIN = const(21)
_DISPLAY_RGB565_BYTE_SWAP = const(1)

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
    display_width=_DISPLAY_WIDTH,
    display_height=_DISPLAY_HEIGHT,
    backlight_pin=_DISPLAY_BACKLIGHT_PIN,
    backlight_on_state=ili9341.STATE_PWM,
    color_space=lv.COLOR_FORMAT.RGB565,
    color_byte_order=ili9341.BYTE_ORDER_RGB,
    rgb565_byte_swap=_DISPLAY_RGB565_BYTE_SWAP
)

'''
Different versions of the CYD require different MADCTL (Display rotation / mirroring) cmds.
They must be determined by try and error.

Excerpt from the ILI9341 driver's MADCTL configurations for rotation and mirroring.
First value stands for mirroring, second value stands for rotation.

MIRROR_ROTATE = {
    (False, 0): 0x80, 
    (False, 90): 0xE0,
    (False, 180): 0x40,
    (False, 270): 0x20,
    (True, 0): 0xC0,
    (True, 90): 0x60,
    (True, 180): 0x00,
    (True, 270): 0xA0
}

D5 - MV 0x20
D6 - MX 0x40
D7 - MY 0x80

'''


display._ORIENTATION_TABLE = (
    0x240,#0x240
    0xE0,# not working, just a placeholder
    0x20,
    0x20,# not working, just a placeholder
)

display.set_rotation(lv.DISPLAY_ROTATION._0)
display.set_power(True)
display.init(1)
display.set_backlight(100)

# Modified version of the xpt2046 driver with swapxy feature is required
indev = xpt2046.XPT2046(device=indev_device, swapxy = True)

do_calibration = 0

# Calibration data is stored in the non-volatile storage (NVS) of the Esp32
# x/y-mirroring required for CYD
if do_calibration:
    indev.calibrate()
    indev._cal.mirrorY = not indev._cal.mirrorY
    indev._cal.mirrorX = not indev._cal.mirrorX
    indev._cal.save()

task_handler.TaskHandler()


############### UI Starts Here #####################


def palette_color(c, shade = 0):
    '''
    Returns a color from LVGL's main palette and
    lightens or darkens the color by a specified shade.
    
    Palette Colors:
    RED, PINK, PURPLE, DEEP_PURPLE, INDIGO, BLUE,
    LIGHT_BLUE, CYAN, TEAL, GREEN, LIGHT_GREEN, LIME, 
    YELLOW, AMBER, ORANGE, DEEP_ORANGE, BROWN, BLUE_GREY, GREY
    '''
    attr = getattr(lv.PALETTE, c.upper(), 'Undefined')
    if attr != 'Undefined':
        if not (shade in range(-4, 6)): return lv.color_black()
        if shade == 0:
            return lv.palette_main(attr)
        elif shade > 0:
            return lv.palette_lighten(attr, shade)
        elif shade < 0:
            return lv.palette_darken(attr, abs(shade))
    else:
        return lv.color_black()

class RectStyle(lv.style_t):
    def __init__(self, bg_color=lv.color_black()):
        super().__init__()
        self.set_bg_opa(lv.OPA._100)
        self.set_bg_color(bg_color)
        self.set_text_opa(lv.OPA._100)
        self.set_text_color(lv.color_black())


class Rect():
    def __init__(self, align, color, parent):
        self.align = align
        self.color = color
        self.parent = parent
        
        self.lvalign = getattr(lv.ALIGN, self.align, 'Undefined')
        
        s = self.align.split('_') # Remove undersore from align value and
        self.text = s[0][0] + s[1][0] # converts e.g. TOP_LEFT to TL as shortcut
        
        self.rect = lv.obj(parent)
        self.rect.remove_style_all()
        self.rect.set_size(35, 35)
        self.rect.align(self.lvalign, 0, 0)
        self.rect.add_style(RectStyle(bg_color = palette_color(self.color)), lv.PART.MAIN)
        self.rect.add_style(RectStyle(bg_color = lv.color_white()), lv.PART.MAIN | lv.STATE.PRESSED)
        self.rect.add_event_cb(lambda e: self._cb(), lv.EVENT.CLICKED, None)
        
        self.lbl = lv.label(self.rect)
        self.lbl.remove_style_all()
        self.lbl.set_text(self.text)
        self.lbl.center()
        
    
    def _cb(self):
        # Get touch coordinates
        point = lv.point_t()
        indev.get_point(point)

        status_lbl.set_text(f'{self.align.replace("_", " ")} obj clicked!\n(x: {point.x}, y: {point.y})')
        status_lbl.set_style_text_color(palette_color(self.color), 0)
        
class FlexRowStyle(lv.style_t):
    def __init__(self):
        super().__init__()
        
        self.set_text_align(lv.TEXT_ALIGN.CENTER)
        
        self.set_flex_flow(lv.FLEX_FLOW.ROW_WRAP)
        self.set_flex_main_place(lv.FLEX_ALIGN.SPACE_EVENLY)
        self.set_layout(lv.LAYOUT.FLEX)

class CircleStyle(lv.style_t):
    def __init__(self):
        super().__init__()

        self.set_bg_opa(lv.OPA._40)
        self.set_bg_color(lv.color_hex3(0x0F0))
        self.set_radius(999)
        self.set_border_opa(lv.OPA._100)
        self.set_border_width(2)
        self.set_border_color(lv.color_hex3(0x0F0))

class TouchIndicator():
    def __init__(self, position_x, position_y):
        
        _size = 10
        self.circle = lv.obj(lv.screen_active())
        self.circle.remove_style_all()
        self.circle.set_size(_size, _size)
        self.circle.set_pos(int(position_x - _size), int(position_y - _size))
        self.circle.add_style(CircleStyle(), lv.PART.MAIN)
    
    def delete(self):
        self.circle.delete()


ti = None # Store TouchIndicator object between calls of touch_cb
def touch_cb(e = None):
    global ti
    code = e.get_code()
    
    if code == lv.EVENT.CLICKED:
        if ti is not None:
            ti.delete()
        
        point = lv.point_t()
        indev.get_point(point)
        
        ti = TouchIndicator(point.x, point.y)
    else:
        pass

group = lv.group_create()
group.set_default()

scr = lv.screen_active()
scr.set_style_bg_color(lv.color_black(), lv.PART.MAIN)
scr.remove_flag(lv.obj.FLAG.SCROLLABLE)

indev.add_event_cb(touch_cb, lv.EVENT.ALL, None)

# This label will display touch coordinates / clicked object
status_lbl = lv.label(scr)
status_lbl.set_text('Touch Test,\nClick Anywhere.')
status_lbl.align(lv.ALIGN.CENTER, 0, -40)
status_lbl.set_style_text_color(lv.color_white(), 0)
status_lbl.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)

# Container provides margin from display for the rects
rect_container = lv.obj(scr)
rect_container.remove_style_all()
rect_container.set_size(lv.pct(100), lv.pct(100))
rect_container.align(lv.ALIGN.TOP_LEFT, 0, 0)
rect_container.set_style_pad_all(10, 0)

# Create rectangular objets as touch targets
align = ['BOTTOM_LEFT', 'BOTTOM_MID', 'BOTTOM_RIGHT', 'LEFT_MID',
         'RIGHT_MID', 'TOP_LEFT', 'TOP_MID', 'TOP_RIGHT']

colors = ['CYAN', 'DEEP_PURPLE', 'GREEN', 'ORANGE',
          'PINK', 'LIME', 'RED', 'YELLOW']

for a, c in zip(align, colors):
    r = Rect(a, c, rect_container)

# Container for color display test
# Will display three rects in red, green and blue with labels
color_container = lv.obj(rect_container)
color_container.remove_style_all()
color_container.set_size(132, 40)
color_container.align(lv.ALIGN.CENTER, 0, 30)
color_container.add_style(RectStyle(bg_color = lv.color_black()), lv.PART.MAIN)
color_container.add_style(FlexRowStyle(), lv.PART.MAIN)

for l, c in (zip('rgb', (0xF00, 0x0F0, 0x00F))):
    color_rect = lv.obj(color_container)
    color_rect.remove_style_all()
    color_rect.set_size(lv.pct(30), lv.pct(100))
    color_rect.add_style(RectStyle(bg_color = lv.color_hex3(c)), lv.PART.MAIN)
    
    color_lbl = lv.label(color_rect)
    color_lbl.remove_style_all()
    color_lbl.set_text(l)
    color_lbl.center()
    color_lbl.set_style_text_color(lv.color_black(), 0)
    
    
color_container_lbl = lv.label(rect_container)
color_container_lbl.remove_style_all()
color_container_lbl.set_text('Color Test.')
color_container_lbl.align_to(color_container, lv.ALIGN.OUT_TOP_MID, 0, -5)
color_container_lbl.set_style_text_color(lv.color_white(), 0)

'''
Print available default lvgl fonts:
print([f for f in dir(lv) if 'font_montserrat' in f or 'font_unscii' in f])

['font_montserrat_10', 'font_montserrat_12', 'font_montserrat_14', 'font_montserrat_16',
'font_montserrat_24', 'font_montserrat_28', 'font_montserrat_32', 'font_montserrat_36',
'font_montserrat_40', 'font_montserrat_48', 'font_montserrat_8',
'font_unscii_16', 'font_unscii_8']
'''


while True:
    time.sleep(1)