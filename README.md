# Directionality for batch mode

This is a modified version of the Fiji plugin Directionality (https://imagej.net/plugins/directionality) originally by Jean-Yves Tinevez, forked from https://github.com/fiji/Directionality and adapted for batch analysis of entire folders of images.
All graphical output that pops out as Java windows with JFrame has been disabled.


The java source code available at https://github.com/adamtywoniak/directionality-batch/blob/master/BatchDirectionality_.java needs to be compiled in ImageJ (see https://imagej.nih.gov/ij/docs/menus/plugins.html#compile for reference).

 <h2>Use</h2>
The plugin needs to be installed manually and can then be called from a script.
An example Python script that gets Gaussian fit parameters using the *getFitAnalysis()* function and exports them as comma separated values into a text file is available at https://github.com/adamtywoniak/directionality-batch/blob/master/DirOutput.py 

* Results from *getFitParameters()* can still be displayed or accessed if needed, just as in the original version.
