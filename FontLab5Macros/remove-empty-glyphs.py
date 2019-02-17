#FLM: Remove empty glyphs
# Removes all empty glyphs from a font

glyphsToKeep = []
glyphs = fl.font.glyphs
for glyph in glyphs:
	if glyph.nodes or glyph.components:
		glyphsToKeep.append(glyph)

removeCount = len(glyphs) - len(glyphsToKeep)
if removeCount == 0:
	print "No empty glyphs to remove."
else:
	glyphs.clean()
	for glyph in glyphsToKeep:
		glyphs.append(glyph)
	print "Removed " + str(removeCount) + " empty glyphs."

fl.UpdateFont()