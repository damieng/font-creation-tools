# font-creation-tools

Various simple tools and scripts for making fonts.

## FontLab5Macros

Copy these into your FontLab 5 Macros folder - e.g. `%userprofile%/Documents/FontLab/Studio 5/Macros` and restart FontLab Studio to see them listed in the Macros drop-down.

RoboFont not required!

- [audit-to-notes.py](https://github.com/damieng/font-creation-tools/blob/master/FontLab5Macros/audit-to-notes.py) - Audit the entire font and place issues into the notes for each glyph
- [menu-command-constants.py](https://github.com/damieng/font-creation-tools/blob/master/FontLab5Macros/menu-command-constants.py) - Constants for use with `fl.CallCommand` direct from `Studio5.exe`
- [remove-empty-glyphs.py](https://github.com/damieng/font-creation-tools/blob/master/FontLab5Macros/remove-empty-glyphs.py) - Removes all empty glyphs from a font
- [set-8x8-metrics.py](https://github.com/damieng/font-creation-tools/blob/master/FontLab5Macros/set-8x8-metrics.py) - Set the metrics for nice 8x8 pixel fonts at 8px on Windows
- [set-my-metadata.py](https://github.com/damieng/font-creation-tools/blob/master/FontLab5Macros/set-my-metadata.py) - One-click to set all my personal metadata based on file name (you'll want to modify this one)