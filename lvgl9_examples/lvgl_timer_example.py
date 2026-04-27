import lvgl as lv
import lv_config

def SetFlag( obj, flag, value):
    if (value):
        obj.add_flag(flag)
    else:
        obj.remove_flag(flag)
    return

cnt = 0
def update_time(t):
    global cnt
    cnt += 1
    ui_Label1.set_text(f"Value:\n{cnt}")
    ui_Label1.invalidate()

timer = lv.timer_create(update_time, 250, None)
timer.set_repeat_count(-1)
timer.pause()
#timer.reset()
#timer.resume()    


ui_Screen1 = lv.obj()
SetFlag(ui_Screen1, lv.obj.FLAG.SCROLLABLE, False)
ui_Screen1.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Screen1.set_style_bg_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )

ui_Panel3 = lv.obj(ui_Screen1)
ui_Panel3.set_width(110)
ui_Panel3.set_height(110)
ui_Panel3.align( lv.ALIGN.TOP_MID, 0, 35)
SetFlag(ui_Panel3, lv.obj.FLAG.SCROLLABLE, False)
ui_Panel3.set_style_radius( 999, lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Panel3.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Panel3.set_style_bg_opa(0, lv.PART.MAIN| lv.STATE.DEFAULT )
ui_Panel3.set_style_border_color(lv.color_hex(0x006FFF), lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Panel3.set_style_border_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )
ui_Panel3.set_style_border_width( 2, lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Panel3.set_style_border_side( lv.BORDER_SIDE.FULL, lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Panel3.set_style_text_font( lv.font_montserrat_16, lv.PART.MAIN | lv.STATE.DEFAULT )

ui_Label1 = lv.label(ui_Panel3)
ui_Label1.set_text("Value:\n0")
ui_Label1.set_width(lv.SIZE_CONTENT)
ui_Label1.set_height(lv.SIZE_CONTENT)
ui_Label1.set_align( lv.ALIGN.CENTER)
ui_Label1.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN | lv.STATE.DEFAULT)

ui_Container1 = lv.obj(ui_Screen1)
ui_Container1.remove_style_all()
ui_Container1.set_width(310)
ui_Container1.set_height(75)
ui_Container1.set_x(0)
ui_Container1.set_y(-5)
ui_Container1.set_align( lv.ALIGN.BOTTOM_MID)
ui_Container1.set_flex_flow(lv.FLEX_FLOW.ROW)
ui_Container1.set_flex_align(lv.FLEX_ALIGN.SPACE_EVENLY, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)
SetFlag(ui_Container1, lv.obj.FLAG.CLICKABLE, False)
SetFlag(ui_Container1, lv.obj.FLAG.SCROLLABLE, False)
ui_Container1.set_style_pad_row( 20, lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Container1.set_style_pad_column( 0, lv.PART.MAIN | lv.STATE.DEFAULT )

ui_Button1 = lv.button(ui_Container1)
ui_Button1.set_width(120)
ui_Button1.set_height(70)
ui_Button1.set_align( lv.ALIGN.CENTER)
SetFlag(ui_Button1, lv.obj.FLAG.SCROLLABLE, False)
SetFlag(ui_Button1, lv.obj.FLAG.SCROLL_ON_FOCUS, True)
ui_Button1.set_style_text_font( lv.font_montserrat_16, lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Button1.add_event_cb(lambda e: timer.resume(), lv.EVENT.CLICKED, None)

ui_Label2 = lv.label(ui_Button1)
ui_Label2.set_text(lv.SYMBOL.PLAY + "  START")
ui_Label2.set_width(lv.SIZE_CONTENT)
ui_Label2.set_height(lv.SIZE_CONTENT)
ui_Label2.set_align( lv.ALIGN.CENTER)

ui_Button2 = lv.button(ui_Container1)
ui_Button2.set_width(120)
ui_Button2.set_height(70)
ui_Button2.set_align( lv.ALIGN.CENTER)
SetFlag(ui_Button2, lv.obj.FLAG.SCROLLABLE, False)
SetFlag(ui_Button2, lv.obj.FLAG.SCROLL_ON_FOCUS, True)
ui_Button2.set_style_text_font( lv.font_montserrat_16, lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Button2.add_event_cb(lambda e: timer.pause(), lv.EVENT.CLICKED, None)

ui_Label3 = lv.label(ui_Button2)
ui_Label3.set_text(lv.SYMBOL.STOP + "  STOP")
ui_Label3.set_width(lv.SIZE_CONTENT)
ui_Label3.set_height(lv.SIZE_CONTENT)
ui_Label3.set_align( lv.ALIGN.CENTER)

ui_Label5 = lv.label(ui_Screen1)
ui_Label5.set_text("TIMER TEST")
ui_Label5.set_width(lv.SIZE_CONTENT)
ui_Label5.set_height(lv.SIZE_CONTENT)
ui_Label5.set_x(0)
ui_Label5.set_y(5)
ui_Label5.set_align( lv.ALIGN.TOP_MID)
ui_Label5.set_style_text_font( lv.font_montserrat_16, lv.PART.MAIN | lv.STATE.DEFAULT )

lv.screen_load(ui_Screen1)