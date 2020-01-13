# font-creation-tools

Various simple tools and scripts for making fonts things in FontLab.

## CodePages

- [cpm-plus-amstrad-sinclair.cpg](./FontLab/CodePages/cpm-plus-amstrad-sinclair.cpg) - CP/M+ codepage for Amstrad & Sinclair Spectrum +3 machines

## Macros for FontLab 5.0

Copy these into your FontLab 5 Macros folder - e.g. `%userprofile%/Documents/FontLab/Studio 5/Macros` and restart FontLab Studio to see them listed in the Macros drop-down.

RoboFont not required!

- [audit-to-notes.py](./FontLab/Macros-5/audit-to-notes.py) - Audit the entire font and place issues into the notes for each glyph
- [index-to-unicode.py](./FontLab/Macros-5/index-to-unicode.py) - Creates unicode and names based on the import index number
- [menu-command-constants.py](./FontLab/Macros-5/menu-command-constants.py) - Constants for use with `fl.CallCommand` direct from `Studio5.exe`
- [remove-empty-glyphs.py](./FontLab/Macros-5/remove-empty-glyphs.py) - Removes all empty glyphs from a font
- [set-8x8-metrics.py](./FontLab/Macros-5/set-8x8-metrics.py) - Set the metrics for nice 8x8 pixel fonts at 8px on Windows
- [set-my-metadata.py](./FontLab/Macros-5/set-my-metadata.py) - One-click to set all my personal metadata based on file name (you'll want to modify this one)
