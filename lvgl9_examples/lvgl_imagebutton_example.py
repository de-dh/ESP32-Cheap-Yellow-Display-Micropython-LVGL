import lvgl as lv
import lv_config


scr = lv.screen_active()
scr.set_style_bg_color(lv.color_white(), 0)


def get_image_data(filename):
    with open(filename, 'rb') as f:
        imgdata = f.read()

    return imgdata
    
def create_img_dsc(imgdata):
    imgdsc = lv.image_dsc_t({'data_size':len(imgdata), 'data':imgdata})
    return imgdsc


ui_Label1 = lv.label(scr)
ui_Label1.set_text("STATE: Released")
ui_Label1.align(lv.ALIGN.TOP_MID, 0, 30)
ui_Label1.set_style_text_font( lv.font_montserrat_16, lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Label1.set_style_text_color(lv.color_black(), lv.PART.MAIN | lv.STATE.DEFAULT )

image_data = get_image_data('assets/gears1.png')
image_data_mv = memoryview(image_data)
img_dsc = create_img_dsc(image_data_mv)

image_data_2 = get_image_data('assets/gears2.png')
image_data_mv_2 = memoryview(image_data_2)
img_dsc_2 = create_img_dsc(image_data_mv_2)

imgbtn1 = lv.imagebutton(scr)
imgbtn1.set_src(lv.imagebutton.STATE.RELEASED, None, img_dsc, None)
imgbtn1.set_src(lv.imagebutton.STATE.PRESSED, None, img_dsc_2, None)
imgbtn1.center()
imgbtn1.add_event_cb(lambda e: ui_Label1.set_text('STATE: Pressed'), lv.EVENT.PRESSED, None)
imgbtn1.add_event_cb(lambda e: ui_Label1.set_text('STATE: Released'), lv.EVENT.RELEASED, None)