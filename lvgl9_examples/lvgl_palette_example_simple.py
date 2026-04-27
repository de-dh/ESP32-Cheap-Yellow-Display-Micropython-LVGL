import lvgl as lv
import lv_config

    
def SetFlag( obj, flag, value):
    if (value):
        obj.add_flag(flag)
    else:
        obj.remove_flag(flag)
    return
# ========== Start UI  ========== #

colors = [str(s) for s in dir(lv.PALETTE) if not s.startswith('_') and s not in ('NONE', 'LAST')]
print(colors)

ui_Color_Screen = lv.obj()
SetFlag(ui_Color_Screen, lv.obj.FLAG.SCROLLABLE, False)
ui_Color_Screen.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Color_Screen.set_style_bg_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )

ui_color_wrapper = lv.obj(ui_Color_Screen)
ui_color_wrapper.set_width(300)
ui_color_wrapper.set_height(230)
ui_color_wrapper.set_x(0)
ui_color_wrapper.set_y(5)
ui_color_wrapper.set_align( lv.ALIGN.TOP_MID)
ui_color_wrapper.set_flex_flow(lv.FLEX_FLOW.COLUMN)
ui_color_wrapper.set_flex_align(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)
ui_color_wrapper.set_style_pad_row(0, lv.PART.MAIN | lv.STATE.DEFAULT )
ui_color_wrapper.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT )

for i, c in enumerate(colors):
    ui_color_container = lv.obj(ui_color_wrapper)
    ui_color_container.remove_style_all()
    ui_color_container.set_height(20)
    ui_color_container.set_width(lv.pct(100))
    ui_color_container.set_align( lv.ALIGN.CENTER)
    SetFlag(ui_color_container, lv.obj.FLAG.CLICKABLE, False)
    SetFlag(ui_color_container, lv.obj.FLAG.SCROLLABLE, False)

    ui_color_name_label = lv.label(ui_color_container)
    ui_color_name_label.set_text(f"{i+1:02d} - {c}")
    ui_color_name_label.set_width(lv.SIZE_CONTENT)
    ui_color_name_label.set_height(lv.SIZE_CONTENT)
    

    ui_color_rect = lv.obj(ui_color_container)
    ui_color_rect.set_width(50)
    ui_color_rect.set_height(15)
    
    p =  lv.palette_main(getattr(lv.PALETTE, c, 'NONE'))

        
    ui_color_rect.align(lv.ALIGN.TOP_RIGHT, -10, 5)
    
    SetFlag(ui_color_rect, lv.obj.FLAG.SCROLLABLE, False)
    ui_color_rect.set_style_bg_color(p, lv.PART.MAIN | lv.STATE.DEFAULT )
    ui_color_rect.set_style_bg_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )
    ui_color_rect.set_style_radius(0, lv.PART.MAIN| lv.STATE.DEFAULT )

lv.screen_load(ui_Color_Screen)