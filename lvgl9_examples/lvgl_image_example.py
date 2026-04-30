import lvgl as lv
import lv_config

# Source: https://github.com/lvgl-micropython/lvgl_micropython/discussions/317#discussioncomment-13230539

def get_image_data(filename):
    with open(filename, 'rb') as f:
        imgdata = f.read()

    return imgdata
    
def create_img_dsc(imgdata):
    imgdsc = lv.image_dsc_t({'data_size':len(imgdata), 'data':imgdata})
    return imgdsc
    

image_data = get_image_data('assets/hamster_round.png')
image_data_mv = memoryview(image_data)
img_dsc = create_img_dsc(image_data_mv)


ui_Screen1 = lv.obj()
ui_Screen1.remove_flag(lv.obj.FLAG.SCROLLABLE)
ui_Screen1.set_style_bg_color(lv.color_black(), lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Screen1.set_style_bg_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )

ui_Container8 = lv.obj(ui_Screen1)
ui_Container8.remove_style_all()
ui_Container8.set_width(280)
ui_Container8.set_height(100)
ui_Container8.set_x(1)
ui_Container8.set_y(-10)
ui_Container8.set_align( lv.ALIGN.CENTER)
ui_Container8.set_style_radius( 20, lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Container8.set_style_bg_color(lv.color_hex(0x282B30), lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Container8.set_style_bg_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )
ui_Container8.set_style_border_color(lv.color_hex(0x33373E), lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Container8.set_style_border_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )
ui_Container8.set_style_border_width( 2, lv.PART.MAIN | lv.STATE.DEFAULT )


image = lv.image(ui_Container8)
image.set_src(img_dsc)
image.set_x(10)
image.set_y(0)
image.set_align( lv.ALIGN.LEFT_MID)
image.add_flag(lv.obj.FLAG.CLICKABLE)
image.set_style_border_color(lv.color_hex3(0xDDD), lv.PART.MAIN | lv.STATE.DEFAULT )
image.set_style_border_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )
image.set_style_border_width(3, lv.PART.MAIN | lv.STATE.DEFAULT )
image.set_style_radius(lv.RADIUS_CIRCLE, lv.PART.MAIN | lv.STATE.DEFAULT )
image.set_style_clip_corner(True, lv.PART.MAIN | lv.STATE.DEFAULT )
image.set_style_border_post(True, lv.PART.MAIN | lv.STATE.DEFAULT )
# Recolor when pressed
image.set_style_image_recolor_opa(128, lv.PART.MAIN| lv.STATE.PRESSED)
image.set_style_image_recolor(lv.color_white(), lv.PART.MAIN| lv.STATE.PRESSED)

ui_Label7 = lv.label(ui_Container8)
ui_Label7.set_text("Golden Hamster")
ui_Label7.set_width(lv.SIZE_CONTENT)
ui_Label7.set_height(lv.SIZE_CONTENT)
ui_Label7.set_x(105)
ui_Label7.set_y(10)
ui_Label7.set_style_text_font( lv.font_montserrat_16, lv.PART.MAIN | lv.STATE.DEFAULT )

ui_Label13 = lv.label(ui_Container8)
ui_Label13.set_text("Mesocricetus auratus")
ui_Label13.set_width(lv.SIZE_CONTENT)
ui_Label13.set_height(lv.SIZE_CONTENT)
ui_Label13.set_x(115)
ui_Label13.set_y(35)
ui_Label13.set_style_text_font( lv.font_montserrat_12, lv.PART.MAIN | lv.STATE.DEFAULT )

ui_Label15 = lv.label(ui_Container8)
ui_Label15.set_text("Occupation: Sleeping,\nrunning, eating")
ui_Label15.set_width(lv.SIZE_CONTENT)
ui_Label15.set_height(lv.SIZE_CONTENT)
ui_Label15.set_x(115)
ui_Label15.set_y(54)
ui_Label15.set_style_text_letter_space( 0, lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Label15.set_style_text_line_space( 1, lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Label15.set_style_text_font( lv.font_montserrat_12, lv.PART.MAIN | lv.STATE.DEFAULT )

ui_Panel1 = lv.obj(ui_Screen1)
ui_Panel1.set_height(30)
ui_Panel1.set_width(lv.pct(100))
ui_Panel1.set_align( lv.ALIGN.TOP_MID)
ui_Panel1.set_style_radius( 0, lv.PART.MAIN | lv.STATE.DEFAULT )

ui_Label14 = lv.label(ui_Panel1)
ui_Label14.set_text("PETS")
ui_Label14.set_width(lv.SIZE_CONTENT)
ui_Label14.set_height(lv.SIZE_CONTENT)
ui_Label14.set_align( lv.ALIGN.CENTER)
ui_Label14.set_style_text_font( lv.font_montserrat_16, lv.PART.MAIN | lv.STATE.DEFAULT )



lv.screen_load(ui_Screen1)
