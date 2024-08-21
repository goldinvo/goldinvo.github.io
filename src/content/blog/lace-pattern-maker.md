---
title: 'Lace Pattern Maker'
type: 'short'
description: ''
pubDate: '2024-06-29'
featuredImage: '/2024-06-29/screenshot.png'
images:

---
**Lace Pattern Maker** is an interactive canvas designed for making torchon bobbin lace 
patterns. <!--more--> This tool allows you to quickly produce, modify, rescale, and reproduce lace patterns.

Both this post and the pattern tool are currently being improved. Keep an eye out for updates!

[Visit the App](https://goldinvo.com/lace-pattern-maker).

*This post was last updated July 9, 2024*

## Usage
Hover over buttons to see the actions they perform and the keyboard shortcuts associated with them.
 
### Modes
1. Select
    - Box Select
    - Lasso Select
2. Draw
    - Point
    - Line
    - Freehand
3. Pan
4. Erase

### Navigating the Canvas
The scroll wheel allows you to zoom in and out. Use the Pan mode to click and drag
across the canvas.

The `x` and `y` coordinates of your cursor are displayed at the bottom of your toolbar.

### Working with Objects
Use Draw mode to create objects. In this mode, you can draw:
1. Points: Click to plot a point. Will snap to grid if "Snap To Grid" is toggled.
2. Lines: Click once to mark the start of a line, and click again at another location to mark the end of a line.
A line will be filled in between the points and have a red marker. Click away to keep the line, or click
and drag the red marker to create a curve.
3. Freehand lines: Draw as if you would a pen. Each line you draw is converted into a single object. Hold shift to
quickly draw freehand straight lines.

To delete objects, use Erase mode and click on objects to delete them. Alternatively, use the Group Delete
feature on a selection of objects in Select mode.

### Select Mode
Click on an object to select an object. Hold `Shift` and click on other objects
to add/remove them to/from your selection. Click and drag to make a group selection.
The default mode is Box Select. Activate Lasso Select to capture a selection by
drawing a region on the canvas.

With an active selection, you may: 
- Delete
- Cut/Copy/Paste
- Transform (Rotate or Flip Horizontally/Vertically)
All of these actions except for delete require a blue Control Point to be plotted. All
actions will be performed relative to this control point.

Double-click to place your blue control point. A new coordinate display should appear
in the toolbar, showing the coordinate of the control point. You may also remove your 
control point by clicking the close icon on this display.

### Importing and Exporting
Using the "Export/Import" option in the top bar, you can obtain a text representation
of your canvas. Importing a canvas will overwrite your current canvas. 

### Save and Load
I do not recommend relying too much on this feature for storing patterns over time.
Instead, use the Export/Import feature and store them manually on your device.

The save and load feature will write/load your current canvas into your browser's
local storage. There is no concept of separate files, so saving will overwrite 
whatever was last stored! This feature is most useful for making sure you do not 
lose your work during your session, in case you accidentally close your browser 
or want to return to a previous save state.

### Printing
The print form will prompt for the top-left and bottom-right coordinates of your
printing selection, as well as the scaling (in a ratio of grid squares to inches)
to get a print at the correct measurements. Use the cursor position and control 
point coordinate display in the toolbar to get this information. 

To determine the correct scaling, I recommend guessing-and-checking by printing
out patterns and changing the ratio as needed. A ratio of 8 squares to 1 inch 
is a good starting point for no.30 crochet cotton as your thread. Alternatively,
you can manually calculate the desired ratio by measuring an existing pattern
that you have.

## Development
Please contact me (see my About page) if you have any feedback, bug reports, or feature 
requests. Listed below are features that I have planned, somewhat in order of priority.

- Performance improvements
- Bugfixes
    - Import/export is pretty buggy right now
- Copy multiple "motifs" to clipboard, select different motifs to paste to canvas.
- Mobile support
- Backend for user accounts and saving patterns/motifs (likely just as an exercise).