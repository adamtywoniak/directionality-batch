from ij import IJ
from ij import WindowManager
from ij.measure import ResultsTable

import BatchDirectionality_
#from fiji.analyze.directionality import Directionality_ #now replaced

from ij import WindowManager
from ij.measure import ResultsTable
import math
# from ij import IJ
# from ij.process import ImageConverter

# Conversion to 32-bit grayscale
# imp = IJ.getImage()
# imp2 = imp.duplicate()
# ImageConverter(imp).convertToGray32() 

# Instantiate plugin
#dnlty = Directionality_() #now replaced
dnlty = BatchDirectionality_()
 
# Set fields and settings
imp = WindowManager.getCurrentImage()
dnlty.setImagePlus(imp)
#dnlty.setMethod(Directionality_.AnalysisMethod.FOURIER_COMPONENTS)
dnlty.setMethod(BatchDirectionality_.AnalysisMethod.FOURIER_COMPONENTS)
dnlty.setBinNumber(181)
dnlty.setBinStart(0)
dnlty.setBuildOrientationMapFlag(False) # No orientation map

# Do calculation
dnlty.computeHistograms()
dnlty.fitHistograms()
 
# Display fit analysis
data_frame = dnlty.displayFitAnalysis()
data_frame.setVisible(False)
 
# Get the fit params and put them in a results table
fitParams = dnlty.getFitParameters()
rt = ResultsTable()
index = 1;

# print(type(fitParams[0][:]))

# for param in fitParams:
    #rt.incrementCounter()
    ##rt.addLabel(imp.getStack().getShortSliceLabel(index))
    #rt.addValue('a', param[0])
    #rt.addValue('b', param[1])
    #rt.addValue('c', param[2])
    #rt.addValue('d', param[3])
    #index = index + 1;
 
#rt.show('Fit param for y = a + (b-a)*exp(-(x-c)*(x-c)/(2*d*d)')
#commented out to prevent table display | uncomment for manual analysis

# print('fitParams:')
# print(fitParams[0][2])
# print(math.degrees(fitParams[0][2]))

# print('Goodness')
# getGoodness = dnlty.getGoodnessOfFit()
# print(getGoodness[0])

anl = dnlty.getFitAnalysis()
# Plugin's source code for reference:
#analysis[ 0 ] = center;
#analysis[ 1 ] = std;
#analysis[ 2 ] = amount;
#analysis[ 3 ] = gof[ i ];

center=math.degrees(anl[0][0])#anl stores value in rad
# requires conversion
std=math.degrees(anl[0][1])#rad to deg
# anl[0][2]
 # no use for amount
gof=(anl[0][3])
ImgFolder = imp.getOriginalFileInfo().directory
FileName = imp.getTitle()

textfile = open(ImgFolder+"output.txt", "a")
textfile.write('\n'+FileName+','+str(center)+','+str(std)+','+str(gof))
textfile.close()

#with open(ImgFolder+"output.txt", "a") as text_file:
##header = "Filename,Direction,Dispersion,GoF";
#	text_file.write('\n'+FileName+','+str(center)+','+str(std)+','+str(gof))
#	text_file.close()
