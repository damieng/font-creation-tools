#FLM: Set my metadata
# Set all my personal metadata
import os

font = fl.font

# Base name on filename
fontName = os.path.basename(os.path.splitext(font.file_name)[0]).strip()
nameParts = fontName.split()
isBold = True if "Bold" in nameParts else False
isItalic = True if "Italic" in nameParts else False

styleNames = []
font.font_style = 0
font.weight = "Regular"
font.weight_code = 400

if isBold:
    styleNames.append("Bold")
    nameParts.remove("Bold")
    font.font_style += 32
    font.weight = "Bold"
    font.weight_code = 700

if isItalic:
    styleNames.append("Italic")
    nameParts.remove("Italic")
    font.font_style += 1

if styleNames:
    styleName = " ".join(styleNames)
else:
    styleName = "Regular"

familyName = " ".join(nameParts)
fullName = familyName + " " + styleName

# Set all standard names
font.family_name = familyName
font.style_name = styleName
font.font_name = familyName.replace(' ', '') + "-" + styleName.replace(' ', '')
font.full_name = fullName
font.menu_name = familyName
font.apple_name = fullName if isBold or isItalic else familyName

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
