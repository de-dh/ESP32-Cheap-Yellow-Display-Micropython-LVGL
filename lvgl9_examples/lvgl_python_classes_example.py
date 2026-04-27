import lvgl as lv
import lv_config
import time

class StyleBorder(lv.style_t):
    def __init__(self, border_color = lv.color_black()):
        super().__init__()
        self.set_clip_corner(True)
        self.set_border_post(True)
        self.set_border_side(lv.BORDER_SIDE.FULL)
        self.set_border_color(border_color)
        self.set_border_opa(255)
        self.set_border_width(3)
        
        self.set_text_color(lv.color_white())
        self.set_text_font(lv.font_montserrat_16)


class Screen1(lv.obj):
    def __init__(self):
        super().__init__()
        
        self.remove_flag(lv.obj.FLAG.SCROLLABLE)
        self.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT )
        self.set_style_bg_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )
        
        self.ui_box = lv.obj(self)
        self.ui_box.set_size(250, 100)
        self.ui_box.set_align(lv.ALIGN.CENTER)
        self.ui_box.add_style(StyleBorder(border_color = lv.color_hex(0xFFFF00)), lv.PART.MAIN)
        
        self.ui_Label = lv.label(self.ui_box)
        self.ui_Label.set_text(f'First Screen!')
        self.ui_Label.center()


class Screen2(lv.obj):
    def __init__(self):
        super().__init__()
        
        self.remove_flag(lv.obj.FLAG.SCROLLABLE)
        self.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT )
        self.set_style_bg_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )
        
        self.ui_box = lv.obj(self)
        self.ui_box.set_size(250, 100)
        self.ui_box.set_align(lv.ALIGN.CENTER)
        self.ui_box.add_style(StyleBorder(border_color = lv.color_hex(0x00FFFF)), lv.PART.MAIN)
        
        self.ui_Label = lv.label(self.ui_box)
        self.ui_Label.set_text(f'Second Screen!')
        self.ui_Label.center()

lv.screen_load(Screen1())
time.sleep(3)
lv.screen_load(Screen2())