## LVGL8 - Deprecated Documentation and Examples

The old [LVGL8 documentation and examples](LVGL8.md) can be found here.
It is not maintained and the programs are incompatible with LVGL9.

## LVGL9 Firmware
The `/lvgl9_firmware` folder contains a prebuilt firmware for the Cheap Yellow Display (CYD) using LVGL 9.3 and MicroPython 1.25.0. 


The firmware was compiled from commit [15a414b](https://github.com/lvgl-micropython/lvgl_micropython/commit/15a414bc03486017235234882ce7415532c6325e)  from  [Kdschlosser's Micropython Bindings](https://github.com/lvgl-micropython/lvgl_micropython). All drivers for the CYD are included in the firmware, no additional drivers are needed.


The firmware had to be compiled from a previous version of the bindings since the current version has a bug which puts the CYD in a boot loop. 
The firmware includes the touch fix kdschlosser/lvgl_micropython#454 for correct touch calibration.
The previous version of the precompiled firmware required a modified touch driver due to a bug in the calibration routine. This is obsolete now.


The following command is used to flash the firmware (esptool required):

```bash
python -m esptool --chip esp32 --port COMXX -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size 4MB --flash_freq 40m --erase-all 0x0 lvgl_micropython_cyd.bin
```


### Finding the correct display settings

The file `/lvgl9_firmware/color_test.py` can be used to find the correct display driver's rotation and color settings.
All neccessary settings can be customized at the top of the file. A hard reset is required after every execution of the program (the hardware might not work correctly otherwise).
The following steps have to be followed to correctly set up the CYD for LVGL9:

1. Before start: Set correct width and height (portrait vs. landscape).
2. Start program and find correct rotation settings (MADCTL).
3. Find correct color mode (RGB vs. BGR).
4. Calibrate the touchscreen.

```python
# ============== Customize settings ============== #
# The following values need to be customized.

# Switch width and height for portrait mode.
_DISPLAY_WIDTH = const(320)
_DISPLAY_HEIGHT = const(240)
# Try different values from rotation table, see below.
_DISPLAY_ROT = const(0xE0)
# Set to True if red and blue are switched.
_DISPLAY_BGR = const(1)
# May have to be set to 0 if both RGB / BGR mode give bad results.
_DISPLAY_RGB565_BYTE_SWAP = const(1)
# Allow touch calibration. Set to True when display works correctly.
_ALLOW_TOUCH_CAL = const(0)
# Show marker at current touch coordinates.
_DISPLAY_SHOW_TOUCH_INDICATOR = const(1)
```

Depending on the displays orientation the display's width and height might need to be edited before running the file. 
For use in landscape mode, `_DISPLAY_WIDTH = 240` and `_DISPLAY_HEIGHT = 320` have to be used. Switch the values for use in portrait mode.

Start the program now. If the displayed content is distorted the correct display rotation `_DISPLAY_ROT` needs to be found.
The following `MADCTL` values for rotation need to be tested by try and error.

```
# Part from rdagger's micropython ili9341 driver provided under MIT license.
# https://github.com/rdagger/micropython-ili9341/blob/master/ili9341.py

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
```

Next, the correct colormode has to be found
E.g. if the red square is rendered in blue then BGR mode must be used by setting `_DISPLAY_BGR = const(1)`. If RGB mode is required set `_DISPLAY_BGR = const(0)`.


The last step is the calibration of the touchscreen. Set `_ALLOW_TOUCH_CAL = const(0)` and follow the instructions on screen. 
The calibration data is stored in the non volatile storage (NVS) of the Esp32 so calibration has to be performed only once.
The program detects automatically if calibration data is available.


## LVGL Tips

### Examples from the LVGL 8.3 Documentation

The [Documentation for LVGL 8.3](https://docs.lvgl.io/8.3/examples.html) contains Micropython examples for most widgets which are missing in other versions of the documentation.

### Font Converter for custom fonts

The prebuild firmwares only contain the `lv.font_montserrat_14` and `lv.font_montserrat_16` fonts.
Use the [font converter](https://lvgl.io/tools/fontconverter) to compile custom fonts for LVGL. 
The image shows the settings used to compile fonts and load them in the demo script (click to enlarge).


I have tested several fonts and [Lexend](https://fonts.google.com/specimen/Lexend) is one of my favourites.
It's clearly readable on the CYD with medium or semi-bold font-weight.
It's provided under the Open Font License.


<img src="doc/Font_Converter_Settings.jpg" width="250" height="auto" />



## CYD2 and MicroPython

### Drivers and Firmware

The standard release of ESP32 MPY-Firmware can be installed on the CYD-2 as described [here](https://github.com/witnessmenow/ESP32-Cheap-Yellow-Display/blob/main/Examples/Micropython/Micropython.md).
The ILI9341 driver and the xpt2046 driver can be found in the `/demo_no_lvgl` folder. 

### Color Mode for CYD2

During display initialization in pure Micropython, bgr-mode needs to be disabled:
```python
Display(self.spi_display, dc=Pin(2), cs=Pin(15), rst=Pin(15), width = 320, height = 240, bgr = False)
```

Another solution can be disabling gamma-correction by passing `gamma = False` during Display initialization (see [#2](https://github.com/de-dh/ESP32-Cheap-Yellow-Display-Micropython-LVGL/issues/2#issuecomment-2558521839) )

### Demo program

A working demo and the drivers can be found in the `/demo_no_lvgl` folder. 
Draw functions can be used and touch actions can be assigned to multiple areas on screen in the demo program.

<img src="doc/CYD_MPY_Only.jpg" width="300" height="auto" />


## Links

CYD links:

- [Micropython example for the CYD](https://github.com/witnessmenow/ESP32-Cheap-Yellow-Display/blob/main/Examples/Micropython/Micropython.md): Large repositry about the CYD mainly with `C` examples.
- [Modifiying the CYD's hardware](https://github.com/hexeguitar/ESP32_TFT_PIO): Adding PSRAM, freeing GPIO pins, attaching a speaker.
- [Overview of the different CYD versions](https://github.com/rzeldent/platformio-espressif32-sunton): Overview of different CYD boards and board definitions for PlatformIO.

LVGL / Micropython links:

- [LVGL](https://github.com/rzeldent/platformio-espressif32-sunton): LVGL main repositry.
- [Micropython](https://github.com/micropython/micropython): Micropython main repositry.
- [LVGL Forum](https://forum.lvgl.io/): You can find help at the LVGL forum. Has a micropython category.
- [Kdschlosser's Micropython Bindings](https://github.com/lvgl-micropython/lvgl_micropython): Micropython bindings from kdschlosser make building the firmware easier and support additional displays.
- [Stefan's Blog](https://stefan.box2code.de/2023/11/18/esp32-grafik-mit-lvgl-und-micropython/): German blog with instructions on how to use LVGL on the CYD. Also contains prebuild firmware for LVGL 8.3.
- [Documentation for LVGL 8.3](https://docs.lvgl.io/8.3/examples.html): Documentation for LVGL 8.3 with Micropython examples.
- [LVGL Font Converter](https://lvgl.io/tools/fontconverter): Online font converter for LVGL.
