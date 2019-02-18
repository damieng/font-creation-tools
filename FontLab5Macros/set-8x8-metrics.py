#FLM: Set 8x8 monospace metrics
# Set the metrics for nice 8x8 pixel fonts at 8px on Windows

font = fl.font

# Typical font characteristics
pixels_descender = 1 # Pixels for the descender
pixels_lower = 5     # Lower-case x-height (acxo)
pixels_upper = 7     # Upper-case height (ABCD)
pixels_ascender = pixels_upper

# Pixel metrics
pixel_size_x = 100
pixel_size_y = 100
pixels_wide = 8
pixels_high = 8

# Calculations
height = pixel_size_y * 8
width = pixel_size_x * 8

# Set the font metrics
font.upm = height
font.ascender[0] = pixels_ascender * pixel_size_y
font.descender[0] = 0 - (pixels_descender * pixel_size_y)
font.cap_height[0] = pixels_upper * pixel_size_y
font.x_height[0] = pixels_lower * pixel_size_y
font.default_width[0] = width
font.underline_position = font.descender[0]
font.underline_thickness = pixel_size_y
font.is_fixed_pitch = 1

for glyph in fl.font.glyphs:
    glyph.width = width

fl.UpdateFont()
