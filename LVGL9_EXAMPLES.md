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
| lvgl_custom_font_example.py | Loading a custom font compiled by the LVGL font converter. Font  license: [SIL](#licenses). |
| lvgl_custom_icon_font_example.py | Loading a custom icon font. [Described here](LVGL9_TIPS.md#icon-fonts). |
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



## Licenses

The files `/lvgl9_examples/assets/oxanium_m_16.bin` and `/lvgl9_examples/assets/oxanium_m_40.bin` used in `/lvgl9_examples/lvgl_custom_font_example.py` were compiled from [Google Fonts - Oxanium](https://fonts.google.com/specimen/Oxanium?preview.script=Latn) using the LVGL font converter. The Oxanium font is provided under the SIL OPEN FONT LICENSE Version 1.1 as described below.

Copyright 2019 The Oxanium Project Authors (https://github.com/sevmeyer/oxanium)

This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is copied below, and is also available with a FAQ at:
https://scripts.sil.org/OFL


**SIL OPEN FONT LICENSE Version 1.1 - 26 February 2007**


PREAMBLE
The goals of the Open Font License (OFL) are to stimulate worldwide
development of collaborative font projects, to support the font creation
efforts of academic and linguistic communities, and to provide a free and
open framework in which fonts may be shared and improved in partnership
with others.

The OFL allows the licensed fonts to be used, studied, modified and
redistributed freely as long as they are not sold by themselves. The
fonts, including any derivative works, can be bundled, embedded,
redistributed and/or sold with any software provided that any reserved
names are not used by derivative works. The fonts and derivatives,
however, cannot be released under any other type of license. The
requirement for fonts to remain under this license does not apply
to any document created using the fonts or their derivatives.

DEFINITIONS
"Font Software" refers to the set of files released by the Copyright
Holder(s) under this license and clearly marked as such. This may
include source files, build scripts and documentation.

"Reserved Font Name" refers to any names specified as such after the
copyright statement(s).

"Original Version" refers to the collection of Font Software components as
distributed by the Copyright Holder(s).

"Modified Version" refers to any derivative made by adding to, deleting,
or substituting -- in part or in whole -- any of the components of the
Original Version, by changing formats or by porting the Font Software to a
new environment.

"Author" refers to any designer, engineer, programmer, technical
writer or other person who contributed to the Font Software.

PERMISSION & CONDITIONS
Permission is hereby granted, free of charge, to any person obtaining
a copy of the Font Software, to use, study, copy, merge, embed, modify,
redistribute, and sell modified and unmodified copies of the Font
Software, subject to the following conditions:

1) Neither the Font Software nor any of its individual components,
in Original or Modified Versions, may be sold by itself.

2) Original or Modified Versions of the Font Software may be bundled,
redistributed and/or sold with any software, provided that each copy
contains the above copyright notice and this license. These can be
included either as stand-alone text files, human-readable headers or
in the appropriate machine-readable metadata fields within text or
binary files as long as those fields can be easily viewed by the user.

3) No Modified Version of the Font Software may use the Reserved Font
Name(s) unless explicit written permission is granted by the corresponding
Copyright Holder. This restriction only applies to the primary font name as
presented to the users.

4) The name(s) of the Copyright Holder(s) or the Author(s) of the Font
Software shall not be used to promote, endorse or advertise any
Modified Version, except to acknowledge the contribution(s) of the
Copyright Holder(s) and the Author(s) or with their explicit written
permission.

5) The Font Software, modified or unmodified, in part or in whole,
must be distributed entirely under this license, and must not be
distributed under any other license. The requirement for fonts to
remain under this license does not apply to any document created
using the Font Software.

TERMINATION
This license becomes null and void if any of the above conditions are
not met.

DISCLAIMER
THE FONT SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT
OF COPYRIGHT, PATENT, TRADEMARK, OR OTHER RIGHT. IN NO EVENT SHALL THE
COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
INCLUDING ANY GENERAL, SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL
DAMAGES, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF THE USE OR INABILITY TO USE THE FONT SOFTWARE OR FROM
OTHER DEALINGS IN THE FONT SOFTWARE.
