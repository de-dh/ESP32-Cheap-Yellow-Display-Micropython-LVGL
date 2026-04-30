# LVGL9.4 Example Programs

## Setup
Open the file `/lvgl9_examples/lib/lv_config.py` and copy the correct display settings from `/lvgl9_firmwares/color_test.py` to it.

Upload the `/lvgl9_examples` folder to your board and run the example programms and it will use a lot of storage.

You don't need to upload the `/lvgl9_examples/example_screenshots` folder since the screenshots are only used in the documentation.

| Folder Name  | Description |
| ------------- | ------------- |
| `/lvgl9_examples`  | Contains the LVGL9 example programs. |
| `/lvgl9_examples/lib`  | Contains LVGL9 includes like `lv_config.py` which contains the display setup. |
| `/lvgl9_examples/assets`  | Contains additional files needed for the demo programs, e.g. font files and images. |
| `/lvgl9_examples/example_screenshots`  | Screenshots of the example programs. The screenshots demonstrate how the demos are supposed to be displayed. Don't upload to MCU.|


## Example Programms
| File in `/lvgl9_examples` | Description |
|---|---|
| lvgl_async_example.py | Using asyncio to update the screen. |
| lvgl_custom_font_example.py | Loading a custom font compiled by the font-compiler. |
| lvgl_custom_icon_font_example.py | Loading a custom icon font. The icon font was created using IcoMoon and converted using the font-compiler. |
| lvgl_flex_example.py | Flexbox layout with fixed items of fixed and variable width demonstrating flex-grow.|
| lvgl_icons_example.py | Using the font-awesome icons included in the LVGL build by default. |
| lvgl_image_example.py | Loading a .png image directly from the flash storage of the CYD. |
| lvgl_imagebutton_example.py | Demonstrates the image button widget. |
| lvgl_keyboard_example.py | Custom keyboard layout.|
| lvgl_multiscreen_example.py | Creating and navigating through multiple screens. |
| lvgl_palette_example.py | LVGL build-in color palette example with shades. |
| lvgl_palette_example_simple.py | LVGL build-in color palette example. |
| lvgl_python_classes_example.py | OOP example demonstrating how to create screens and styles from custom classes. |
| lvgl_timer_example.py |Using the LVGL timer module. |
