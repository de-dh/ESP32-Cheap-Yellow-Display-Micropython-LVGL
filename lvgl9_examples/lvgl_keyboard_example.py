import lvgl as lv
import lv_config


# Callback function of the keyboard.
def kb_event_cb(e):
    code = e.get_code()
    target = e.get_current_target_obj()
    ta = ui_ta_money
    
    if code == lv.EVENT.VALUE_CHANGED:
        ui_kb_money.set_textarea(ta)
        if not ta.has_state(lv.STATE.FOCUSED):
            ta.add_state(lv.STATE.FOCUSED)

    elif code == lv.EVENT.READY:
        print('Ready, current text: ' + ta.get_text())
    
    elif code == lv.EVENT.CANCEL:
        print('Cancelled')


# ===== LVGL UI Start ===== #

scr = lv.screen_active()
scr.set_style_bg_color(lv.color_black(), 0)


# ----- Textarea: Enter amount of money spent ----- #
# Accept only numbers and decimal point
ui_ta_money = lv.textarea(scr)
ui_ta_money.set_accepted_chars('0123456789.')
ui_ta_money.set_width(140)
ui_ta_money.set_max_length(7)
ui_ta_money.set_placeholder_text('0000.00')
ui_ta_money.set_one_line(True)
ui_ta_money.align( lv.ALIGN.TOP_MID, 0, 30)
ui_ta_money.add_state(lv.STATE.FOCUSED)
ui_ta_money.set_style_text_font(lv.font_montserrat_16, 0)


# ----- Keyboard: Control the input of the TA ----- #
btn_map = ['1', '2', '3', lv.SYMBOL.CLOSE, '\n',
            '4', '5', '6', lv.SYMBOL.BACKSPACE, '\n',
            '7', '8', '9', lv.SYMBOL.OK, '\n',
            lv.SYMBOL.LEFT, '0', lv.SYMBOL.RIGHT, '.', '']

ctrl_map = [1, 1, 1, 1,
            1, 1, 1, 1,
            1, 1, 1, 1,
            1, 1, 1, 1]

ui_kb_money = lv.keyboard(scr)
ui_kb_money.set_map(ui_kb_money.MODE.USER_1, btn_map, ctrl_map)
ui_kb_money.set_width(lv.pct(100))
ui_kb_money.set_height(160)
ui_kb_money.set_align( lv.ALIGN.BOTTOM_MID)
ui_kb_money.set_mode(ui_kb_money.MODE.USER_1)
ui_kb_money.set_style_text_font(lv.font_montserrat_16, 0)
ui_kb_money.set_textarea(ui_ta_money)
ui_kb_money.add_event_cb(kb_event_cb, lv.EVENT.ALL, None)

# ----- Label: Caption for TA ----- #
ui_label_ta = lv.label(scr)
ui_label_ta.set_text('Enter Amount')
ui_label_ta.align_to(ui_ta_money, lv.ALIGN.OUT_TOP_MID, -7, -7)
ui_label_ta.set_style_text_font(lv.font_montserrat_16, 0)

# ----- Label: Euro sign at the end of the TA ----- #
ui_label_ta_euro = lv.label(scr)
ui_label_ta_euro.set_text('Euro')
ui_label_ta_euro.align_to(ui_ta_money, lv.ALIGN.OUT_RIGHT_MID, 5, -5)
ui_label_ta_euro.set_style_text_font(lv.font_montserrat_16, 0)