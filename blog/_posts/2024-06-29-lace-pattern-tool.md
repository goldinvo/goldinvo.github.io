---
layout: long-post
tag: other
featured-image: /assets/2024-06-29/screenshot.png
featured: false
---
**Lace Pattern Tool** is an interactive canvas designed for making torchon bobbin lace 
patterns. <!--more--> Digital pattern have the advantages of easy rescaling, 
reproduction, and modification. My objective is to create purpose-built digital tool that is 
easy to learn and free, unlike standard graphic design apps. 

Both this post and the pattern tool are currently being improved. Keep an eye out for updates!

[Visit the App](https://goldinvo.com/lace-pattern-tool).

*This post was last updated July 4, 2024*

## Usage
### Modes
1. Select
2. Draw
    - Point
    - Line
    - Freehand
3. Pan
4. Erase

### Navigating the Canvas
The scroll wheel allows you to zoom in and out. Use the Pan mode to click and drag
across the canvas. Alternatively, hold `Alt/Option` to toggle Pan mode.

The `x` and `y` coordinates of your cursor are displayed at the bottom of your toolbar.

### Working with Objects
Use the Draw mode to create objects. Use the Point tool for your standard pin-hole
markings. Toggle "Snap to Grid" to snap points to grid lines. The Line tool features a control node to create smooth quadratic curves,
which is especially useful for scalloped edges. Finally, use the Freehand tool 
for any other special pattern markings. Holding shift while using the Freehand tool
allows you to quickly draw straight lines.

To delete objects, use the Erase mode. Alternatively, click 'Delete' in Select mode
to delete a highlighted selection.

### Select Mode
Click on an object to select an object. Hold `Shift` and click on other objects
to add/remove them to/from your selection. Click and drag to make a group selection.

With a highlighted selection, you can choose to delete or copy your selection. Copy
and paste requires that you place a "control point." Objects are copy/pasted 
relative to the control point.

Double-click to place your blue control point. A new coordinate display should appear
in the toolbar, showing the coordinate of the control point. You may also remove your 
control point by clicking the 'x' icon. 

### Other features
Using the top toolbar, you can export/import your canvas, or print your pattern.

## Development
Please contact me (see my About page) if you have any feedback, bug reports, or feature 
requests. Listed below are features that I have planned, somewhat in order of priority.

- Performance improvements
- Saving to localStorage
- Bugfixes
    - Import/export is pretty buggy right now
- Styling and UI: Improve aesthetics and usability
- Copy multiple "motifs" to clipboard, select different motifs to paste to canvas.
- Mobile support
- Backend for user accounts and saving patterns/motifs (likely just as an exercise).