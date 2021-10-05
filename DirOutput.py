from ij import IJ
from ij import WindowManager
from ij.measure import ResultsTable

import BatchDirectionality_
# Required modified plugin to be installed
from ij import WindowManager
from ij.measure import ResultsTable
import math

# Instantiate plugin
dnlty = BatchDirectionality_()
 
# Set fields and settings
imp = WindowManager.getCurrentImage()
dnlty.setImagePlus(imp)
dnlty.setMethod(BatchDirectionality_.AnalysisMethod.FOURIER_COMPONENTS)
dnlty.setBinNumber(181)
dnlty.setBinStart(0)
dnlty.setBuildOrientationMapFlag(False) # No orientation map needed, only data as output

# Do calculation
dnlty.computeHistograms()
dnlty.fitHistograms()
 
# Display fit analysis (could be removed)
data_frame = dnlty.displayFitAnalysis()
data_frame.setVisible(False)
 
# Get the fit params and put them in a results table
fitParams = dnlty.getFitParameters()
rt = ResultsTable()
index = 1;

anl = dnlty.getFitAnalysis()

center=math.degrees(anl[0][0])# Conversion to degrees needed
std=math.degrees(anl[0][1])
# anl[0][2] # no use for amount
gof=(anl[0][3])
ImgFolder = imp.getOriginalFileInfo().directory
FileName = imp.getTitle()

textfile = open(ImgFolder+"output.txt", "a")
# Opens text file in defined subdirectory
textfile.write('\n'+FileName+','+str(center)+','+str(std)+','+str(gof))
# Writes new line of comma-separated values
textfile.close()
