#FLM: Set my metadata
# Set all my personal metadata
import os

font = fl.font

# Base name on filename
fontName = os.path.basename(os.path.splitext(font.file_name)[0]).strip()
nameParts = fontName.split()

styleNames = []
font.font_style = 0
font.weight = "Regular"
font.weight_code = 400

if "Bold" in nameParts:
    styleNames.append("Bold")
    nameParts.remove("Bold")
    font.font_style += 32
    font.weight = "Bold"
    font.weight_code = 700

if "SemiBold" in nameParts:
    styleNames.append("SemiBold")
    nameParts.remove("SemiBold")
    font.font_style += 32
    font.weight = "SemiBold"
    font.weight_code = 600

if "Italic" in nameParts:
    styleNames.append("Italic")
    nameParts.remove("Italic")
    font.font_style += 1

familyName = " ".join(nameParts)
appleName = familyName
if styleNames:
    styleName = " ".join(styleNames)
    appleName += " " + styleName
else:
    styleName = "Regular"

fullName = familyName + " " + styleName

# Set all standard names
font.family_name = familyName
font.style_name = styleName
font.font_name = familyName.replace(' ', '') + "-" + styleName.replace(' ', '')
font.full_name = fullName
font.menu_name = familyName
font.apple_name = appleName

# Personalized creator info
font.designer = "Damien Guard"
font.designer_url = "https://damieng.com"
font.year = 2019
font.copyright = "Copyright 2019 Damien Guard."
font.vendor = "ENVY"
font.vendor_url = "https://envytech.com"

# Set OpenType & TrueType data
font.pref_family_name = familyName
font.pref_style_name = styleName
font.mac_compatible = fullName
font.tt_u_id = font.designer.replace(' ','') + ": " + fullName + ": " + str(font.year)

fl.UpdateFont()
