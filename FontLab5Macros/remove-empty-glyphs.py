#FLM: Remove empty glyphs
# Removes all empty glyphs from a font

font = fl.font
glyphs = font.glyphs
namesToKeep = [ '.notdef', 'NULL', 'CR', 'space' ]

# Find all the empty glyphs
for glyph in reversed(glyphs):
	if not glyph.nodes and not glyph.components:
		if not glyph.name in namesToKeep:
			del glyphs[font.FindGlyph(glyph.name)]

fl.UpdateFont()