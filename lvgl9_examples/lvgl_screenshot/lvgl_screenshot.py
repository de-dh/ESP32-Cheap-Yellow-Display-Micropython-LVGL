def save_screen_raw_to_buf(filename='screen.raw'):
    scr = lv.screen_active()
    w = scr.get_width()
    h = scr.get_height()

    # RGB565 = 2 Bytes per pixel
    buf_size = w * h * 2
    buf = bytearray(buf_size)

    img = lv.image_dsc_t()
    res = lv.snapshot_take_to_buf(scr, lv.COLOR_FORMAT.RGB565, img, buf, buf_size)

    if res != lv.RESULT.OK:
        raise RuntimeError('Snapshot failed.')

    with open(filename, 'wb') as f:
        f.write(buf)

    with open(filename + '.txt', 'w') as f:
        f.write('width={}\n'.format(w))
        f.write('height={}\n'.format(h))
        f.write('cf=RGB565\n')
        f.write('size={}\n'.format(buf_size))


#save_screen_raw_to_buf(filename='screen.raw')