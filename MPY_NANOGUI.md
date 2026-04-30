# CYD Nanogui Setup

## Setup

The `/mpy_nanogui` folder contains the complete setup for [Peter Hinch's nanogui](https://github.com/peterhinch/micropython-nano-gui). Only the neccessary display drivers are included.
The screenshot shows how the displayed screen should look after a successfull setup.

<img  src="mpy_nanogui/snapshot_nanogui.png" width="240" height="auto" />

1. Upload content of the `/mpy_nanogui` folder (except for the `/font_to_py_multiconverter` folder) to your CYD.
2. Run `main.py`.
3. Edit settings in `color_setup.py` if neccessary. Find the correct settings for `default_mod` and `default_bgr` by trial and error.

**`color_setup.py`**
```python
default_mod = 4 # orientation: 0 - 7
default_bgr = True # rgb / bgr mode
```

## font_to_py_multiconverter

The `font_to_py_multiconverter` is used to convert a `*.ttf` file to `*.py` font files which can be used by nanogui's (C)Writer module.
Simply drag-and-drop a *.ttf file onto `multi_converter.bat` and a new subfolder will be created containing compiled `*.py` font files in multiple sizes.
