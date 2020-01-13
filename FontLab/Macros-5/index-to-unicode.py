#FLM: Index to Unicode
# Create unicode based on index

font = fl.font
glyphs = font.glyphs

# Set unicode to be index
for i in range(32, len(glyphs)):
    glyphs[i].unicode = i
    font.GenerateNames()		

fl.UpdateFont()
