import lvgl as lv
import lv_config

def SetFlag(obj, flag, value):
    if value:
        obj.add_flag(flag)
    else:
        obj.remove_flag(flag)

def StepSpinbox(trg, val):
    if val == 1:
        trg.increment()
    if val == -1:
        trg.decrement()
    trg.send_event(lv.EVENT.VALUE_CHANGED, None)

def Button1_eventhandler(event_struct):
   event = event_struct.get_code()
   if event == lv.EVENT.CLICKED and True:
      lv.screen_load(ui_Screen2)

ui_Screen1 = lv.obj()
SetFlag(ui_Screen1, lv.obj.FLAG.SCROLLABLE, False)
ui_Screen1.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_Screen1.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

ui_Container1 = lv.obj(ui_Screen1)
ui_Container1.remove_style_all()
ui_Container1.set_height(30)
ui_Container1.set_width(lv.pct(100))
SetFlag(ui_Container1, lv.obj.FLAG.CLICKABLE, False)
SetFlag(ui_Container1, lv.obj.FLAG.SCROLLABLE, False)
ui_Container1.set_style_bg_color(lv.color_hex(0x282828), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_Container1.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

ui_Label3 = lv.label(ui_Container1)
ui_Label3.set_text("SCREEN 1")
ui_Label3.set_width(lv.SIZE_CONTENT)
ui_Label3.set_height(lv.SIZE_CONTENT)
ui_Label3.set_align(lv.ALIGN.CENTER)

ui_Container2 = lv.obj(ui_Screen1)
ui_Container2.remove_style_all()
ui_Container2.set_width(300)
ui_Container2.set_height(190)
ui_Container2.set_x(10)
ui_Container2.set_y(40)
SetFlag(ui_Container2, lv.obj.FLAG.CLICKABLE, False)
SetFlag(ui_Container2, lv.obj.FLAG.SCROLLABLE, False)
ui_Container2.set_style_bg_color(lv.color_hex(0x282828), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_Container2.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

ui_Button1 = lv.button(ui_Container2)
ui_Button1.set_width(98)
ui_Button1.set_height(55)
ui_Button1.set_x(-10)
ui_Button1.set_y(-10)
ui_Button1.set_align(lv.ALIGN.BOTTOM_RIGHT)
SetFlag(ui_Button1, lv.obj.FLAG.SCROLLABLE, False)
SetFlag(ui_Button1, lv.obj.FLAG.SCROLL_ON_FOCUS, True)

ui_Label1 = lv.label(ui_Button1)
ui_Label1.set_text("NEXT")
ui_Label1.set_width(lv.SIZE_CONTENT)
ui_Label1.set_height(lv.SIZE_CONTENT)
ui_Label1.set_align(lv.ALIGN.CENTER)

ui_Button1.add_event_cb(Button1_eventhandler, lv.EVENT.ALL, None)

ui_Button2 = lv.button(ui_Container2)
ui_Button2.set_width(98)
ui_Button2.set_height(55)
ui_Button2.set_x(10)
ui_Button2.set_y(-10)
ui_Button2.set_align(lv.ALIGN.BOTTOM_LEFT)
SetFlag(ui_Button2, lv.obj.FLAG.SCROLLABLE, False)
SetFlag(ui_Button2, lv.obj.FLAG.SCROLL_ON_FOCUS, True)
ui_Button2.add_state(lv.STATE.CHECKED * False | lv.STATE.PRESSED * False | lv.STATE.FOCUSED * False | lv.STATE.DISABLED * True | lv.STATE.EDITED * False | lv.STATE.USER_1 * False | lv.STATE.USER_2 * False | lv.STATE.USER_3 * False | lv.STATE.USER_4 * False)
ui_Button2.remove_state(lv.STATE.CHECKED * (not False) | lv.STATE.PRESSED * (not False) | lv.STATE.FOCUSED * (not False) | lv.STATE.DISABLED * (not True) | lv.STATE.EDITED * (not False) | lv.STATE.USER_1 * (not False) | lv.STATE.USER_2 * (not False) | lv.STATE.USER_3 * (not False) | lv.STATE.USER_4 * (not False))
ui_Button2.set_style_bg_color(lv.color_hex(0x494949), lv.PART.MAIN | lv.STATE.DISABLED)
ui_Button2.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DISABLED)

ui_Label2 = lv.label(ui_Button2)
ui_Label2.set_text("BACK")
ui_Label2.set_width(lv.SIZE_CONTENT)
ui_Label2.set_height(lv.SIZE_CONTENT)
ui_Label2.set_align(lv.ALIGN.CENTER)

ui_Spinner1 = lv.spinner(ui_Container2)
ui_Spinner1.set_width(80)
ui_Spinner1.set_height(80)
ui_Spinner1.set_x(0)
ui_Spinner1.set_y(-30)
ui_Spinner1.set_align(lv.ALIGN.CENTER)
ui_Spinner1.set_style_arc_width(5, lv.PART.MAIN | lv.STATE.DEFAULT)
ui_Spinner1.set_style_arc_rounded(True, lv.PART.MAIN | lv.STATE.DEFAULT)
ui_Spinner1.set_style_arc_width(5, lv.PART.INDICATOR | lv.STATE.DEFAULT)
ui_Spinner1.set_style_arc_rounded(True, lv.PART.INDICATOR | lv.STATE.DEFAULT)

def Button3_eventhandler(event_struct):
   event = event_struct.get_code()
   if event == lv.EVENT.CLICKED and True:
      lv.screen_load(ui_Screen3)

def Button4_eventhandler(event_struct):
   event = event_struct.get_code()
   if event == lv.EVENT.CLICKED and True:
      lv.screen_load(ui_Screen1)

ui_Screen2 = lv.obj()
SetFlag(ui_Screen2, lv.obj.FLAG.SCROLLABLE, False)
ui_Screen2.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_Screen2.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

ui_Container3 = lv.obj(ui_Screen2)
ui_Container3.remove_style_all()
ui_Container3.set_height(30)
ui_Container3.set_width(lv.pct(100))
SetFlag(ui_Container3, lv.obj.FLAG.CLICKABLE, False)
SetFlag(ui_Container3, lv.obj.FLAG.SCROLLABLE, False)
ui_Container3.set_style_bg_color(lv.color_hex(0x282828), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_Container3.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

ui_Label4 = lv.label(ui_Container3)
ui_Label4.set_text("SCREEN 2")
ui_Label4.set_width(lv.SIZE_CONTENT)
ui_Label4.set_height(lv.SIZE_CONTENT)
ui_Label4.set_align(lv.ALIGN.CENTER)

ui_Container4 = lv.obj(ui_Screen2)
ui_Container4.remove_style_all()
ui_Container4.set_width(300)
ui_Container4.set_height(190)
ui_Container4.set_x(10)
ui_Container4.set_y(40)
SetFlag(ui_Container4, lv.obj.FLAG.CLICKABLE, False)
SetFlag(ui_Container4, lv.obj.FLAG.SCROLLABLE, False)
ui_Container4.set_style_bg_color(lv.color_hex(0x282828), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_Container4.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

ui_Button3 = lv.button(ui_Container4)
ui_Button3.set_width(98)
ui_Button3.set_height(55)
ui_Button3.set_x(-10)
ui_Button3.set_y(-10)
ui_Button3.set_align(lv.ALIGN.BOTTOM_RIGHT)
SetFlag(ui_Button3, lv.obj.FLAG.SCROLLABLE, False)
SetFlag(ui_Button3, lv.obj.FLAG.SCROLL_ON_FOCUS, True)

ui_Label5 = lv.label(ui_Button3)
ui_Label5.set_text("NEXT")
ui_Label5.set_width(lv.SIZE_CONTENT)
ui_Label5.set_height(lv.SIZE_CONTENT)
ui_Label5.set_align(lv.ALIGN.CENTER)

ui_Button3.add_event_cb(Button3_eventhandler, lv.EVENT.ALL, None)

ui_Button4 = lv.button(ui_Container4)
ui_Button4.set_width(98)
ui_Button4.set_height(55)
ui_Button4.set_x(10)
ui_Button4.set_y(-10)
ui_Button4.set_align(lv.ALIGN.BOTTOM_LEFT)
SetFlag(ui_Button4, lv.obj.FLAG.SCROLLABLE, False)
SetFlag(ui_Button4, lv.obj.FLAG.SCROLL_ON_FOCUS, True)

ui_Label6 = lv.label(ui_Button4)
ui_Label6.set_text("BACK")
ui_Label6.set_width(lv.SIZE_CONTENT)
ui_Label6.set_height(lv.SIZE_CONTENT)
ui_Label6.set_align(lv.ALIGN.CENTER)

ui_Button4.add_event_cb(Button4_eventhandler, lv.EVENT.ALL, None)

ui_Dropdown1 = lv.dropdown(ui_Container4)
ui_Dropdown1.set_options("Option 1\nOption 2\nOption 3")
ui_Dropdown1.set_text("Make a choice!" if len("Make a choice!") > 0 else None)
ui_Dropdown1.set_width(200)
ui_Dropdown1.set_height(lv.SIZE_CONTENT)
ui_Dropdown1.set_x(0)
ui_Dropdown1.set_y(20)
ui_Dropdown1.set_align(lv.ALIGN.TOP_MID)
SetFlag(ui_Dropdown1, lv.obj.FLAG.SCROLL_ON_FOCUS, True)

def Button6_eventhandler(event_struct):
   event = event_struct.get_code()
   if event == lv.EVENT.CLICKED and True:
      lv.screen_load(ui_Screen2)

def Button7_eventhandler(event_struct):
   event = event_struct.get_code()
   if event == lv.EVENT.CLICKED and True:
      StepSpinbox(ui_Spinbox1, 1)

def Button8_eventhandler(event_struct):
   event = event_struct.get_code()
   if event == lv.EVENT.CLICKED and True:
      StepSpinbox(ui_Spinbox1, -1)

ui_Screen3 = lv.obj()
SetFlag(ui_Screen3, lv.obj.FLAG.SCROLLABLE, False)
ui_Screen3.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_Screen3.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

ui_Container6 = lv.obj(ui_Screen3)
ui_Container6.remove_style_all()
ui_Container6.set_height(30)
ui_Container6.set_width(lv.pct(100))
SetFlag(ui_Container6, lv.obj.FLAG.CLICKABLE, False)
SetFlag(ui_Container6, lv.obj.FLAG.SCROLLABLE, False)
ui_Container6.set_style_bg_color(lv.color_hex(0x282828), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_Container6.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

ui_Label8 = lv.label(ui_Container6)
ui_Label8.set_text("SCREEN 3")
ui_Label8.set_width(lv.SIZE_CONTENT)
ui_Label8.set_height(lv.SIZE_CONTENT)
ui_Label8.set_align(lv.ALIGN.CENTER)

ui_Container7 = lv.obj(ui_Screen3)
ui_Container7.remove_style_all()
ui_Container7.set_width(300)
ui_Container7.set_height(190)
ui_Container7.set_x(10)
ui_Container7.set_y(40)
SetFlag(ui_Container7, lv.obj.FLAG.CLICKABLE, False)
SetFlag(ui_Container7, lv.obj.FLAG.SCROLLABLE, False)
ui_Container7.set_style_bg_color(lv.color_hex(0x282828), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_Container7.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

ui_Button5 = lv.button(ui_Container7)
ui_Button5.set_width(98)
ui_Button5.set_height(55)
ui_Button5.set_x(-10)
ui_Button5.set_y(-10)
ui_Button5.set_align(lv.ALIGN.BOTTOM_RIGHT)
SetFlag(ui_Button5, lv.obj.FLAG.SCROLLABLE, False)
SetFlag(ui_Button5, lv.obj.FLAG.SCROLL_ON_FOCUS, True)
ui_Button5.add_state(lv.STATE.CHECKED * False | lv.STATE.PRESSED * False | lv.STATE.FOCUSED * False | lv.STATE.DISABLED * True | lv.STATE.EDITED * False | lv.STATE.USER_1 * False | lv.STATE.USER_2 * False | lv.STATE.USER_3 * False | lv.STATE.USER_4 * False)
ui_Button5.remove_state(lv.STATE.CHECKED * (not False) | lv.STATE.PRESSED * (not False) | lv.STATE.FOCUSED * (not False) | lv.STATE.DISABLED * (not True) | lv.STATE.EDITED * (not False) | lv.STATE.USER_1 * (not False) | lv.STATE.USER_2 * (not False) | lv.STATE.USER_3 * (not False) | lv.STATE.USER_4 * (not False))
ui_Button5.set_style_bg_color(lv.color_hex(0x494949), lv.PART.MAIN | lv.STATE.DISABLED)
ui_Button5.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DISABLED)

ui_Label9 = lv.label(ui_Button5)
ui_Label9.set_text("NEXT")
ui_Label9.set_width(lv.SIZE_CONTENT)
ui_Label9.set_height(lv.SIZE_CONTENT)
ui_Label9.set_align(lv.ALIGN.CENTER)

ui_Button6 = lv.button(ui_Container7)
ui_Button6.set_width(98)
ui_Button6.set_height(55)
ui_Button6.set_x(10)
ui_Button6.set_y(-10)
ui_Button6.set_align(lv.ALIGN.BOTTOM_LEFT)
SetFlag(ui_Button6, lv.obj.FLAG.SCROLLABLE, False)
SetFlag(ui_Button6, lv.obj.FLAG.SCROLL_ON_FOCUS, True)

ui_Label10 = lv.label(ui_Button6)
ui_Label10.set_text("BACK")
ui_Label10.set_width(lv.SIZE_CONTENT)
ui_Label10.set_height(lv.SIZE_CONTENT)
ui_Label10.set_align(lv.ALIGN.CENTER)

ui_Button6.add_event_cb(Button6_eventhandler, lv.EVENT.ALL, None)

ui_Spinbox1 = lv.spinbox(ui_Container7)
ui_Spinbox1.set_width(85)
ui_Spinbox1.set_height(42)
ui_Spinbox1.set_x(110)
ui_Spinbox1.set_y(36)
ui_Spinbox1.set_digit_format(4, 2)
ui_Spinbox1.set_range(0, 9999)
ui_Spinbox1.set_step(10 ** (1 - 1))
ui_Spinbox1.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN | lv.STATE.DEFAULT)
ui_Spinbox1.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN | lv.STATE.DEFAULT)

ui_Button7 = lv.button(ui_Container7)
ui_Button7.set_width(57)
ui_Button7.set_height(43)
ui_Button7.set_x(208)
ui_Button7.set_y(35)
SetFlag(ui_Button7, lv.obj.FLAG.SCROLLABLE, False)
SetFlag(ui_Button7, lv.obj.FLAG.SCROLL_ON_FOCUS, True)

ui_Label11 = lv.label(ui_Button7)
ui_Label11.set_text(">")
ui_Label11.set_width(lv.SIZE_CONTENT)
ui_Label11.set_height(lv.SIZE_CONTENT)
ui_Label11.set_align(lv.ALIGN.CENTER)

ui_Button7.add_event_cb(Button7_eventhandler, lv.EVENT.ALL, None)

ui_Button8 = lv.button(ui_Container7)
ui_Button8.set_width(57)
ui_Button8.set_height(43)
ui_Button8.set_x(36)
ui_Button8.set_y(33)
SetFlag(ui_Button8, lv.obj.FLAG.SCROLLABLE, False)
SetFlag(ui_Button8, lv.obj.FLAG.SCROLL_ON_FOCUS, True)

ui_Label12 = lv.label(ui_Button8)
ui_Label12.set_text("<")
ui_Label12.set_width(lv.SIZE_CONTENT)
ui_Label12.set_height(lv.SIZE_CONTENT)
ui_Label12.set_align(lv.ALIGN.CENTER)

ui_Button8.add_event_cb(Button8_eventhandler, lv.EVENT.ALL, None)

lv.screen_load(ui_Screen1)