# color_setup.py Customise for your hardware config

# Released under the MIT License (MIT). See LICENSE.
# Copyright (c) 2020 Peter Hinch


from machine import Pin, PWM, SPI
import gc
import time
import framebuf


# nano gui
from color_setup import ssd
from gui.core.colors import * 
from gui.core.nanogui import refresh
from gui.core.writer import CWriter  # Renders custom text fonts
from gui.widgets.label import Label
import gui.fonts.arial35 as arial35
import gui.fonts.arial10 as arial10
import sys


def hsv_to_rgb(h, s, v):
    """
    Converts HSV to RGB.

    Input:
        h: 0..360 (Degree)
        s: 0.0..1.0
        v: 0.0..1.0

    Outout:
        (r, g, b) 0..255
    """

    h = h % 360
    if s < 0:
        s = 0
    elif s > 1:
        s = 1

    if v < 0:
        v = 0
    elif v > 1:
        v = 1

    if s == 0:
        gray = round(v * 255)
        return (gray, gray, gray)

    c = v * s
    h_section = h / 60
    x = c * (1 - abs((h_section % 2) - 1))
    m = v - c

    if h_section < 1:
        r1, g1, b1 = c, x, 0
    elif h_section < 2:
        r1, g1, b1 = x, c, 0
    elif h_section < 3:
        r1, g1, b1 = 0, c, x
    elif h_section < 4:
        r1, g1, b1 = 0, x, c
    elif h_section < 5:
        r1, g1, b1 = x, 0, c
    else:
        r1, g1, b1 = c, 0, x

    r = round((r1 + m) * 255)
    g = round((g1 + m) * 255)
    b = round((b1 + m) * 255)

    return (r, g, b)


def rainbow_text(txt, x, y, centered=True, start=0, s=0.85, v=1):
    l = len(txt)
    
    x = x - (l * 4) if centered else x
    x = 0 if x < 0 else x
    
    if s < 0:
        s = 0
    elif s > 1:
        s = 1
    
    if v < 0:
        v = 0
    elif v > 1:
        v = 1
    
    ssd.rect(x, y, l * 8, 8, 0, 1)
    
    for i in range(l):
        h = int((start + 360 / (l) * i) % 360)
        ssd.text(txt[i], x + 8 * i, y, SSD.rgb(*hsv_to_rgb(h, s, v)))

class TextMPY:
    def __init__(self, parent_buffer, text, pos_x, pos_y, color = 1, bg_color = 0):
        self.parent_buffer = parent_buffer
        self.text = str(text)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.bg_color = bg_color

        self._prev_text = self.text
        
        self.parent_buffer.rect(self.pos_x, self.pos_y, len(self.text) * 8, 8, self.bg_color, 1)
        self.parent_buffer.text(self.text, self.pos_x, self.pos_y, self.color)

        
            
    def update(self, text):
        self.hide()
        
        self.text = text
        self.parent_buffer.text(self.text, self.pos_x, self.pos_y, self.color)
        
        
    @property
    def width(self):
        return int(len(self.text) * 8)
    
    @property
    def height(self):
        return 8
    
    def hide(self):
        self.parent_buffer.rect(self.pos_x, self.pos_y, len(self.text) * 8, 8, self.bg_color, 1)

import framebuf

