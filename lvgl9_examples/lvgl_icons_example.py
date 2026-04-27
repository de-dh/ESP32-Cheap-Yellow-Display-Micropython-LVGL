import lvgl as lv
import lv_config

ui_Screen1 = lv.obj()
ui_Screen1.remove_flag(lv.obj.FLAG.SCROLLABLE)
ui_Screen1.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Screen1.set_style_bg_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )

symbols = [s for s in dir(lv.SYMBOL) if not s.startswith('_')]
print(f'Included Icons in lv.SYMBOL:')
print(symbols)

ui_Label = lv.label(ui_Screen1)
ui_Label.set_text(f'NUMBER OF ICONS: {len(symbols)}')
ui_Label.set_width(lv.SIZE_CONTENT)
ui_Label.set_height(lv.SIZE_CONTENT)
ui_Label.align( lv.ALIGN.TOP_MID, 0, 15)

ui_Label2 = lv.label(ui_Screen1)
ui_Label2.set_width(250)
ui_Label2.set_height(lv.SIZE_CONTENT)
ui_Label2.align( lv.ALIGN.TOP_MID, 0, 50)
ui_Label2.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN | lv.STATE.DEFAULT)
ui_Label2.set_style_text_font(lv.font_montserrat_16, 0)
ui_Label2.set_style_text_line_space(3, 0)

t = ''
for i, s in enumerate(symbols): 
    t += getattr(lv.SYMBOL, s, 'X') + ' '

ui_Label2.set_text(t)

button = lv.button(ui_Screen1)
button.set_height(55)
button.set_width(140)
button.align(lv.ALIGN.BOTTOM_MID, 0, -15)
button.set_style_text_font(lv.font_montserrat_16, 0)

button_label = lv.label(button)
button_label.set_text(lv.SYMBOL.OK + '  ICON BTN')
button_label.set_width(lv.SIZE_CONTENT)
button_label.set_height(lv.SIZE_CONTENT)
button_label.set_align(lv.ALIGN.CENTER)

lv.screen_load(ui_Screen1)