import lvgl as lv

# Helper functions for LVGL9.
def SetFlag( obj, flag, value):
    if (value):
        obj.add_flag(flag)
    else:
        obj.remove_flag(flag)
    return

def hide(el):
    if not el.has_flag(lv.obj.FLAG.HIDDEN):
        el.add_flag(lv.obj.FLAG.HIDDEN)

def show(el):
    if el.has_flag(lv.obj.FLAG.HIDDEN):
        el.remove_flag(lv.obj.FLAG.HIDDEN)

def enable(el):
    if el.has_state(lv.STATE.DISABLED):
        el.remove_state(lv.STATE.DISABLED)

def disable(el):
    if not el.has_state(lv.STATE.DISABLED):
        el.add_state(lv.STATE.DISABLED)

def palette_color(c, shade = 0):
    '''
    Returns a color from LVGL's main palette and
    lightens or darkens the color by a specified shade.
    
    Palette Colors:
    RED, PINK, PURPLE, DEEP_PURPLE, INDIGO, BLUE,
    LIGHT_BLUE, CYAN, TEAL, GREEN, LIGHT_GREEN, LIME, 
    YELLOW, AMBER, ORANGE, DEEP_ORANGE, BROWN, BLUE_GREY, GREY
    '''
    attr = getattr(lv.PALETTE, c.upper(), 'Undefined')
    if attr != 'Undefined':
        if not (shade in range(-4, 6)): return lv.color_black()
        if shade == 0:
            return lv.palette_main(attr)
        elif shade > 0:
            return lv.palette_lighten(attr, shade)
        elif shade < 0:
            return lv.palette_darken(attr, abs(shade))
    else:
        return lv.color_black()

def get_all_children(parent_obj, exclude_parent = True):
    child_list = []
    
    def walk(child_obj, data = None):
        # exclude parent obj
        if child_obj == parent_obj and exclude_parent:
            pass
        else:
            child_list.append(child_obj)
            
        return lv.obj.TREE_WALK.NEXT    
        
    parent_obj.tree_walk(walk, None)
    
    return child_list

def utf8Bytes(hexStr: str):
    ''' Helper function used to display icons.
    Returns the six digit utf8 bytecode from four digit Unicode
    as shown on font collection websites (e.g. font awesome, fontello, icomoon)
    for direct use in lvgl.
    'F287' -> b'\0xEF\0x8A\0x87'

    Use:
    obj.set_style_text_font(icon_font, 0)
    obj.set_text(utf8Bytes('F287'))'''

    hexCode = int(hexStr, 16)
    unicodeStr= chr(hexCode)
    utf8Bytecode = unicodeStr.encode('utf-8')
    return utf8Bytecode