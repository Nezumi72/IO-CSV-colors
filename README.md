# IO-CSV-colors
Blender 2.9x Example import color data (rgb, hex, hsv) from csv file; create icon swatches; perform operations based on selected color data.

# Installation
Download code as .zip file
Install from:
Blender
  Edit Menu
  Preferences
  Addons

# Enabling Addon
Given this is intended as an example the addon is located in the Testing section.

# Usage
  # Import options
  This comes with an example packaged csv data file.
  Use the sniff operator to read the Header and 1st row of data.
  Use the drop down selections to map an incoming data header to a relevant data type (RGB, Hex, HSV, generic description, etc)
  The scaling field is used to allow incoming data of a non float (0.0 - 1.0) range to be adjusted for Blender's expected (0.0 - 1.0) range.
  Once you have mapped the incoming data fields (at least 1 unique field and one color type) you can load the csv data file.
  
  # Export options
  Boolean flags allow limiting data to be exported.
  Currently only data that was loaded from the original file may be exported, no calculated data is preserved.
  
  # Save images
  This section allows for generating thumbnail icon images based on loaded color data. Icon size field has a soft limit of 32 pixels but any size of at least 1 pixel will create custom icon color swatches available to be seen in sample color.
  
  # Sample color
  A dynamic list of loaded color data will be shown as color list displaying description field if available if not displayed name will be based on the ID_Name field. If a corresponding image has not been saved to disk the list will only display the text. Once an image has been saved to disk (save images section above) a preview icon will automatically be generated and added to a preview collection dictionary. 
  Apply color to obj viewport color:
    Sample operator does not require icon image only loaded data. To view this effect in the 3d Viewport you must be in solid mode on viewport shader settings and in the viewport shader options set color to object. Alternatively you may see the color swatch update in the properties panel; object tab; viewport display section.
  Color Details:
    Quick text reference of loaded data for selected color.
  Palette colors:
    Unfinished example of creating a palette from loaded data.
    Name a palette then press enter to create the named palette.
    Add selected to palette:
      Sample operator does not require icon image only loaded data.
      Once a palette is created you can add colors from loaded data to it.
      A display of loaded colors will be shown below.
      Once a color is loaded it can be dragged to any other color data field available.
      As mentioned above this is unfinished example of working with a pallete while not requiring an image mode context.