class ImagePBM:
    def __init__(self, parent_buffer, image_file, fg_color=WHITE,
                 bg_color=BLACK, pos_x=None, pos_y=None):
        self.parent_buffer = parent_buffer
        self.image_file = image_file
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.fg_color = fg_color
        self.bg_color = bg_color

        self.w = 0
        self.h = 0
        self.data = None
        self.fbuf = None

        pbuf = bytearray(4) # custom palette
        self._palette = framebuf.FrameBuffer(pbuf, 2, 1, framebuf.RGB565)
        self._palette.pixel(0, 0, self.bg_color)
        self._palette.pixel(1, 0, self.fg_color)

        self._load_image(image_file)

        if self.pos_x is not None and self.pos_y is not None:
            self.show(self.pos_x, self.pos_y)

    def update(self, image_file, pos_x=None, pos_y=None):
        if self.pos_x is not None and self.pos_y is not None:
            self.hide()

        self.image_file = image_file
        self._load_image(image_file)

        if pos_x is not None:
            self.pos_x = pos_x
        if pos_y is not None:
            self.pos_y = pos_y

        if self.pos_x is not None and self.pos_y is not None:
            self.show(self.pos_x, self.pos_y)

    def _load_image(self, image_file):
        with open(image_file, 'rb') as f:

            magic = f.readline().strip()
            if magic != b'P4':
                raise ValueError('Only PBM files (P4) are supported by this class.')

            line = f.readline()
            while line.startswith(b'#'):
                line = f.readline()

            self.w, self.h = map(int, line.split())

            self.data = bytearray(f.read())

            expected_size = ((self.w + 7) // 8) * self.h
            if len(self.data) != expected_size:
                raise ValueError(
                    'PBM file: Wrong size. Found: {}. Expected: {}'.format(len(self.data), expected_size)
                )

            self.fbuf = framebuf.FrameBuffer(
                self.data,
                self.w,
                self.h,
                framebuf.MONO_HLSB
            )

    @property
    def width(self):
        return self.w

    @property
    def height(self):
        return self.h

    def hide(self):
        if self.pos_x is not None and self.pos_y is not None:
            self.parent_buffer.fill_rect(self.pos_x, self.pos_y, self.w, self.h, self.bg_color)

    def show(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

        print('[{}]: Showing image file "{}" at ({}, {})'.format(
            self.__class__.__name__,
            self.image_file,
            self.pos_x,
            self.pos_y
        ))
        print('with dimensions of width = {} px and height = {} px.'.format(
            self.w,
            self.h
        ))

        # Transparent bg.
        self.parent_buffer.blit(self.fbuf, self.pos_x, self.pos_y, 0, self._palette)

        # Draw bg_color to parent buffer.
        # self.parent_buffer.blit(self.fbuf, self.pos_x, self.pos_y, -1, self._palette)


# Load fonts for GUI

CWriter.set_textpos(ssd, 0, 0)  # In case previous tests have altered it
wri1 = CWriter(ssd, arial35, SSD.rgb(255, 128, 0), BLACK, verbose=False)
wri1.set_clip(True, True, False)

wri2 = CWriter(ssd, arial10, YELLOW, BLACK, verbose=False)
wri2.set_clip(True, True, False)

# Start GUI
refresh(ssd, True)  # Initialise and clear display

# Using micropython's primitive draw functions
# Drawing a border
thickness = 10
width = 320
height = 240

color = YELLOW # inner border
ssd.rect(0, 0, width, thickness, color, 1) # top
ssd.rect(0, 0, thickness, height, color, 1) # left
ssd.rect(width - thickness, 0, thickness, height, color, 1) # right
ssd.rect(0, height - thickness, width, thickness, color, 1) # bottom

color = BLACK # outer border
ofs = 5
ssd.rect(0, 0, width, ofs, color, 1) # top
ssd.rect(0, 0, ofs, height, color, 1) # left
ssd.rect(width - ofs, 0, ofs, height, color, 1) # right
ssd.rect(0, height - ofs, width, ofs, color, 1) # bottom


ssd.rect(int(width / 2) - 40, 160, 20, 20, RED, 1)
ssd.rect(int(width / 2) - 10, 160, 20, 20, GREEN, 1)
ssd.rect(int(width / 2) + 20, 160, 20, 20, BLUE, 1)


# Displaying some text (standard 8x8 monospace font)
text_margin = 3
text_content = 'Micropython\'s Standard 8x8 Mono Font'
# ssd.text(text_content, thickness + text_margin,
#          height - thickness - 8 - text_margin, WHITE)
rainbow_text(text_content, 15, 220, centered= False, start=180)



# Using nanogui Label class with a custom font
# This label's text is centered and it's value can be updated
offset = 95
large_label = Label(wri1, 45, thickness + offset, width - 2 * thickness - offset, align=2)
large_label.value('Large Font')

small_label = Label(wri2, 90, thickness + offset, width - 2 * thickness - offset, align=2)
small_label.value('Small Font')

rainbow_text('COLOR_TEST', 160, 145, centered = True)

image = ImagePBM(ssd,'Hamster_100.pbm', fg_color = YELLOW)
image.show(thickness + text_margin + 10, thickness + text_margin + 10)

mono_2 = TextMPY(ssd, 'Image Test', 24, 125, color = WHITE, bg_color = BLACK)


refresh(ssd)

while True:
    time.sleep(1)