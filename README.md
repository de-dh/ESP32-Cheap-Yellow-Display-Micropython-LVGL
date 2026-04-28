> [!WARNING]
> You must do hard-resets of your CYD after code changes. Soft resets may throw this error: `can't convert to module to int`.
>
> The demos / example programs from the different folders require individual firmwares. They may not be mixed up.
> 
> **>>>>> Please read the complete readme file and check the closed issues before asking for help / opening any new issues. <<<<<**


## Cheap Yellow Display

<img align="right"  src="img/CYD_application_example.jpg" width="250" height="auto" />

The family of Esp32-S2432028Rs or Cheap Yellow Displays (CYDs) comprises of various boards with similar hardware configuration most importantly including

- an Esp32- WROOM and
- an ILI9341 2.8' (320 x 240, RGB565) display with a xpt2046 resistive touch interface.

This makes the CYDs ideal candidates for the development of small GUI projects using LVGL and MicroPython.
This repositry documents three different approaches on how to use the CYDs Display and it's touchscreen.

| Approach | Folder | Firmware | Usecase | Description |
| :---: | :---: | :---: | :---: | --- |
| [MPY Only](MPY_ONLY.md) | [`/mpy_only`](/mpy_only) | Standard MPY Firmware | Very Limited | **Low-level touch** support.<br> Uses rdaggers ILI9431 driver. Only primitive draw functions from MPY's framebuffer module and the display driver available.  |
| [MPY + nanogui](MPY_NANOGUI.md) | [`/mpy_nanogui`](/mpy_nanogui) | Standard MPY Firmware | Simple UI / Data Display | **No touch** support.<br> Supports the creation and updates of simple widgets like Labels and simple diagrams. Custom fonts and mono images can be used easily. Good choice for simple UIs (e. g. displaying data) without touch input. |
| [MPY + LVGL9](LVGL9_SETUP.md) | [`/lvgl9_firmwares`](/lvgl9_firmwares) | Precompiled LVGL9 Firmware | Professional GUIs / User Interactions | **High-level touch** support.<br> Supports professionally looking GUIs with touch user input.<br> _Versions: LVGL 9.4 and Micropython 1.27.0._ |
| [MPY + LVGL9](LVGL9_SETUP.md) | [`/lvgl9_examples`](/lvgl9_examples) | LVGL9 Examples | LVGL9 Examples | Demonstrates various widgets and functionalities of LVGL9 on the CYD.|


The focus of this repositry is the setup of LVGL. LVGL enables the development of professionally looking GUIs which accept user input with reasonable effort. LVGL offers predefined widgets like labels, buttons, lists, textareas etc. All objects are styled using css-like style properties, e. g. text-color, background-color, shadow, padding. Objects can be aligned relative to each other and complex layouts can be designed using flexbox and grid like positioning. Even animations are supported.

The major drawback of LVGL is that it requires a custom MPY firmware build and setting up the cofiguration for a specific touch / display combination can be tricky. [Kdschlosser's Micropython Bindings](https://github.com/lvgl-micropython/lvgl_micropython) for MPY aims to make the compilation of the firmware as easy as possible. The bindings were used to compile the firmware for the CYD which is provided for download in this repositry.

An integrated Esp32S3 display module with more power is the [JC3248W535 aka Cheap Black Display (CBD)](https://github.com/de-dh/ESP32-JC3248W535-Micropython-LVGL/tree/main). It has onboard PSRAM which supports more complex LVGL programs.

## CYD Setup

The following links provide detailed instructions on how to setup the CYD.

- [LVGL9 Setup Instructions](LVGL9_SETUP.md)
- [MPY Nanogui Setup Inctructions](MPY_NANOGUI.md)
- [MPY Only Setup Inctructions](MPY_ONLY.md)


## Links

CYD links:

- [Micropython example for the CYD](https://github.com/witnessmenow/ESP32-Cheap-Yellow-Display/blob/main/Examples/Micropython/Micropython.md): Large repositry about the CYD mainly with `C` examples.
- [Modifiying the CYD's hardware](https://github.com/hexeguitar/ESP32_TFT_PIO): Adding PSRAM, freeing GPIO pins, attaching a speaker.
- [Overview of the different CYD versions](https://github.com/rzeldent/platformio-espressif32-sunton): Overview of different CYD boards and board definitions for PlatformIO.

LVGL / Micropython links:

- [Kdschlosser's Micropython Bindings](https://github.com/lvgl-micropython/lvgl_micropython): Micropython bindings from kdschlosser make building the firmware easier and support additional displays.
- [baxterbuilds](https://baxterbuilds.com/): Some very useful LVGL9 Micropython examples.
- [JC3248W535 aka Cheap Black Display (CBD)](https://github.com/de-dh/ESP32-JC3248W535-Micropython-LVGL/tree/main)
- [Micropython](https://github.com/micropython/micropython): Micropython main repositry.
- [LVGL Forum](https://forum.lvgl.io/): You can find help at the LVGL forum. Has a micropython category.
- [Stefan's Blog (LVGL8!)](https://stefan.box2code.de/2023/11/18/esp32-grafik-mit-lvgl-und-micropython/): German blog with instructions on how to use LVGL on the CYD. Also contains prebuild firmware for LVGL 8.3.
- [Documentation for LVGL 8.3](https://docs.lvgl.io/8.3/examples.html): Documentation for LVGL 8.3 with Micropython examples.
- [LVGL Font Converter](https://lvgl.io/tools/fontconverter): Online font converter for LVGL.
