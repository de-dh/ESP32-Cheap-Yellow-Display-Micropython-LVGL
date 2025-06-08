WIP!


# Cheap-Yellow-Display Micropython LVGL Guide and Examples

## Introduction
CYDs


## Display And Touch Screen Driver Setup
Although CYDs from different vendors look almost identical, they may require varying display and touch screen initialization setups.
The main differences are
- MADCTL configuration (display roration and mirroring) / Display Orientation Table
- Color modes: RGB vs. BGR
- Touch screen calibration: mirroring the x/y-axis or swapping the axes may be neccessary.

The correct configuration for a specific display can only be found by trial and error.

[https://github.com/lvgl-micropython/lvgl_micropython/discussions/281](https://github.com/lvgl-micropython/lvgl_micropython/discussions/281)

## LVGL9
I compiled a firmware for the CYD using lvgl9.
I also uploaded a test program which might help to find the correct display orientation, colormode and touchscreen settings.

## LVGL8
Firmware
Examples

## No LVGL
Examples
