'''Wrapper for cairo

Generated with:
tools/genwrappers.py cairo

Do not modify this file.
'''

__docformat__ =  'restructuredtext'
__version__ = '$Id: wrap.py 1694 2008-01-30 23:12:00Z Alex.Holkner $'

import ctypes
from ctypes import *

import pyglet.lib

_lib = pyglet.lib.load_library('cairo')

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]


import pyglet.gl.glx
import pyglet.window.xlib.xlib

CAIRO_VERSION = 10600 	# /usr/include/cairo/cairo.h:229
# /usr/include/cairo/cairo.h:235
cairo_version = _lib.cairo_version
cairo_version.restype = c_int
cairo_version.argtypes = []

# /usr/include/cairo/cairo.h:237
cairo_version_string = _lib.cairo_version_string
cairo_version_string.restype = c_char_p
cairo_version_string.argtypes = []

cairo_bool_t = c_int 	# /usr/include/cairo/cairo.h:254
class struct__cairo(Structure):
    __slots__ = [
    ]
struct__cairo._fields_ = [
    ('_opaque_struct', c_int)
]

class struct__cairo(Structure):
    __slots__ = [
    ]
struct__cairo._fields_ = [
    ('_opaque_struct', c_int)
]

cairo_t = struct__cairo 	# /usr/include/cairo/cairo.h:269
class struct__cairo_surface(Structure):
    __slots__ = [
    ]
struct__cairo_surface._fields_ = [
    ('_opaque_struct', c_int)
]

class struct__cairo_surface(Structure):
    __slots__ = [
    ]
struct__cairo_surface._fields_ = [
    ('_opaque_struct', c_int)
]

cairo_surface_t = struct__cairo_surface 	# /usr/include/cairo/cairo.h:287
class struct__cairo_matrix(Structure):
    __slots__ = [
        'xx',
        'yx',
        'xy',
        'yy',
        'x0',
        'y0',
    ]
struct__cairo_matrix._fields_ = [
    ('xx', c_double),
    ('yx', c_double),
    ('xy', c_double),
    ('yy', c_double),
    ('x0', c_double),
    ('y0', c_double),
]

cairo_matrix_t = struct__cairo_matrix 	# /usr/include/cairo/cairo.h:310
class struct__cairo_pattern(Structure):
    __slots__ = [
    ]
struct__cairo_pattern._fields_ = [
    ('_opaque_struct', c_int)
]

class struct__cairo_pattern(Structure):
    __slots__ = [
    ]
struct__cairo_pattern._fields_ = [
    ('_opaque_struct', c_int)
]

cairo_pattern_t = struct__cairo_pattern 	# /usr/include/cairo/cairo.h:331
cairo_destroy_func_t = CFUNCTYPE(None, POINTER(None)) 	# /usr/include/cairo/cairo.h:341
class struct__cairo_user_data_key(Structure):
    __slots__ = [
        'unused',
    ]
struct__cairo_user_data_key._fields_ = [
    ('unused', c_int),
]

cairo_user_data_key_t = struct__cairo_user_data_key 	# /usr/include/cairo/cairo.h:355
enum__cairo_status = c_int
CAIRO_STATUS_SUCCESS = 0
CAIRO_STATUS_NO_MEMORY = 1
CAIRO_STATUS_INVALID_RESTORE = 2
CAIRO_STATUS_INVALID_POP_GROUP = 3
CAIRO_STATUS_NO_CURRENT_POINT = 4
CAIRO_STATUS_INVALID_MATRIX = 5
CAIRO_STATUS_INVALID_STATUS = 6
CAIRO_STATUS_NULL_POINTER = 7
CAIRO_STATUS_INVALID_STRING = 8
CAIRO_STATUS_INVALID_PATH_DATA = 9
CAIRO_STATUS_READ_ERROR = 10
CAIRO_STATUS_WRITE_ERROR = 11
CAIRO_STATUS_SURFACE_FINISHED = 12
CAIRO_STATUS_SURFACE_TYPE_MISMATCH = 13
CAIRO_STATUS_PATTERN_TYPE_MISMATCH = 14
CAIRO_STATUS_INVALID_CONTENT = 15
CAIRO_STATUS_INVALID_FORMAT = 16
CAIRO_STATUS_INVALID_VISUAL = 17
CAIRO_STATUS_FILE_NOT_FOUND = 18
CAIRO_STATUS_INVALID_DASH = 19
CAIRO_STATUS_INVALID_DSC_COMMENT = 20
CAIRO_STATUS_INVALID_INDEX = 21
CAIRO_STATUS_CLIP_NOT_REPRESENTABLE = 22
CAIRO_STATUS_TEMP_FILE_ERROR = 23
CAIRO_STATUS_INVALID_STRIDE = 24
cairo_status_t = enum__cairo_status 	# /usr/include/cairo/cairo.h:420
enum__cairo_content = c_int
CAIRO_CONTENT_COLOR = 0
CAIRO_CONTENT_ALPHA = 1
CAIRO_CONTENT_COLOR_ALPHA = 2
cairo_content_t = enum__cairo_content 	# /usr/include/cairo/cairo.h:440
cairo_write_func_t = CFUNCTYPE(cairo_status_t, POINTER(None), POINTER(c_ubyte), c_uint) 	# /usr/include/cairo/cairo.h:458
cairo_read_func_t = CFUNCTYPE(cairo_status_t, POINTER(None), POINTER(c_ubyte), c_uint) 	# /usr/include/cairo/cairo.h:478
# /usr/include/cairo/cairo.h:483
cairo_create = _lib.cairo_create
cairo_create.restype = POINTER(cairo_t)
cairo_create.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:486
cairo_reference = _lib.cairo_reference
cairo_reference.restype = POINTER(cairo_t)
cairo_reference.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:490
cairo_destroy = _lib.cairo_destroy
cairo_destroy.restype = None
cairo_destroy.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:493
cairo_get_reference_count = _lib.cairo_get_reference_count
cairo_get_reference_count.restype = c_uint
cairo_get_reference_count.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:495
cairo_get_user_data = _lib.cairo_get_user_data
cairo_get_user_data.restype = POINTER(c_void)
cairo_get_user_data.argtypes = [POINTER(cairo_t), POINTER(cairo_user_data_key_t)]

# /usr/include/cairo/cairo.h:500
cairo_set_user_data = _lib.cairo_set_user_data
cairo_set_user_data.restype = cairo_status_t
cairo_set_user_data.argtypes = [POINTER(cairo_t), POINTER(cairo_user_data_key_t), POINTER(None), cairo_destroy_func_t]

# /usr/include/cairo/cairo.h:506
cairo_save = _lib.cairo_save
cairo_save.restype = None
cairo_save.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:509
cairo_restore = _lib.cairo_restore
cairo_restore.restype = None
cairo_restore.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:512
cairo_push_group = _lib.cairo_push_group
cairo_push_group.restype = None
cairo_push_group.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:515
cairo_push_group_with_content = _lib.cairo_push_group_with_content
cairo_push_group_with_content.restype = None
cairo_push_group_with_content.argtypes = [POINTER(cairo_t), cairo_content_t]

# /usr/include/cairo/cairo.h:517
cairo_pop_group = _lib.cairo_pop_group
cairo_pop_group.restype = POINTER(cairo_pattern_t)
cairo_pop_group.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:521
cairo_pop_group_to_source = _lib.cairo_pop_group_to_source
cairo_pop_group_to_source.restype = None
cairo_pop_group_to_source.argtypes = [POINTER(cairo_t)]

enum__cairo_operator = c_int
CAIRO_OPERATOR_CLEAR = 0
CAIRO_OPERATOR_SOURCE = 1
CAIRO_OPERATOR_OVER = 2
CAIRO_OPERATOR_IN = 3
CAIRO_OPERATOR_OUT = 4
CAIRO_OPERATOR_ATOP = 5
CAIRO_OPERATOR_DEST = 6
CAIRO_OPERATOR_DEST_OVER = 7
CAIRO_OPERATOR_DEST_IN = 8
CAIRO_OPERATOR_DEST_OUT = 9
CAIRO_OPERATOR_DEST_ATOP = 10
CAIRO_OPERATOR_XOR = 11
CAIRO_OPERATOR_ADD = 12
CAIRO_OPERATOR_SATURATE = 13
cairo_operator_t = enum__cairo_operator 	# /usr/include/cairo/cairo.h:587
# /usr/include/cairo/cairo.h:590
cairo_set_operator = _lib.cairo_set_operator
cairo_set_operator.restype = None
cairo_set_operator.argtypes = [POINTER(cairo_t), cairo_operator_t]

# /usr/include/cairo/cairo.h:593
cairo_set_source = _lib.cairo_set_source
cairo_set_source.restype = None
cairo_set_source.argtypes = [POINTER(cairo_t), POINTER(cairo_pattern_t)]

