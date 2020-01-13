# font-creation-tools

Various simple tools and scripts for making fonts.

## FontLab/CodePages

- [cpm-plus-amstrad-sinclair.cpg](./FontLab/CpdePages/cpm-plus-amstrad-sinclair.cpg) - CP/M+ codepage for Amstrad & Sinclair Spectrum +3 machines

## FontLab5Macros

Copy these into your FontLab 5 Macros folder - e.g. `%userprofile%/Documents/FontLab/Studio 5/Macros` and restart FontLab Studio to see them listed in the Macros drop-down.

RoboFont not required!

- [audit-to-notes.py](./FontLab5Macros/audit-to-notes.py) - Audit the entire font and place issues into the notes for each glyph
- [index-to-unicode.py](./FontLab5Macros/index-to-unicode.py) - Creates unicode and names based on the import index number
- [menu-command-constants.py](./FontLab5Macros/menu-command-constants.py) - Constants for use with `fl.CallCommand` direct from `Studio5.exe`
- [remove-empty-glyphs.py](./FontLab5Macros/remove-empty-glyphs.py) - Removes all empty glyphs from a font
- [set-8x8-metrics.py](./FontLab5Macros/set-8x8-metrics.py) - Set the metrics for nice 8x8 pixel fonts at 8px on Windows
- [set-my-metadata.py](./FontLab5Macros/set-my-metadata.py) - One-click to set all my personal metadata based on file name (you'll want to modify this one)
