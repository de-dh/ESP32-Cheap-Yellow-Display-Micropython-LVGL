import lvgl as lv
import lv_config

# ===== Custom Fonts ===== #
import fs_driver

fs_drive_letter = 'S'
fs_font_driver = lv.fs_drv_t()
fs_driver.fs_register(fs_font_driver, fs_drive_letter)

font_oxanium_m_16 = lv.binfont_create(f'{fs_drive_letter}:assets/oxanium_m_16.bin')
font_oxanium_m_40 = lv.binfont_create(f'{fs_drive_letter}:assets/oxanium_m_40.bin')

ui_Screen1 = lv.obj()
ui_Screen1.remove_flag(lv.obj.FLAG.SCROLLABLE)
ui_Screen1.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Screen1.set_style_bg_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )

ui_Label = lv.label(ui_Screen1)
ui_Label.set_text(f'Custom Font: Oxanium')
ui_Label.set_width(lv.SIZE_CONTENT)
ui_Label.set_height(lv.SIZE_CONTENT)
ui_Label.align( lv.ALIGN.TOP_MID, 0, 15)

ui_Label2 = lv.label(ui_Screen1)
ui_Label2.align( lv.ALIGN.TOP_MID, 0, 50)
ui_Label2.set_style_text_font(font_oxanium_m_16, 0)
ui_Label2.set_style_text_color(lv.color_white(), 0)
ui_Label2.set_text('Oxanium 16 pt')

ui_Label3 = lv.label(ui_Screen1)
ui_Label3.align( lv.ALIGN.TOP_MID, 0, 80)
ui_Label3.set_style_text_font(font_oxanium_m_40, 0)
ui_Label3.set_style_text_color(lv.color_white(), 0)
ui_Label3.set_text('Oxanium 40 pt')

lv.screen_load(ui_Screen1)