# /usr/include/cairo/cairo.h:596
cairo_set_source_rgb = _lib.cairo_set_source_rgb
cairo_set_source_rgb.restype = None
cairo_set_source_rgb.argtypes = [POINTER(cairo_t), c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:599
cairo_set_source_rgba = _lib.cairo_set_source_rgba
cairo_set_source_rgba.restype = None
cairo_set_source_rgba.argtypes = [POINTER(cairo_t), c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:604
cairo_set_source_surface = _lib.cairo_set_source_surface
cairo_set_source_surface.restype = None
cairo_set_source_surface.argtypes = [POINTER(cairo_t), POINTER(cairo_surface_t), c_double, c_double]

# /usr/include/cairo/cairo.h:610
cairo_set_tolerance = _lib.cairo_set_tolerance
cairo_set_tolerance.restype = None
cairo_set_tolerance.argtypes = [POINTER(cairo_t), c_double]

enum__cairo_antialias = c_int
CAIRO_ANTIALIAS_DEFAULT = 0
CAIRO_ANTIALIAS_NONE = 1
CAIRO_ANTIALIAS_GRAY = 2
CAIRO_ANTIALIAS_SUBPIXEL = 3
cairo_antialias_t = enum__cairo_antialias 	# /usr/include/cairo/cairo.h:630
# /usr/include/cairo/cairo.h:633
cairo_set_antialias = _lib.cairo_set_antialias
cairo_set_antialias.restype = None
cairo_set_antialias.argtypes = [POINTER(cairo_t), cairo_antialias_t]

enum__cairo_fill_rule = c_int
CAIRO_FILL_RULE_WINDING = 0
CAIRO_FILL_RULE_EVEN_ODD = 1
cairo_fill_rule_t = enum__cairo_fill_rule 	# /usr/include/cairo/cairo.h:663
# /usr/include/cairo/cairo.h:666
cairo_set_fill_rule = _lib.cairo_set_fill_rule
cairo_set_fill_rule.restype = None
cairo_set_fill_rule.argtypes = [POINTER(cairo_t), cairo_fill_rule_t]

# /usr/include/cairo/cairo.h:669
cairo_set_line_width = _lib.cairo_set_line_width
cairo_set_line_width.restype = None
cairo_set_line_width.argtypes = [POINTER(cairo_t), c_double]

enum__cairo_line_cap = c_int
CAIRO_LINE_CAP_BUTT = 0
CAIRO_LINE_CAP_ROUND = 1
CAIRO_LINE_CAP_SQUARE = 2
cairo_line_cap_t = enum__cairo_line_cap 	# /usr/include/cairo/cairo.h:685
# /usr/include/cairo/cairo.h:688
cairo_set_line_cap = _lib.cairo_set_line_cap
cairo_set_line_cap.restype = None
cairo_set_line_cap.argtypes = [POINTER(cairo_t), cairo_line_cap_t]

enum__cairo_line_join = c_int
CAIRO_LINE_JOIN_MITER = 0
CAIRO_LINE_JOIN_ROUND = 1
CAIRO_LINE_JOIN_BEVEL = 2
cairo_line_join_t = enum__cairo_line_join 	# /usr/include/cairo/cairo.h:707
# /usr/include/cairo/cairo.h:710
cairo_set_line_join = _lib.cairo_set_line_join
cairo_set_line_join.restype = None
cairo_set_line_join.argtypes = [POINTER(cairo_t), cairo_line_join_t]

# /usr/include/cairo/cairo.h:713
cairo_set_dash = _lib.cairo_set_dash
cairo_set_dash.restype = None
cairo_set_dash.argtypes = [POINTER(cairo_t), POINTER(c_double), c_int, c_double]

# /usr/include/cairo/cairo.h:719
cairo_set_miter_limit = _lib.cairo_set_miter_limit
cairo_set_miter_limit.restype = None
cairo_set_miter_limit.argtypes = [POINTER(cairo_t), c_double]

# /usr/include/cairo/cairo.h:722
cairo_translate = _lib.cairo_translate
cairo_translate.restype = None
cairo_translate.argtypes = [POINTER(cairo_t), c_double, c_double]

# /usr/include/cairo/cairo.h:725
cairo_scale = _lib.cairo_scale
cairo_scale.restype = None
cairo_scale.argtypes = [POINTER(cairo_t), c_double, c_double]

# /usr/include/cairo/cairo.h:728
cairo_rotate = _lib.cairo_rotate
cairo_rotate.restype = None
cairo_rotate.argtypes = [POINTER(cairo_t), c_double]

# /usr/include/cairo/cairo.h:731
cairo_transform = _lib.cairo_transform
cairo_transform.restype = None
cairo_transform.argtypes = [POINTER(cairo_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:735
cairo_set_matrix = _lib.cairo_set_matrix
cairo_set_matrix.restype = None
cairo_set_matrix.argtypes = [POINTER(cairo_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:739
cairo_identity_matrix = _lib.cairo_identity_matrix
cairo_identity_matrix.restype = None
cairo_identity_matrix.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:742
cairo_user_to_device = _lib.cairo_user_to_device
cairo_user_to_device.restype = None
cairo_user_to_device.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:745
cairo_user_to_device_distance = _lib.cairo_user_to_device_distance
cairo_user_to_device_distance.restype = None
cairo_user_to_device_distance.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:748
cairo_device_to_user = _lib.cairo_device_to_user
cairo_device_to_user.restype = None
cairo_device_to_user.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:751
cairo_device_to_user_distance = _lib.cairo_device_to_user_distance
cairo_device_to_user_distance.restype = None
cairo_device_to_user_distance.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:755
cairo_new_path = _lib.cairo_new_path
cairo_new_path.restype = None
cairo_new_path.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:758
cairo_move_to = _lib.cairo_move_to
cairo_move_to.restype = None
cairo_move_to.argtypes = [POINTER(cairo_t), c_double, c_double]

# /usr/include/cairo/cairo.h:761
cairo_new_sub_path = _lib.cairo_new_sub_path
cairo_new_sub_path.restype = None
cairo_new_sub_path.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:764
cairo_line_to = _lib.cairo_line_to
cairo_line_to.restype = None
cairo_line_to.argtypes = [POINTER(cairo_t), c_double, c_double]

# /usr/include/cairo/cairo.h:767
cairo_curve_to = _lib.cairo_curve_to
cairo_curve_to.restype = None
cairo_curve_to.argtypes = [POINTER(cairo_t), c_double, c_double, c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:773
cairo_arc = _lib.cairo_arc
cairo_arc.restype = None
cairo_arc.argtypes = [POINTER(cairo_t), c_double, c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:779
cairo_arc_negative = _lib.cairo_arc_negative
cairo_arc_negative.restype = None
cairo_arc_negative.argtypes = [POINTER(cairo_t), c_double, c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:793
cairo_rel_move_to = _lib.cairo_rel_move_to
cairo_rel_move_to.restype = None
cairo_rel_move_to.argtypes = [POINTER(cairo_t), c_double, c_double]

# /usr/include/cairo/cairo.h:796
cairo_rel_line_to = _lib.cairo_rel_line_to
cairo_rel_line_to.restype = None
cairo_rel_line_to.argtypes = [POINTER(cairo_t), c_double, c_double]

# /usr/include/cairo/cairo.h:799
cairo_rel_curve_to = _lib.cairo_rel_curve_to
cairo_rel_curve_to.restype = None
cairo_rel_curve_to.argtypes = [POINTER(cairo_t), c_double, c_double, c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:805
cairo_rectangle = _lib.cairo_rectangle
cairo_rectangle.restype = None
cairo_rectangle.argtypes = [POINTER(cairo_t), c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:815
cairo_close_path = _lib.cairo_close_path
cairo_close_path.restype = None
cairo_close_path.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:818
cairo_path_extents = _lib.cairo_path_extents
cairo_path_extents.restype = None
cairo_path_extents.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:824
cairo_paint = _lib.cairo_paint
cairo_paint.restype = None
cairo_paint.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:827
cairo_paint_with_alpha = _lib.cairo_paint_with_alpha
cairo_paint_with_alpha.restype = None
cairo_paint_with_alpha.argtypes = [POINTER(cairo_t), c_double]

# /usr/include/cairo/cairo.h:831
cairo_mask = _lib.cairo_mask
cairo_mask.restype = None
cairo_mask.argtypes = [POINTER(cairo_t), POINTER(cairo_pattern_t)]

# /usr/include/cairo/cairo.h:835
cairo_mask_surface = _lib.cairo_mask_surface
cairo_mask_surface.restype = None
cairo_mask_surface.argtypes = [POINTER(cairo_t), POINTER(cairo_surface_t), c_double, c_double]

# /usr/include/cairo/cairo.h:841
cairo_stroke = _lib.cairo_stroke
cairo_stroke.restype = None
cairo_stroke.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:844
cairo_stroke_preserve = _lib.cairo_stroke_preserve
cairo_stroke_preserve.restype = None
cairo_stroke_preserve.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:847
cairo_fill = _lib.cairo_fill
cairo_fill.restype = None
cairo_fill.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:850
cairo_fill_preserve = _lib.cairo_fill_preserve
cairo_fill_preserve.restype = None
cairo_fill_preserve.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:853
cairo_copy_page = _lib.cairo_copy_page
cairo_copy_page.restype = None
cairo_copy_page.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:856
cairo_show_page = _lib.cairo_show_page
cairo_show_page.restype = None
cairo_show_page.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:860
cairo_in_stroke = _lib.cairo_in_stroke
cairo_in_stroke.restype = cairo_bool_t
cairo_in_stroke.argtypes = [POINTER(cairo_t), c_double, c_double]

# /usr/include/cairo/cairo.h:863
cairo_in_fill = _lib.cairo_in_fill
cairo_in_fill.restype = cairo_bool_t
cairo_in_fill.argtypes = [POINTER(cairo_t), c_double, c_double]

# /usr/include/cairo/cairo.h:867
cairo_stroke_extents = _lib.cairo_stroke_extents
cairo_stroke_extents.restype = None
cairo_stroke_extents.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:872
cairo_fill_extents = _lib.cairo_fill_extents
cairo_fill_extents.restype = None
cairo_fill_extents.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:878
cairo_reset_clip = _lib.cairo_reset_clip
cairo_reset_clip.restype = None
cairo_reset_clip.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:881
cairo_clip = _lib.cairo_clip
cairo_clip.restype = None
cairo_clip.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:884
cairo_clip_preserve = _lib.cairo_clip_preserve
cairo_clip_preserve.restype = None
cairo_clip_preserve.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:887
cairo_clip_extents = _lib.cairo_clip_extents
cairo_clip_extents.restype = None
cairo_clip_extents.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

class struct__cairo_rectangle(Structure):
    __slots__ = [
        'x',
        'y',
        'width',
        'height',
    ]
struct__cairo_rectangle._fields_ = [
    ('x', c_double),
    ('y', c_double),
    ('width', c_double),
    ('height', c_double),
]

cairo_rectangle_t = struct__cairo_rectangle 	# /usr/include/cairo/cairo.h:904
class struct__cairo_rectangle_list(Structure):
    __slots__ = [
        'status',
        'rectangles',
        'num_rectangles',
    ]
struct__cairo_rectangle_list._fields_ = [
    ('status', cairo_status_t),
    ('rectangles', POINTER(cairo_rectangle_t)),
    ('num_rectangles', c_int),
]

cairo_rectangle_list_t = struct__cairo_rectangle_list 	# /usr/include/cairo/cairo.h:921
# /usr/include/cairo/cairo.h:923
cairo_copy_clip_rectangle_list = _lib.cairo_copy_clip_rectangle_list
cairo_copy_clip_rectangle_list.restype = POINTER(cairo_rectangle_list_t)
cairo_copy_clip_rectangle_list.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:927
cairo_rectangle_list_destroy = _lib.cairo_rectangle_list_destroy
cairo_rectangle_list_destroy.restype = None
cairo_rectangle_list_destroy.argtypes = [POINTER(cairo_rectangle_list_t)]

class struct__cairo_scaled_font(Structure):
    __slots__ = [
    ]
struct__cairo_scaled_font._fields_ = [
    ('_opaque_struct', c_int)
]

class struct__cairo_scaled_font(Structure):
    __slots__ = [
    ]
struct__cairo_scaled_font._fields_ = [
    ('_opaque_struct', c_int)
]

cairo_scaled_font_t = struct__cairo_scaled_font 	# /usr/include/cairo/cairo.h:946
class struct__cairo_font_face(Structure):
    __slots__ = [
    ]
struct__cairo_font_face._fields_ = [
    ('_opaque_struct', c_int)
]

class struct__cairo_font_face(Structure):
    __slots__ = [
    ]
struct__cairo_font_face._fields_ = [
    ('_opaque_struct', c_int)
]

cairo_font_face_t = struct__cairo_font_face 	# /usr/include/cairo/cairo.h:965
class struct_anon_1(Structure):
    __slots__ = [
        'index',
        'x',
        'y',
    ]
struct_anon_1._fields_ = [
    ('index', c_ulong),
    ('x', c_double),
    ('y', c_double),
]

cairo_glyph_t = struct_anon_1 	# /usr/include/cairo/cairo.h:995
class struct_anon_2(Structure):
    __slots__ = [
        'x_bearing',
        'y_bearing',
        'width',
        'height',
        'x_advance',
        'y_advance',
    ]
struct_anon_2._fields_ = [
    ('x_bearing', c_double),
    ('y_bearing', c_double),
    ('width', c_double),
    ('height', c_double),
    ('x_advance', c_double),
    ('y_advance', c_double),
]

cairo_text_extents_t = struct_anon_2 	# /usr/include/cairo/cairo.h:1031
class struct_anon_3(Structure):
    __slots__ = [
        'ascent',
        'descent',
        'height',
        'max_x_advance',
        'max_y_advance',
    ]
struct_anon_3._fields_ = [
    ('ascent', c_double),
    ('descent', c_double),
    ('height', c_double),
    ('max_x_advance', c_double),
    ('max_y_advance', c_double),
]

cairo_font_extents_t = struct_anon_3 	# /usr/include/cairo/cairo.h:1080
enum__cairo_font_slant = c_int
CAIRO_FONT_SLANT_NORMAL = 0
CAIRO_FONT_SLANT_ITALIC = 1
CAIRO_FONT_SLANT_OBLIQUE = 2
cairo_font_slant_t = enum__cairo_font_slant 	# /usr/include/cairo/cairo.h:1094
enum__cairo_font_weight = c_int
CAIRO_FONT_WEIGHT_NORMAL = 0
CAIRO_FONT_WEIGHT_BOLD = 1
cairo_font_weight_t = enum__cairo_font_weight 	# /usr/include/cairo/cairo.h:1106
enum__cairo_subpixel_order = c_int
CAIRO_SUBPIXEL_ORDER_DEFAULT = 0
CAIRO_SUBPIXEL_ORDER_RGB = 1
CAIRO_SUBPIXEL_ORDER_BGR = 2
CAIRO_SUBPIXEL_ORDER_VRGB = 3
CAIRO_SUBPIXEL_ORDER_VBGR = 4
cairo_subpixel_order_t = enum__cairo_subpixel_order 	# /usr/include/cairo/cairo.h:1131
enum__cairo_hint_style = c_int
CAIRO_HINT_STYLE_DEFAULT = 0
CAIRO_HINT_STYLE_NONE = 1
CAIRO_HINT_STYLE_SLIGHT = 2
CAIRO_HINT_STYLE_MEDIUM = 3
CAIRO_HINT_STYLE_FULL = 4
cairo_hint_style_t = enum__cairo_hint_style 	# /usr/include/cairo/cairo.h:1161
enum__cairo_hint_metrics = c_int
CAIRO_HINT_METRICS_DEFAULT = 0
CAIRO_HINT_METRICS_OFF = 1
CAIRO_HINT_METRICS_ON = 2
cairo_hint_metrics_t = enum__cairo_hint_metrics 	# /usr/include/cairo/cairo.h:1180
class struct__cairo_font_options(Structure):
    __slots__ = [
    ]
struct__cairo_font_options._fields_ = [
    ('_opaque_struct', c_int)
]

class struct__cairo_font_options(Structure):
    __slots__ = [
    ]
struct__cairo_font_options._fields_ = [
    ('_opaque_struct', c_int)
]

cairo_font_options_t = struct__cairo_font_options 	# /usr/include/cairo/cairo.h:1202
# /usr/include/cairo/cairo.h:1204
cairo_font_options_create = _lib.cairo_font_options_create
cairo_font_options_create.restype = POINTER(cairo_font_options_t)
cairo_font_options_create.argtypes = []

# /usr/include/cairo/cairo.h:1207
cairo_font_options_copy = _lib.cairo_font_options_copy
cairo_font_options_copy.restype = POINTER(cairo_font_options_t)
cairo_font_options_copy.argtypes = [POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1211
cairo_font_options_destroy = _lib.cairo_font_options_destroy
cairo_font_options_destroy.restype = None
cairo_font_options_destroy.argtypes = [POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1214
cairo_font_options_status = _lib.cairo_font_options_status
cairo_font_options_status.restype = cairo_status_t
cairo_font_options_status.argtypes = [POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1217
cairo_font_options_merge = _lib.cairo_font_options_merge
cairo_font_options_merge.restype = None
cairo_font_options_merge.argtypes = [POINTER(cairo_font_options_t), POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1220
cairo_font_options_equal = _lib.cairo_font_options_equal
cairo_font_options_equal.restype = cairo_bool_t
cairo_font_options_equal.argtypes = [POINTER(cairo_font_options_t), POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1224
cairo_font_options_hash = _lib.cairo_font_options_hash
cairo_font_options_hash.restype = c_ulong
cairo_font_options_hash.argtypes = [POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1227
cairo_font_options_set_antialias = _lib.cairo_font_options_set_antialias
cairo_font_options_set_antialias.restype = None
cairo_font_options_set_antialias.argtypes = [POINTER(cairo_font_options_t), cairo_antialias_t]

# /usr/include/cairo/cairo.h:1230
cairo_font_options_get_antialias = _lib.cairo_font_options_get_antialias
cairo_font_options_get_antialias.restype = cairo_antialias_t
cairo_font_options_get_antialias.argtypes = [POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1233
cairo_font_options_set_subpixel_order = _lib.cairo_font_options_set_subpixel_order
cairo_font_options_set_subpixel_order.restype = None
cairo_font_options_set_subpixel_order.argtypes = [POINTER(cairo_font_options_t), cairo_subpixel_order_t]

# /usr/include/cairo/cairo.h:1236
cairo_font_options_get_subpixel_order = _lib.cairo_font_options_get_subpixel_order
cairo_font_options_get_subpixel_order.restype = cairo_subpixel_order_t
cairo_font_options_get_subpixel_order.argtypes = [POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1239
cairo_font_options_set_hint_style = _lib.cairo_font_options_set_hint_style
cairo_font_options_set_hint_style.restype = None
cairo_font_options_set_hint_style.argtypes = [POINTER(cairo_font_options_t), cairo_hint_style_t]

# /usr/include/cairo/cairo.h:1242
cairo_font_options_get_hint_style = _lib.cairo_font_options_get_hint_style
cairo_font_options_get_hint_style.restype = cairo_hint_style_t
cairo_font_options_get_hint_style.argtypes = [POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1245
cairo_font_options_set_hint_metrics = _lib.cairo_font_options_set_hint_metrics
cairo_font_options_set_hint_metrics.restype = None
cairo_font_options_set_hint_metrics.argtypes = [POINTER(cairo_font_options_t), cairo_hint_metrics_t]

# /usr/include/cairo/cairo.h:1248
cairo_font_options_get_hint_metrics = _lib.cairo_font_options_get_hint_metrics
cairo_font_options_get_hint_metrics.restype = cairo_hint_metrics_t
cairo_font_options_get_hint_metrics.argtypes = [POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1254
cairo_select_font_face = _lib.cairo_select_font_face
cairo_select_font_face.restype = None
cairo_select_font_face.argtypes = [POINTER(cairo_t), c_char_p, cairo_font_slant_t, cairo_font_weight_t]

# /usr/include/cairo/cairo.h:1260
cairo_set_font_size = _lib.cairo_set_font_size
cairo_set_font_size.restype = None
cairo_set_font_size.argtypes = [POINTER(cairo_t), c_double]

# /usr/include/cairo/cairo.h:1263
cairo_set_font_matrix = _lib.cairo_set_font_matrix
cairo_set_font_matrix.restype = None
cairo_set_font_matrix.argtypes = [POINTER(cairo_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:1267
cairo_get_font_matrix = _lib.cairo_get_font_matrix
cairo_get_font_matrix.restype = None
cairo_get_font_matrix.argtypes = [POINTER(cairo_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:1271
cairo_set_font_options = _lib.cairo_set_font_options
cairo_set_font_options.restype = None
cairo_set_font_options.argtypes = [POINTER(cairo_t), POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1275
cairo_get_font_options = _lib.cairo_get_font_options
cairo_get_font_options.restype = None
cairo_get_font_options.argtypes = [POINTER(cairo_t), POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1279
cairo_set_font_face = _lib.cairo_set_font_face
cairo_set_font_face.restype = None
cairo_set_font_face.argtypes = [POINTER(cairo_t), POINTER(cairo_font_face_t)]

# /usr/include/cairo/cairo.h:1281
cairo_get_font_face = _lib.cairo_get_font_face
cairo_get_font_face.restype = POINTER(cairo_font_face_t)
cairo_get_font_face.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1285
cairo_set_scaled_font = _lib.cairo_set_scaled_font
cairo_set_scaled_font.restype = None
cairo_set_scaled_font.argtypes = [POINTER(cairo_t), POINTER(cairo_scaled_font_t)]

# /usr/include/cairo/cairo.h:1288
cairo_get_scaled_font = _lib.cairo_get_scaled_font
cairo_get_scaled_font.restype = POINTER(cairo_scaled_font_t)
cairo_get_scaled_font.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1292
cairo_show_text = _lib.cairo_show_text
cairo_show_text.restype = None
cairo_show_text.argtypes = [POINTER(cairo_t), c_char_p]

# /usr/include/cairo/cairo.h:1295
cairo_show_glyphs = _lib.cairo_show_glyphs
cairo_show_glyphs.restype = None
cairo_show_glyphs.argtypes = [POINTER(cairo_t), POINTER(cairo_glyph_t), c_int]

# /usr/include/cairo/cairo.h:1298
cairo_text_path = _lib.cairo_text_path
cairo_text_path.restype = None
cairo_text_path.argtypes = [POINTER(cairo_t), c_char_p]

# /usr/include/cairo/cairo.h:1301
cairo_glyph_path = _lib.cairo_glyph_path
cairo_glyph_path.restype = None
cairo_glyph_path.argtypes = [POINTER(cairo_t), POINTER(cairo_glyph_t), c_int]

# /usr/include/cairo/cairo.h:1304
cairo_text_extents = _lib.cairo_text_extents
cairo_text_extents.restype = None
cairo_text_extents.argtypes = [POINTER(cairo_t), c_char_p, POINTER(cairo_text_extents_t)]

# /usr/include/cairo/cairo.h:1309
cairo_glyph_extents = _lib.cairo_glyph_extents
cairo_glyph_extents.restype = None
cairo_glyph_extents.argtypes = [POINTER(cairo_t), POINTER(cairo_glyph_t), c_int, POINTER(cairo_text_extents_t)]

# /usr/include/cairo/cairo.h:1315
cairo_font_extents = _lib.cairo_font_extents
cairo_font_extents.restype = None
cairo_font_extents.argtypes = [POINTER(cairo_t), POINTER(cairo_font_extents_t)]

# /usr/include/cairo/cairo.h:1320
cairo_font_face_reference = _lib.cairo_font_face_reference
cairo_font_face_reference.restype = POINTER(cairo_font_face_t)
cairo_font_face_reference.argtypes = [POINTER(cairo_font_face_t)]

# /usr/include/cairo/cairo.h:1324
cairo_font_face_destroy = _lib.cairo_font_face_destroy
cairo_font_face_destroy.restype = None
cairo_font_face_destroy.argtypes = [POINTER(cairo_font_face_t)]

# /usr/include/cairo/cairo.h:1327
cairo_font_face_get_reference_count = _lib.cairo_font_face_get_reference_count
cairo_font_face_get_reference_count.restype = c_uint
cairo_font_face_get_reference_count.argtypes = [POINTER(cairo_font_face_t)]

# /usr/include/cairo/cairo.h:1330
cairo_font_face_status = _lib.cairo_font_face_status
cairo_font_face_status.restype = cairo_status_t
cairo_font_face_status.argtypes = [POINTER(cairo_font_face_t)]

enum__cairo_font_type = c_int
CAIRO_FONT_TYPE_TOY = 0
CAIRO_FONT_TYPE_FT = 1
CAIRO_FONT_TYPE_WIN32 = 2
CAIRO_FONT_TYPE_QUARTZ = 3
cairo_font_type_t = enum__cairo_font_type 	# /usr/include/cairo/cairo.h:1373
# /usr/include/cairo/cairo.h:1376
cairo_font_face_get_type = _lib.cairo_font_face_get_type
cairo_font_face_get_type.restype = cairo_font_type_t
cairo_font_face_get_type.argtypes = [POINTER(cairo_font_face_t)]

# /usr/include/cairo/cairo.h:1378
cairo_font_face_get_user_data = _lib.cairo_font_face_get_user_data
cairo_font_face_get_user_data.restype = POINTER(c_void)
cairo_font_face_get_user_data.argtypes = [POINTER(cairo_font_face_t), POINTER(cairo_user_data_key_t)]

# /usr/include/cairo/cairo.h:1383
cairo_font_face_set_user_data = _lib.cairo_font_face_set_user_data
cairo_font_face_set_user_data.restype = cairo_status_t
cairo_font_face_set_user_data.argtypes = [POINTER(cairo_font_face_t), POINTER(cairo_user_data_key_t), POINTER(None), cairo_destroy_func_t]

# /usr/include/cairo/cairo.h:1390
cairo_scaled_font_create = _lib.cairo_scaled_font_create
cairo_scaled_font_create.restype = POINTER(cairo_scaled_font_t)
cairo_scaled_font_create.argtypes = [POINTER(cairo_font_face_t), POINTER(cairo_matrix_t), POINTER(cairo_matrix_t), POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1396
cairo_scaled_font_reference = _lib.cairo_scaled_font_reference
cairo_scaled_font_reference.restype = POINTER(cairo_scaled_font_t)
cairo_scaled_font_reference.argtypes = [POINTER(cairo_scaled_font_t)]

# /usr/include/cairo/cairo.h:1400
cairo_scaled_font_destroy = _lib.cairo_scaled_font_destroy
cairo_scaled_font_destroy.restype = None
cairo_scaled_font_destroy.argtypes = [POINTER(cairo_scaled_font_t)]

# /usr/include/cairo/cairo.h:1403
cairo_scaled_font_get_reference_count = _lib.cairo_scaled_font_get_reference_count
cairo_scaled_font_get_reference_count.restype = c_uint
cairo_scaled_font_get_reference_count.argtypes = [POINTER(cairo_scaled_font_t)]

# /usr/include/cairo/cairo.h:1406
cairo_scaled_font_status = _lib.cairo_scaled_font_status
cairo_scaled_font_status.restype = cairo_status_t
cairo_scaled_font_status.argtypes = [POINTER(cairo_scaled_font_t)]

# /usr/include/cairo/cairo.h:1409
cairo_scaled_font_get_type = _lib.cairo_scaled_font_get_type
cairo_scaled_font_get_type.restype = cairo_font_type_t
cairo_scaled_font_get_type.argtypes = [POINTER(cairo_scaled_font_t)]

# /usr/include/cairo/cairo.h:1411
cairo_scaled_font_get_user_data = _lib.cairo_scaled_font_get_user_data
cairo_scaled_font_get_user_data.restype = POINTER(c_void)
cairo_scaled_font_get_user_data.argtypes = [POINTER(cairo_scaled_font_t), POINTER(cairo_user_data_key_t)]

# /usr/include/cairo/cairo.h:1416
cairo_scaled_font_set_user_data = _lib.cairo_scaled_font_set_user_data
cairo_scaled_font_set_user_data.restype = cairo_status_t
cairo_scaled_font_set_user_data.argtypes = [POINTER(cairo_scaled_font_t), POINTER(cairo_user_data_key_t), POINTER(None), cairo_destroy_func_t]

# /usr/include/cairo/cairo.h:1422
cairo_scaled_font_extents = _lib.cairo_scaled_font_extents
cairo_scaled_font_extents.restype = None
cairo_scaled_font_extents.argtypes = [POINTER(cairo_scaled_font_t), POINTER(cairo_font_extents_t)]

# /usr/include/cairo/cairo.h:1426
cairo_scaled_font_text_extents = _lib.cairo_scaled_font_text_extents
cairo_scaled_font_text_extents.restype = None
cairo_scaled_font_text_extents.argtypes = [POINTER(cairo_scaled_font_t), c_char_p, POINTER(cairo_text_extents_t)]

# /usr/include/cairo/cairo.h:1431
cairo_scaled_font_glyph_extents = _lib.cairo_scaled_font_glyph_extents
cairo_scaled_font_glyph_extents.restype = None
cairo_scaled_font_glyph_extents.argtypes = [POINTER(cairo_scaled_font_t), POINTER(cairo_glyph_t), c_int, POINTER(cairo_text_extents_t)]

# /usr/include/cairo/cairo.h:1436
cairo_scaled_font_get_font_face = _lib.cairo_scaled_font_get_font_face
cairo_scaled_font_get_font_face.restype = POINTER(cairo_font_face_t)
cairo_scaled_font_get_font_face.argtypes = [POINTER(cairo_scaled_font_t)]

# /usr/include/cairo/cairo.h:1440
cairo_scaled_font_get_font_matrix = _lib.cairo_scaled_font_get_font_matrix
cairo_scaled_font_get_font_matrix.restype = None
cairo_scaled_font_get_font_matrix.argtypes = [POINTER(cairo_scaled_font_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:1444
cairo_scaled_font_get_ctm = _lib.cairo_scaled_font_get_ctm
cairo_scaled_font_get_ctm.restype = None
cairo_scaled_font_get_ctm.argtypes = [POINTER(cairo_scaled_font_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:1448
cairo_scaled_font_get_font_options = _lib.cairo_scaled_font_get_font_options
cairo_scaled_font_get_font_options.restype = None
cairo_scaled_font_get_font_options.argtypes = [POINTER(cairo_scaled_font_t), POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1454
cairo_get_operator = _lib.cairo_get_operator
cairo_get_operator.restype = cairo_operator_t
cairo_get_operator.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1456
cairo_get_source = _lib.cairo_get_source
cairo_get_source.restype = POINTER(cairo_pattern_t)
cairo_get_source.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1460
cairo_get_tolerance = _lib.cairo_get_tolerance
cairo_get_tolerance.restype = c_double
cairo_get_tolerance.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1463
cairo_get_antialias = _lib.cairo_get_antialias
cairo_get_antialias.restype = cairo_antialias_t
cairo_get_antialias.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1466
cairo_has_current_point = _lib.cairo_has_current_point
cairo_has_current_point.restype = cairo_bool_t
cairo_has_current_point.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1469
cairo_get_current_point = _lib.cairo_get_current_point
cairo_get_current_point.restype = None
cairo_get_current_point.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:1472
cairo_get_fill_rule = _lib.cairo_get_fill_rule
cairo_get_fill_rule.restype = cairo_fill_rule_t
cairo_get_fill_rule.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1475
cairo_get_line_width = _lib.cairo_get_line_width
cairo_get_line_width.restype = c_double
cairo_get_line_width.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1478
cairo_get_line_cap = _lib.cairo_get_line_cap
cairo_get_line_cap.restype = cairo_line_cap_t
cairo_get_line_cap.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1481
cairo_get_line_join = _lib.cairo_get_line_join
cairo_get_line_join.restype = cairo_line_join_t
cairo_get_line_join.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1484
cairo_get_miter_limit = _lib.cairo_get_miter_limit
cairo_get_miter_limit.restype = c_double
cairo_get_miter_limit.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1487
cairo_get_dash_count = _lib.cairo_get_dash_count
cairo_get_dash_count.restype = c_int
cairo_get_dash_count.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1490
cairo_get_dash = _lib.cairo_get_dash
cairo_get_dash.restype = None
cairo_get_dash.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:1493
cairo_get_matrix = _lib.cairo_get_matrix
cairo_get_matrix.restype = None
cairo_get_matrix.argtypes = [POINTER(cairo_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:1495
cairo_get_target = _lib.cairo_get_target
cairo_get_target.restype = POINTER(cairo_surface_t)
cairo_get_target.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1498
cairo_get_group_target = _lib.cairo_get_group_target
cairo_get_group_target.restype = POINTER(cairo_surface_t)
cairo_get_group_target.argtypes = [POINTER(cairo_t)]

enum__cairo_path_data_type = c_int
CAIRO_PATH_MOVE_TO = 0
CAIRO_PATH_LINE_TO = 1
CAIRO_PATH_CURVE_TO = 2
CAIRO_PATH_CLOSE_PATH = 3
cairo_path_data_type_t = enum__cairo_path_data_type 	# /usr/include/cairo/cairo.h:1517
class struct__cairo_path_data_t(Union):
    __slots__ = [
    ]
struct__cairo_path_data_t._fields_ = [
    ('_opaque_struct', c_int)
]

class struct__cairo_path_data_t(Union):
    __slots__ = [
    ]
struct__cairo_path_data_t._fields_ = [
    ('_opaque_struct', c_int)
]

cairo_path_data_t = struct__cairo_path_data_t 	# /usr/include/cairo/cairo.h:1585
class struct_cairo_path(Structure):
    __slots__ = [
        'status',
        'data',
        'num_data',
    ]
struct_cairo_path._fields_ = [
    ('status', cairo_status_t),
    ('data', POINTER(cairo_path_data_t)),
    ('num_data', c_int),
]

cairo_path_t = struct_cairo_path 	# /usr/include/cairo/cairo.h:1619
# /usr/include/cairo/cairo.h:1621
cairo_copy_path = _lib.cairo_copy_path
cairo_copy_path.restype = POINTER(cairo_path_t)
cairo_copy_path.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1624
cairo_copy_path_flat = _lib.cairo_copy_path_flat
cairo_copy_path_flat.restype = POINTER(cairo_path_t)
cairo_copy_path_flat.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1628
cairo_append_path = _lib.cairo_append_path
cairo_append_path.restype = None
cairo_append_path.argtypes = [POINTER(cairo_t), POINTER(cairo_path_t)]

# /usr/include/cairo/cairo.h:1632
cairo_path_destroy = _lib.cairo_path_destroy
cairo_path_destroy.restype = None
cairo_path_destroy.argtypes = [POINTER(cairo_path_t)]

# /usr/include/cairo/cairo.h:1637
cairo_status = _lib.cairo_status
cairo_status.restype = cairo_status_t
cairo_status.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1639
cairo_status_to_string = _lib.cairo_status_to_string
cairo_status_to_string.restype = c_char_p
cairo_status_to_string.argtypes = [cairo_status_t]

# /usr/include/cairo/cairo.h:1644
cairo_surface_create_similar = _lib.cairo_surface_create_similar
cairo_surface_create_similar.restype = POINTER(cairo_surface_t)
cairo_surface_create_similar.argtypes = [POINTER(cairo_surface_t), cairo_content_t, c_int, c_int]

# /usr/include/cairo/cairo.h:1650
cairo_surface_reference = _lib.cairo_surface_reference
cairo_surface_reference.restype = POINTER(cairo_surface_t)
cairo_surface_reference.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1654
cairo_surface_finish = _lib.cairo_surface_finish
cairo_surface_finish.restype = None
cairo_surface_finish.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1657
cairo_surface_destroy = _lib.cairo_surface_destroy
cairo_surface_destroy.restype = None
cairo_surface_destroy.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1660
cairo_surface_get_reference_count = _lib.cairo_surface_get_reference_count
cairo_surface_get_reference_count.restype = c_uint
cairo_surface_get_reference_count.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1663
cairo_surface_status = _lib.cairo_surface_status
cairo_surface_status.restype = cairo_status_t
cairo_surface_status.argtypes = [POINTER(cairo_surface_t)]

enum__cairo_surface_type = c_int
CAIRO_SURFACE_TYPE_IMAGE = 0
CAIRO_SURFACE_TYPE_PDF = 1
CAIRO_SURFACE_TYPE_PS = 2
CAIRO_SURFACE_TYPE_XLIB = 3
CAIRO_SURFACE_TYPE_XCB = 4
CAIRO_SURFACE_TYPE_GLITZ = 5
CAIRO_SURFACE_TYPE_QUARTZ = 6
CAIRO_SURFACE_TYPE_WIN32 = 7
CAIRO_SURFACE_TYPE_BEOS = 8
CAIRO_SURFACE_TYPE_DIRECTFB = 9
CAIRO_SURFACE_TYPE_SVG = 10
CAIRO_SURFACE_TYPE_OS2 = 11
CAIRO_SURFACE_TYPE_WIN32_PRINTING = 12
CAIRO_SURFACE_TYPE_QUARTZ_IMAGE = 13
cairo_surface_type_t = enum__cairo_surface_type 	# /usr/include/cairo/cairo.h:1720
# /usr/include/cairo/cairo.h:1723
cairo_surface_get_type = _lib.cairo_surface_get_type
cairo_surface_get_type.restype = cairo_surface_type_t
cairo_surface_get_type.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1726
cairo_surface_get_content = _lib.cairo_surface_get_content
cairo_surface_get_content.restype = cairo_content_t
cairo_surface_get_content.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1731
cairo_surface_write_to_png = _lib.cairo_surface_write_to_png
cairo_surface_write_to_png.restype = cairo_status_t
cairo_surface_write_to_png.argtypes = [POINTER(cairo_surface_t), c_char_p]

# /usr/include/cairo/cairo.h:1735
cairo_surface_write_to_png_stream = _lib.cairo_surface_write_to_png_stream
cairo_surface_write_to_png_stream.restype = cairo_status_t
cairo_surface_write_to_png_stream.argtypes = [POINTER(cairo_surface_t), cairo_write_func_t, POINTER(None)]

# /usr/include/cairo/cairo.h:1741
cairo_surface_get_user_data = _lib.cairo_surface_get_user_data
cairo_surface_get_user_data.restype = POINTER(c_void)
cairo_surface_get_user_data.argtypes = [POINTER(cairo_surface_t), POINTER(cairo_user_data_key_t)]

# /usr/include/cairo/cairo.h:1746
cairo_surface_set_user_data = _lib.cairo_surface_set_user_data
cairo_surface_set_user_data.restype = cairo_status_t
cairo_surface_set_user_data.argtypes = [POINTER(cairo_surface_t), POINTER(cairo_user_data_key_t), POINTER(None), cairo_destroy_func_t]

# /usr/include/cairo/cairo.h:1752
cairo_surface_get_font_options = _lib.cairo_surface_get_font_options
cairo_surface_get_font_options.restype = None
cairo_surface_get_font_options.argtypes = [POINTER(cairo_surface_t), POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1756
cairo_surface_flush = _lib.cairo_surface_flush
cairo_surface_flush.restype = None
cairo_surface_flush.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1759
cairo_surface_mark_dirty = _lib.cairo_surface_mark_dirty
cairo_surface_mark_dirty.restype = None
cairo_surface_mark_dirty.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1762
cairo_surface_mark_dirty_rectangle = _lib.cairo_surface_mark_dirty_rectangle
cairo_surface_mark_dirty_rectangle.restype = None
cairo_surface_mark_dirty_rectangle.argtypes = [POINTER(cairo_surface_t), c_int, c_int, c_int, c_int]

# /usr/include/cairo/cairo.h:1769
cairo_surface_set_device_offset = _lib.cairo_surface_set_device_offset
cairo_surface_set_device_offset.restype = None
cairo_surface_set_device_offset.argtypes = [POINTER(cairo_surface_t), c_double, c_double]

# /usr/include/cairo/cairo.h:1774
cairo_surface_get_device_offset = _lib.cairo_surface_get_device_offset
cairo_surface_get_device_offset.restype = None
cairo_surface_get_device_offset.argtypes = [POINTER(cairo_surface_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:1779
cairo_surface_set_fallback_resolution = _lib.cairo_surface_set_fallback_resolution
cairo_surface_set_fallback_resolution.restype = None
cairo_surface_set_fallback_resolution.argtypes = [POINTER(cairo_surface_t), c_double, c_double]

# /usr/include/cairo/cairo.h:1784
cairo_surface_copy_page = _lib.cairo_surface_copy_page
cairo_surface_copy_page.restype = None
cairo_surface_copy_page.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1787
cairo_surface_show_page = _lib.cairo_surface_show_page
cairo_surface_show_page.restype = None
cairo_surface_show_page.argtypes = [POINTER(cairo_surface_t)]

enum__cairo_format = c_int
CAIRO_FORMAT_ARGB32 = 0
CAIRO_FORMAT_RGB24 = 1
CAIRO_FORMAT_A8 = 2
CAIRO_FORMAT_A1 = 3
cairo_format_t = enum__cairo_format 	# /usr/include/cairo/cairo.h:1827
# /usr/include/cairo/cairo.h:1829
cairo_image_surface_create = _lib.cairo_image_surface_create
cairo_image_surface_create.restype = POINTER(cairo_surface_t)
cairo_image_surface_create.argtypes = [cairo_format_t, c_int, c_int]

# /usr/include/cairo/cairo.h:1835
cairo_format_stride_for_width = _lib.cairo_format_stride_for_width
cairo_format_stride_for_width.restype = c_int
cairo_format_stride_for_width.argtypes = [cairo_format_t, c_int]

# /usr/include/cairo/cairo.h:1838
cairo_image_surface_create_for_data = _lib.cairo_image_surface_create_for_data
cairo_image_surface_create_for_data.restype = POINTER(cairo_surface_t)
cairo_image_surface_create_for_data.argtypes = [POINTER(c_ubyte), cairo_format_t, c_int, c_int, c_int]

# /usr/include/cairo/cairo.h:1845
cairo_image_surface_get_data = _lib.cairo_image_surface_get_data
cairo_image_surface_get_data.restype = POINTER(c_ubyte)
cairo_image_surface_get_data.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1849
cairo_image_surface_get_format = _lib.cairo_image_surface_get_format
cairo_image_surface_get_format.restype = cairo_format_t
cairo_image_surface_get_format.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1852
cairo_image_surface_get_width = _lib.cairo_image_surface_get_width
cairo_image_surface_get_width.restype = c_int
cairo_image_surface_get_width.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1855
cairo_image_surface_get_height = _lib.cairo_image_surface_get_height
cairo_image_surface_get_height.restype = c_int
cairo_image_surface_get_height.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1858
cairo_image_surface_get_stride = _lib.cairo_image_surface_get_stride
cairo_image_surface_get_stride.restype = c_int
cairo_image_surface_get_stride.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1862
cairo_image_surface_create_from_png = _lib.cairo_image_surface_create_from_png
cairo_image_surface_create_from_png.restype = POINTER(cairo_surface_t)
cairo_image_surface_create_from_png.argtypes = [c_char_p]

# /usr/include/cairo/cairo.h:1865
cairo_image_surface_create_from_png_stream = _lib.cairo_image_surface_create_from_png_stream
cairo_image_surface_create_from_png_stream.restype = POINTER(cairo_surface_t)
cairo_image_surface_create_from_png_stream.argtypes = [cairo_read_func_t, POINTER(None)]

# /usr/include/cairo/cairo.h:1873
cairo_pattern_create_rgb = _lib.cairo_pattern_create_rgb
cairo_pattern_create_rgb.restype = POINTER(cairo_pattern_t)
cairo_pattern_create_rgb.argtypes = [c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:1876
cairo_pattern_create_rgba = _lib.cairo_pattern_create_rgba
cairo_pattern_create_rgba.restype = POINTER(cairo_pattern_t)
cairo_pattern_create_rgba.argtypes = [c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:1880
cairo_pattern_create_for_surface = _lib.cairo_pattern_create_for_surface
cairo_pattern_create_for_surface.restype = POINTER(cairo_pattern_t)
cairo_pattern_create_for_surface.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1883
cairo_pattern_create_linear = _lib.cairo_pattern_create_linear
cairo_pattern_create_linear.restype = POINTER(cairo_pattern_t)
cairo_pattern_create_linear.argtypes = [c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:1887
cairo_pattern_create_radial = _lib.cairo_pattern_create_radial
cairo_pattern_create_radial.restype = POINTER(cairo_pattern_t)
cairo_pattern_create_radial.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:1891
cairo_pattern_reference = _lib.cairo_pattern_reference
cairo_pattern_reference.restype = POINTER(cairo_pattern_t)
cairo_pattern_reference.argtypes = [POINTER(cairo_pattern_t)]

# /usr/include/cairo/cairo.h:1895
cairo_pattern_destroy = _lib.cairo_pattern_destroy
cairo_pattern_destroy.restype = None
cairo_pattern_destroy.argtypes = [POINTER(cairo_pattern_t)]

# /usr/include/cairo/cairo.h:1898
cairo_pattern_get_reference_count = _lib.cairo_pattern_get_reference_count
cairo_pattern_get_reference_count.restype = c_uint
cairo_pattern_get_reference_count.argtypes = [POINTER(cairo_pattern_t)]

# /usr/include/cairo/cairo.h:1901
cairo_pattern_status = _lib.cairo_pattern_status
cairo_pattern_status.restype = cairo_status_t
cairo_pattern_status.argtypes = [POINTER(cairo_pattern_t)]

# /usr/include/cairo/cairo.h:1903
cairo_pattern_get_user_data = _lib.cairo_pattern_get_user_data
cairo_pattern_get_user_data.restype = POINTER(c_void)
cairo_pattern_get_user_data.argtypes = [POINTER(cairo_pattern_t), POINTER(cairo_user_data_key_t)]

# /usr/include/cairo/cairo.h:1908
cairo_pattern_set_user_data = _lib.cairo_pattern_set_user_data
cairo_pattern_set_user_data.restype = cairo_status_t
cairo_pattern_set_user_data.argtypes = [POINTER(cairo_pattern_t), POINTER(cairo_user_data_key_t), POINTER(None), cairo_destroy_func_t]

enum__cairo_pattern_type = c_int
CAIRO_PATTERN_TYPE_SOLID = 0
CAIRO_PATTERN_TYPE_SURFACE = 1
CAIRO_PATTERN_TYPE_LINEAR = 2
CAIRO_PATTERN_TYPE_RADIAL = 3
cairo_pattern_type_t = enum__cairo_pattern_type 	# /usr/include/cairo/cairo.h:1948
# /usr/include/cairo/cairo.h:1951
cairo_pattern_get_type = _lib.cairo_pattern_get_type
cairo_pattern_get_type.restype = cairo_pattern_type_t
cairo_pattern_get_type.argtypes = [POINTER(cairo_pattern_t)]

# /usr/include/cairo/cairo.h:1954
cairo_pattern_add_color_stop_rgb = _lib.cairo_pattern_add_color_stop_rgb
cairo_pattern_add_color_stop_rgb.restype = None
cairo_pattern_add_color_stop_rgb.argtypes = [POINTER(cairo_pattern_t), c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:1959
cairo_pattern_add_color_stop_rgba = _lib.cairo_pattern_add_color_stop_rgba
cairo_pattern_add_color_stop_rgba.restype = None
cairo_pattern_add_color_stop_rgba.argtypes = [POINTER(cairo_pattern_t), c_double, c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:1965
cairo_pattern_set_matrix = _lib.cairo_pattern_set_matrix
cairo_pattern_set_matrix.restype = None
cairo_pattern_set_matrix.argtypes = [POINTER(cairo_pattern_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:1969
cairo_pattern_get_matrix = _lib.cairo_pattern_get_matrix
cairo_pattern_get_matrix.restype = None
cairo_pattern_get_matrix.argtypes = [POINTER(cairo_pattern_t), POINTER(cairo_matrix_t)]

enum__cairo_extend = c_int
CAIRO_EXTEND_NONE = 0
CAIRO_EXTEND_REPEAT = 1
CAIRO_EXTEND_REFLECT = 2
CAIRO_EXTEND_PAD = 3
cairo_extend_t = enum__cairo_extend 	# /usr/include/cairo/cairo.h:1998
# /usr/include/cairo/cairo.h:2001
cairo_pattern_set_extend = _lib.cairo_pattern_set_extend
cairo_pattern_set_extend.restype = None
cairo_pattern_set_extend.argtypes = [POINTER(cairo_pattern_t), cairo_extend_t]

# /usr/include/cairo/cairo.h:2004
cairo_pattern_get_extend = _lib.cairo_pattern_get_extend
cairo_pattern_get_extend.restype = cairo_extend_t
cairo_pattern_get_extend.argtypes = [POINTER(cairo_pattern_t)]

enum__cairo_filter = c_int
CAIRO_FILTER_FAST = 0
CAIRO_FILTER_GOOD = 1
CAIRO_FILTER_BEST = 2
CAIRO_FILTER_NEAREST = 3
CAIRO_FILTER_BILINEAR = 4
CAIRO_FILTER_GAUSSIAN = 5
cairo_filter_t = enum__cairo_filter 	# /usr/include/cairo/cairo.h:2031
# /usr/include/cairo/cairo.h:2034
cairo_pattern_set_filter = _lib.cairo_pattern_set_filter
cairo_pattern_set_filter.restype = None
cairo_pattern_set_filter.argtypes = [POINTER(cairo_pattern_t), cairo_filter_t]

# /usr/include/cairo/cairo.h:2037
cairo_pattern_get_filter = _lib.cairo_pattern_get_filter
cairo_pattern_get_filter.restype = cairo_filter_t
cairo_pattern_get_filter.argtypes = [POINTER(cairo_pattern_t)]

# /usr/include/cairo/cairo.h:2040
cairo_pattern_get_rgba = _lib.cairo_pattern_get_rgba
cairo_pattern_get_rgba.restype = cairo_status_t
cairo_pattern_get_rgba.argtypes = [POINTER(cairo_pattern_t), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:2045
cairo_pattern_get_surface = _lib.cairo_pattern_get_surface
cairo_pattern_get_surface.restype = cairo_status_t
cairo_pattern_get_surface.argtypes = [POINTER(cairo_pattern_t), POINTER(POINTER(cairo_surface_t))]

# /usr/include/cairo/cairo.h:2050
cairo_pattern_get_color_stop_rgba = _lib.cairo_pattern_get_color_stop_rgba
cairo_pattern_get_color_stop_rgba.restype = cairo_status_t
cairo_pattern_get_color_stop_rgba.argtypes = [POINTER(cairo_pattern_t), c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:2056
cairo_pattern_get_color_stop_count = _lib.cairo_pattern_get_color_stop_count
cairo_pattern_get_color_stop_count.restype = cairo_status_t
cairo_pattern_get_color_stop_count.argtypes = [POINTER(cairo_pattern_t), POINTER(c_int)]

# /usr/include/cairo/cairo.h:2060
cairo_pattern_get_linear_points = _lib.cairo_pattern_get_linear_points
cairo_pattern_get_linear_points.restype = cairo_status_t
cairo_pattern_get_linear_points.argtypes = [POINTER(cairo_pattern_t), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:2065
cairo_pattern_get_radial_circles = _lib.cairo_pattern_get_radial_circles
cairo_pattern_get_radial_circles.restype = cairo_status_t
cairo_pattern_get_radial_circles.argtypes = [POINTER(cairo_pattern_t), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:2072
cairo_matrix_init = _lib.cairo_matrix_init
cairo_matrix_init.restype = None
cairo_matrix_init.argtypes = [POINTER(cairo_matrix_t), c_double, c_double, c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:2078
cairo_matrix_init_identity = _lib.cairo_matrix_init_identity
cairo_matrix_init_identity.restype = None
cairo_matrix_init_identity.argtypes = [POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:2081
cairo_matrix_init_translate = _lib.cairo_matrix_init_translate
cairo_matrix_init_translate.restype = None
cairo_matrix_init_translate.argtypes = [POINTER(cairo_matrix_t), c_double, c_double]

# /usr/include/cairo/cairo.h:2085
cairo_matrix_init_scale = _lib.cairo_matrix_init_scale
cairo_matrix_init_scale.restype = None
cairo_matrix_init_scale.argtypes = [POINTER(cairo_matrix_t), c_double, c_double]

# /usr/include/cairo/cairo.h:2089
cairo_matrix_init_rotate = _lib.cairo_matrix_init_rotate
cairo_matrix_init_rotate.restype = None
cairo_matrix_init_rotate.argtypes = [POINTER(cairo_matrix_t), c_double]

# /usr/include/cairo/cairo.h:2093
cairo_matrix_translate = _lib.cairo_matrix_translate
cairo_matrix_translate.restype = None
cairo_matrix_translate.argtypes = [POINTER(cairo_matrix_t), c_double, c_double]

# /usr/include/cairo/cairo.h:2096
cairo_matrix_scale = _lib.cairo_matrix_scale
cairo_matrix_scale.restype = None
cairo_matrix_scale.argtypes = [POINTER(cairo_matrix_t), c_double, c_double]

# /usr/include/cairo/cairo.h:2099
cairo_matrix_rotate = _lib.cairo_matrix_rotate
cairo_matrix_rotate.restype = None
cairo_matrix_rotate.argtypes = [POINTER(cairo_matrix_t), c_double]

# /usr/include/cairo/cairo.h:2102
cairo_matrix_invert = _lib.cairo_matrix_invert
cairo_matrix_invert.restype = cairo_status_t
cairo_matrix_invert.argtypes = [POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:2105
cairo_matrix_multiply = _lib.cairo_matrix_multiply
cairo_matrix_multiply.restype = None
cairo_matrix_multiply.argtypes = [POINTER(cairo_matrix_t), POINTER(cairo_matrix_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:2110
cairo_matrix_transform_distance = _lib.cairo_matrix_transform_distance
cairo_matrix_transform_distance.restype = None
cairo_matrix_transform_distance.argtypes = [POINTER(cairo_matrix_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:2114
cairo_matrix_transform_point = _lib.cairo_matrix_transform_point
cairo_matrix_transform_point.restype = None
cairo_matrix_transform_point.argtypes = [POINTER(cairo_matrix_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:2119
cairo_debug_reset_static_data = _lib.cairo_debug_reset_static_data
cairo_debug_reset_static_data.restype = None
cairo_debug_reset_static_data.argtypes = []

Display = pyglet.gl.glx.Display
Drawable = pyglet.window.xlib.xlib.Drawable
Visual = pyglet.gl.glx.Visual
# /usr/include/cairo/cairo-xlib.h:4116
cairo_xlib_surface_create = _lib.cairo_xlib_surface_create
cairo_xlib_surface_create.restype = POINTER(cairo_surface_t)
cairo_xlib_surface_create.argtypes = [POINTER(Display), Drawable, POINTER(Visual), c_int, c_int]

Pixmap = pyglet.gl.glx.Pixmap
Screen = pyglet.window.xlib.xlib.Screen
# /usr/include/cairo/cairo-xlib.h:4123
cairo_xlib_surface_create_for_bitmap = _lib.cairo_xlib_surface_create_for_bitmap
cairo_xlib_surface_create_for_bitmap.restype = POINTER(cairo_surface_t)
cairo_xlib_surface_create_for_bitmap.argtypes = [POINTER(Display), Pixmap, POINTER(Screen), c_int, c_int]

# /usr/include/cairo/cairo-xlib.h:4131
cairo_xlib_surface_set_size = _lib.cairo_xlib_surface_set_size
cairo_xlib_surface_set_size.restype = None
cairo_xlib_surface_set_size.argtypes = [POINTER(cairo_surface_t), c_int, c_int]

# /usr/include/cairo/cairo-xlib.h:4136
cairo_xlib_surface_set_drawable = _lib.cairo_xlib_surface_set_drawable
cairo_xlib_surface_set_drawable.restype = None
cairo_xlib_surface_set_drawable.argtypes = [POINTER(cairo_surface_t), Drawable, c_int, c_int]

# /usr/include/cairo/cairo-xlib.h:4141
cairo_xlib_surface_get_display = _lib.cairo_xlib_surface_get_display
cairo_xlib_surface_get_display.restype = POINTER(Display)
cairo_xlib_surface_get_display.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo-xlib.h:4145
cairo_xlib_surface_get_drawable = _lib.cairo_xlib_surface_get_drawable
cairo_xlib_surface_get_drawable.restype = Drawable
cairo_xlib_surface_get_drawable.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo-xlib.h:4147
cairo_xlib_surface_get_screen = _lib.cairo_xlib_surface_get_screen
cairo_xlib_surface_get_screen.restype = POINTER(Screen)
cairo_xlib_surface_get_screen.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo-xlib.h:4150
cairo_xlib_surface_get_visual = _lib.cairo_xlib_surface_get_visual
cairo_xlib_surface_get_visual.restype = POINTER(Visual)
cairo_xlib_surface_get_visual.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo-xlib.h:4154
cairo_xlib_surface_get_depth = _lib.cairo_xlib_surface_get_depth
cairo_xlib_surface_get_depth.restype = c_int
cairo_xlib_surface_get_depth.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo-xlib.h:4157
cairo_xlib_surface_get_width = _lib.cairo_xlib_surface_get_width
cairo_xlib_surface_get_width.restype = c_int
cairo_xlib_surface_get_width.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo-xlib.h:4160
cairo_xlib_surface_get_height = _lib.cairo_xlib_surface_get_height
cairo_xlib_surface_get_height.restype = c_int
cairo_xlib_surface_get_height.argtypes = [POINTER(cairo_surface_t)]

class struct__FcPattern(Structure):
    __slots__ = [
    ]
struct__FcPattern._fields_ = [
    ('_opaque_struct', c_int)
]

class struct__FcPattern(Structure):
    __slots__ = [
    ]
struct__FcPattern._fields_ = [
    ('_opaque_struct', c_int)
]

FcPattern = struct__FcPattern 	# /usr/include/fontconfig/fontconfig.h:224
# /usr/include/cairo/cairo-ft.h:4220
cairo_ft_font_face_create_for_pattern = _lib.cairo_ft_font_face_create_for_pattern
cairo_ft_font_face_create_for_pattern.restype = POINTER(cairo_font_face_t)
cairo_ft_font_face_create_for_pattern.argtypes = [POINTER(FcPattern)]

# /usr/include/cairo/cairo-ft.h:4224
cairo_ft_font_options_substitute = _lib.cairo_ft_font_options_substitute
cairo_ft_font_options_substitute.restype = None
cairo_ft_font_options_substitute.argtypes = [POINTER(cairo_font_options_t), POINTER(FcPattern)]

# /usr/include/cairo/cairo-ft.h:4235
cairo_ft_scaled_font_unlock_face = _lib.cairo_ft_scaled_font_unlock_face
cairo_ft_scaled_font_unlock_face.restype = None
cairo_ft_scaled_font_unlock_face.argtypes = [POINTER(cairo_scaled_font_t)]


__all__ = ['CAIRO_VERSION', 'cairo_version', 'cairo_version_string',
'cairo_bool_t', 'cairo_t', 'cairo_surface_t', 'cairo_matrix_t',
'cairo_pattern_t', 'cairo_destroy_func_t', 'cairo_user_data_key_t',
'cairo_status_t', 'CAIRO_STATUS_SUCCESS', 'CAIRO_STATUS_NO_MEMORY',
'CAIRO_STATUS_INVALID_RESTORE', 'CAIRO_STATUS_INVALID_POP_GROUP',
'CAIRO_STATUS_NO_CURRENT_POINT', 'CAIRO_STATUS_INVALID_MATRIX',
'CAIRO_STATUS_INVALID_STATUS', 'CAIRO_STATUS_NULL_POINTER',
'CAIRO_STATUS_INVALID_STRING', 'CAIRO_STATUS_INVALID_PATH_DATA',
'CAIRO_STATUS_READ_ERROR', 'CAIRO_STATUS_WRITE_ERROR',
'CAIRO_STATUS_SURFACE_FINISHED', 'CAIRO_STATUS_SURFACE_TYPE_MISMATCH',
'CAIRO_STATUS_PATTERN_TYPE_MISMATCH', 'CAIRO_STATUS_INVALID_CONTENT',
'CAIRO_STATUS_INVALID_FORMAT', 'CAIRO_STATUS_INVALID_VISUAL',
'CAIRO_STATUS_FILE_NOT_FOUND', 'CAIRO_STATUS_INVALID_DASH',
'CAIRO_STATUS_INVALID_DSC_COMMENT', 'CAIRO_STATUS_INVALID_INDEX',
'CAIRO_STATUS_CLIP_NOT_REPRESENTABLE', 'CAIRO_STATUS_TEMP_FILE_ERROR',
'CAIRO_STATUS_INVALID_STRIDE', 'cairo_content_t', 'CAIRO_CONTENT_COLOR',
'CAIRO_CONTENT_ALPHA', 'CAIRO_CONTENT_COLOR_ALPHA', 'cairo_write_func_t',
'cairo_read_func_t', 'cairo_create', 'cairo_reference', 'cairo_destroy',
'cairo_get_reference_count', 'cairo_get_user_data', 'cairo_set_user_data',
'cairo_save', 'cairo_restore', 'cairo_push_group',
'cairo_push_group_with_content', 'cairo_pop_group',
'cairo_pop_group_to_source', 'cairo_operator_t', 'CAIRO_OPERATOR_CLEAR',
'CAIRO_OPERATOR_SOURCE', 'CAIRO_OPERATOR_OVER', 'CAIRO_OPERATOR_IN',
'CAIRO_OPERATOR_OUT', 'CAIRO_OPERATOR_ATOP', 'CAIRO_OPERATOR_DEST',
'CAIRO_OPERATOR_DEST_OVER', 'CAIRO_OPERATOR_DEST_IN',
'CAIRO_OPERATOR_DEST_OUT', 'CAIRO_OPERATOR_DEST_ATOP', 'CAIRO_OPERATOR_XOR',
'CAIRO_OPERATOR_ADD', 'CAIRO_OPERATOR_SATURATE', 'cairo_set_operator',
'cairo_set_source', 'cairo_set_source_rgb', 'cairo_set_source_rgba',
'cairo_set_source_surface', 'cairo_set_tolerance', 'cairo_antialias_t',
'CAIRO_ANTIALIAS_DEFAULT', 'CAIRO_ANTIALIAS_NONE', 'CAIRO_ANTIALIAS_GRAY',
'CAIRO_ANTIALIAS_SUBPIXEL', 'cairo_set_antialias', 'cairo_fill_rule_t',
'CAIRO_FILL_RULE_WINDING', 'CAIRO_FILL_RULE_EVEN_ODD', 'cairo_set_fill_rule',
'cairo_set_line_width', 'cairo_line_cap_t', 'CAIRO_LINE_CAP_BUTT',
'CAIRO_LINE_CAP_ROUND', 'CAIRO_LINE_CAP_SQUARE', 'cairo_set_line_cap',
'cairo_line_join_t', 'CAIRO_LINE_JOIN_MITER', 'CAIRO_LINE_JOIN_ROUND',
'CAIRO_LINE_JOIN_BEVEL', 'cairo_set_line_join', 'cairo_set_dash',
'cairo_set_miter_limit', 'cairo_translate', 'cairo_scale', 'cairo_rotate',
'cairo_transform', 'cairo_set_matrix', 'cairo_identity_matrix',
'cairo_user_to_device', 'cairo_user_to_device_distance',
'cairo_device_to_user', 'cairo_device_to_user_distance', 'cairo_new_path',
'cairo_move_to', 'cairo_new_sub_path', 'cairo_line_to', 'cairo_curve_to',
'cairo_arc', 'cairo_arc_negative', 'cairo_rel_move_to', 'cairo_rel_line_to',
'cairo_rel_curve_to', 'cairo_rectangle', 'cairo_close_path',
'cairo_path_extents', 'cairo_paint', 'cairo_paint_with_alpha', 'cairo_mask',
'cairo_mask_surface', 'cairo_stroke', 'cairo_stroke_preserve', 'cairo_fill',
'cairo_fill_preserve', 'cairo_copy_page', 'cairo_show_page',
'cairo_in_stroke', 'cairo_in_fill', 'cairo_stroke_extents',
'cairo_fill_extents', 'cairo_reset_clip', 'cairo_clip', 'cairo_clip_preserve',
'cairo_clip_extents', 'cairo_rectangle_t', 'cairo_rectangle_list_t',
'cairo_copy_clip_rectangle_list', 'cairo_rectangle_list_destroy',
'cairo_scaled_font_t', 'cairo_font_face_t', 'cairo_glyph_t',
'cairo_text_extents_t', 'cairo_font_extents_t', 'cairo_font_slant_t',
'CAIRO_FONT_SLANT_NORMAL', 'CAIRO_FONT_SLANT_ITALIC',
'CAIRO_FONT_SLANT_OBLIQUE', 'cairo_font_weight_t', 'CAIRO_FONT_WEIGHT_NORMAL',
'CAIRO_FONT_WEIGHT_BOLD', 'cairo_subpixel_order_t',
'CAIRO_SUBPIXEL_ORDER_DEFAULT', 'CAIRO_SUBPIXEL_ORDER_RGB',
'CAIRO_SUBPIXEL_ORDER_BGR', 'CAIRO_SUBPIXEL_ORDER_VRGB',
'CAIRO_SUBPIXEL_ORDER_VBGR', 'cairo_hint_style_t', 'CAIRO_HINT_STYLE_DEFAULT',
'CAIRO_HINT_STYLE_NONE', 'CAIRO_HINT_STYLE_SLIGHT', 'CAIRO_HINT_STYLE_MEDIUM',
'CAIRO_HINT_STYLE_FULL', 'cairo_hint_metrics_t', 'CAIRO_HINT_METRICS_DEFAULT',
'CAIRO_HINT_METRICS_OFF', 'CAIRO_HINT_METRICS_ON', 'cairo_font_options_t',
'cairo_font_options_create', 'cairo_font_options_copy',
'cairo_font_options_destroy', 'cairo_font_options_status',
'cairo_font_options_merge', 'cairo_font_options_equal',
'cairo_font_options_hash', 'cairo_font_options_set_antialias',
'cairo_font_options_get_antialias', 'cairo_font_options_set_subpixel_order',
'cairo_font_options_get_subpixel_order', 'cairo_font_options_set_hint_style',
'cairo_font_options_get_hint_style', 'cairo_font_options_set_hint_metrics',
'cairo_font_options_get_hint_metrics', 'cairo_select_font_face',
'cairo_set_font_size', 'cairo_set_font_matrix', 'cairo_get_font_matrix',
'cairo_set_font_options', 'cairo_get_font_options', 'cairo_set_font_face',
'cairo_get_font_face', 'cairo_set_scaled_font', 'cairo_get_scaled_font',
'cairo_show_text', 'cairo_show_glyphs', 'cairo_text_path', 'cairo_glyph_path',
'cairo_text_extents', 'cairo_glyph_extents', 'cairo_font_extents',
'cairo_font_face_reference', 'cairo_font_face_destroy',
'cairo_font_face_get_reference_count', 'cairo_font_face_status',
'cairo_font_type_t', 'CAIRO_FONT_TYPE_TOY', 'CAIRO_FONT_TYPE_FT',
'CAIRO_FONT_TYPE_WIN32', 'CAIRO_FONT_TYPE_QUARTZ', 'cairo_font_face_get_type',
'cairo_font_face_get_user_data', 'cairo_font_face_set_user_data',
'cairo_scaled_font_create', 'cairo_scaled_font_reference',
'cairo_scaled_font_destroy', 'cairo_scaled_font_get_reference_count',
'cairo_scaled_font_status', 'cairo_scaled_font_get_type',
'cairo_scaled_font_get_user_data', 'cairo_scaled_font_set_user_data',
'cairo_scaled_font_extents', 'cairo_scaled_font_text_extents',
'cairo_scaled_font_glyph_extents', 'cairo_scaled_font_get_font_face',
'cairo_scaled_font_get_font_matrix', 'cairo_scaled_font_get_ctm',
'cairo_scaled_font_get_font_options', 'cairo_get_operator',
'cairo_get_source', 'cairo_get_tolerance', 'cairo_get_antialias',
'cairo_has_current_point', 'cairo_get_current_point', 'cairo_get_fill_rule',
'cairo_get_line_width', 'cairo_get_line_cap', 'cairo_get_line_join',
'cairo_get_miter_limit', 'cairo_get_dash_count', 'cairo_get_dash',
'cairo_get_matrix', 'cairo_get_target', 'cairo_get_group_target',
'cairo_path_data_type_t', 'CAIRO_PATH_MOVE_TO', 'CAIRO_PATH_LINE_TO',
'CAIRO_PATH_CURVE_TO', 'CAIRO_PATH_CLOSE_PATH', 'cairo_path_data_t',
'cairo_path_t', 'cairo_copy_path', 'cairo_copy_path_flat',
'cairo_append_path', 'cairo_path_destroy', 'cairo_status',
'cairo_status_to_string', 'cairo_surface_create_similar',
'cairo_surface_reference', 'cairo_surface_finish', 'cairo_surface_destroy',
'cairo_surface_get_reference_count', 'cairo_surface_status',
'cairo_surface_type_t', 'CAIRO_SURFACE_TYPE_IMAGE', 'CAIRO_SURFACE_TYPE_PDF',
'CAIRO_SURFACE_TYPE_PS', 'CAIRO_SURFACE_TYPE_XLIB', 'CAIRO_SURFACE_TYPE_XCB',
'CAIRO_SURFACE_TYPE_GLITZ', 'CAIRO_SURFACE_TYPE_QUARTZ',
'CAIRO_SURFACE_TYPE_WIN32', 'CAIRO_SURFACE_TYPE_BEOS',
'CAIRO_SURFACE_TYPE_DIRECTFB', 'CAIRO_SURFACE_TYPE_SVG',
'CAIRO_SURFACE_TYPE_OS2', 'CAIRO_SURFACE_TYPE_WIN32_PRINTING',
'CAIRO_SURFACE_TYPE_QUARTZ_IMAGE', 'cairo_surface_get_type',
'cairo_surface_get_content', 'cairo_surface_write_to_png',
'cairo_surface_write_to_png_stream', 'cairo_surface_get_user_data',
'cairo_surface_set_user_data', 'cairo_surface_get_font_options',
'cairo_surface_flush', 'cairo_surface_mark_dirty',
'cairo_surface_mark_dirty_rectangle', 'cairo_surface_set_device_offset',
'cairo_surface_get_device_offset', 'cairo_surface_set_fallback_resolution',
'cairo_surface_copy_page', 'cairo_surface_show_page', 'cairo_format_t',
'CAIRO_FORMAT_ARGB32', 'CAIRO_FORMAT_RGB24', 'CAIRO_FORMAT_A8',
'CAIRO_FORMAT_A1', 'cairo_image_surface_create',
'cairo_format_stride_for_width', 'cairo_image_surface_create_for_data',
'cairo_image_surface_get_data', 'cairo_image_surface_get_format',
'cairo_image_surface_get_width', 'cairo_image_surface_get_height',
'cairo_image_surface_get_stride', 'cairo_image_surface_create_from_png',
'cairo_image_surface_create_from_png_stream', 'cairo_pattern_create_rgb',
'cairo_pattern_create_rgba', 'cairo_pattern_create_for_surface',
'cairo_pattern_create_linear', 'cairo_pattern_create_radial',
'cairo_pattern_reference', 'cairo_pattern_destroy',
'cairo_pattern_get_reference_count', 'cairo_pattern_status',
'cairo_pattern_get_user_data', 'cairo_pattern_set_user_data',
'cairo_pattern_type_t', 'CAIRO_PATTERN_TYPE_SOLID',
'CAIRO_PATTERN_TYPE_SURFACE', 'CAIRO_PATTERN_TYPE_LINEAR',
'CAIRO_PATTERN_TYPE_RADIAL', 'cairo_pattern_get_type',
'cairo_pattern_add_color_stop_rgb', 'cairo_pattern_add_color_stop_rgba',
'cairo_pattern_set_matrix', 'cairo_pattern_get_matrix', 'cairo_extend_t',
'CAIRO_EXTEND_NONE', 'CAIRO_EXTEND_REPEAT', 'CAIRO_EXTEND_REFLECT',
'CAIRO_EXTEND_PAD', 'cairo_pattern_set_extend', 'cairo_pattern_get_extend',
'cairo_filter_t', 'CAIRO_FILTER_FAST', 'CAIRO_FILTER_GOOD',
'CAIRO_FILTER_BEST', 'CAIRO_FILTER_NEAREST', 'CAIRO_FILTER_BILINEAR',
'CAIRO_FILTER_GAUSSIAN', 'cairo_pattern_set_filter',
'cairo_pattern_get_filter', 'cairo_pattern_get_rgba',
'cairo_pattern_get_surface', 'cairo_pattern_get_color_stop_rgba',
'cairo_pattern_get_color_stop_count', 'cairo_pattern_get_linear_points',
'cairo_pattern_get_radial_circles', 'cairo_matrix_init',
'cairo_matrix_init_identity', 'cairo_matrix_init_translate',
'cairo_matrix_init_scale', 'cairo_matrix_init_rotate',
'cairo_matrix_translate', 'cairo_matrix_scale', 'cairo_matrix_rotate',
'cairo_matrix_invert', 'cairo_matrix_multiply',
'cairo_matrix_transform_distance', 'cairo_matrix_transform_point',
'cairo_debug_reset_static_data', 'cairo_xlib_surface_create',
'cairo_xlib_surface_create_for_bitmap', 'cairo_xlib_surface_set_size',
'cairo_xlib_surface_set_drawable', 'cairo_xlib_surface_get_display',
'cairo_xlib_surface_get_drawable', 'cairo_xlib_surface_get_screen',
'cairo_xlib_surface_get_visual', 'cairo_xlib_surface_get_depth',
'cairo_xlib_surface_get_width', 'cairo_xlib_surface_get_height',
'cairo_ft_font_face_create_for_pattern', 'cairo_ft_font_options_substitute',
'cairo_ft_scaled_font_unlock_face']
