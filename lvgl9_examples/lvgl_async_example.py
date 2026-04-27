import lvgl as lv
import lv_config
import lv_utils
import asyncio
from machine import Pin, ADC


# ===== Initialize Hardware ===== #
ldr = ADC(Pin(34), atten=ADC.ATTN_0DB)
# Bright: 75_000 (min value)
# Dark: > 200_000

# ===== Main Screen ===== #
scr = lv.screen_active()
scr.set_style_bg_color(lv.color_black(), lv.PART.MAIN)
scr.remove_flag(lv.obj.FLAG.SCROLLABLE)


# ----- Caption Label ----- #
ldr_caption_label = lv.label(scr)
ldr_caption_label.set_text('LDR VALUE:')
ldr_caption_label.align(lv.ALIGN.CENTER, 0, -30)
ldr_caption_label.set_style_text_color(lv.color_white(), 0)
ldr_caption_label.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)

# ----- LDR Value Label ----- #
ldr_data_label = lv.label(scr)
ldr_data_label.set_text('---')
ldr_data_label.align(lv.ALIGN.CENTER, 0, 0)
ldr_data_label.set_style_text_color(lv.color_white(), 0)
ldr_data_label.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)


async def update():
    
    while True:
        await asyncio.sleep(0.2)
        ldr_data_label.set_text(str(ldr.read_uv()))
        ldr_data_label.invalidate()
    

async def main():
    print('Starting Main')
    
    update_task = asyncio.create_task(update())
    
    if not lv_utils.event_loop.is_running():
        eventloop = lv_utils.event_loop(asynchronous=True)

    loop = asyncio.get_event_loop()
    loop.run_forever()
    

asyncio.run(main())