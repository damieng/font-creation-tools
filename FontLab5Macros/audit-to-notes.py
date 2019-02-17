#FLM: Audit font with notes
# Audit the entire font and place issues into the notes for each glyph

for glyph in fl.font.glyphs:
    audits = glyph.Audit()
    audit_note = ""
    if audits:
        for audit in audits:
            audit_note += str(audit.position) + " " + audit.description + "\r\n\r\n"                
    glyph.note = audit_note

fl.updateFont()