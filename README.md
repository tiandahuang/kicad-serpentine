# kicad-serpentine 🐍
 
kicad 7.0 extension for generating serpentine traces

**note: developed and tested in kicad 7.0. definitely doesn't work in previous versions and i have no clue if it'll work in future versions**

![Parameters](paramguide.bmp)

serpentine edge cuts and traces will likely end on an uneven x,y coordinate.
to connect to these edge cuts and traces, make sure snapping is enabled:

**Preferences → PCB Editor → Editing Options → Magnetic Points**

* Snap to pads: When creating tracks (or Always)
* Snap to tracks: When creating tracks (or Always)
* Snap to graphics: Always

_sorry in advance if something breaks_ 😔
