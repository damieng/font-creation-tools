#FLM: Set my metadata
# Set all my personal metadata
import os

font = fl.font

# Base name on filename
fontname = os.path.basename(os.path.splitext(font.file_name)[0])

# Set all standard names
font.family_name = fontname
font.font_name = fontname.replace(' ','') + "-" + font.style_name
font.full_name = fontname + " " + font.style_name
font.menu_name = fontname
font.apple_name = fontname

# Personalized creator info
font.designer = "Damien Guard"
font.designer_url = "https://damieng.com"
font.year = 2019
font.copyright = "Copyright 2019 Damien Guard."
font.vendor = "ENVY"
font.vendor_url = "https://envytech.com"

# Set OpenType & TrueType data
font.pref_family_name = fontname
font.pref_style_name = font.style_name
font.mac_compatible = font.full_name
font.tt_u_id = font.designer.replace(' ','') + ": " + font.full_name + ": " + str(font.year)

fl.UpdateFont()
