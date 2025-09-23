## LVGL8 - Deprecated Documentation and Examples

The old [LVGL8 documentation and examples](LVGL8.md) can be found here.
It is not maintaines and the programms are incompatible with LVGL9.

## LVGL9 Firmware
The `lvgl9_firmware` folder contains a prebuilt firmware (with flash instructions and a test program) using LVGL 9.3 and MicroPython 1.25.0 compiled from [Kdschlosser's Micropython Bindings](https://github.com/lvgl-micropython/lvgl_micropython) for the Cheap Yellow Display (CYD). It was compiled from commit 
[15a414b](https://github.com/lvgl-micropython/lvgl_micropython/commit/15a414bc03486017235234882ce7415532c6325e) since the current version has a bug which puts the CYD in a boot loop. The firmware includes the touch fix kdschlosser/lvgl_micropython#454 for correct touch calibration.


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

### Demo Programm

A working demo and the drivers can be found in the `/demo_no_lvgl` folder. 
Draw functions can be used and touch actions can be assigned to multiple areas on screen in the demo programm.

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
