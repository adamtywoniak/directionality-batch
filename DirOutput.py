from fiji.analyze.directionality import Directionality_
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
dnlty = Directionality_()
 
# Set fields and settings
imp = WindowManager.getCurrentImage()
dnlty.setImagePlus(imp)
dnlty.setMethod(Directionality_.AnalysisMethod.FOURIER_COMPONENTS)
dnlty.setBinNumber(181)
dnlty.setBinStart(0)
dnlty.setBuildOrientationMapFlag(False) # No orientation map

# Do calculation
dnlty.computeHistograms()
dnlty.fitHistograms()
 
# Display plot frame
plot_frame = dnlty.plotResults()
plot_frame.setVisible(False)
 
# Display fit analysis
data_frame = dnlty.displayFitAnalysis()
data_frame.setVisible(False)
 
# Display results table
# table = dnlty.displayResultsTable()
# table.show("Directionality histograms")
 
# Get the fit params and put them in a results table
fitParams = dnlty.getFitParameters()
rt = ResultsTable()
index = 1;

# print(type(fitParams[0][:]))

for param in fitParams:
    rt.incrementCounter()
    #rt.addLabel(imp.getStack().getShortSliceLabel(index))
    rt.addValue('a', param[0])
    rt.addValue('b', param[1])
    rt.addValue('c', param[2])
    rt.addValue('d', param[3])
    index = index + 1;
 
rt.show('Fit param for y = a + (b-a)*exp(-(x-c)*(x-c)/(2*d*d)')

# print('fitParams:')
# print(fitParams[0][2])
# print(math.degrees(fitParams[0][2]))

# print('Goodness')
# getGoodness = dnlty.getGoodnessOfFit()
# print(getGoodness[0])

print('Analysis')
anl = dnlty.getFitAnalysis()
#analysis[ 0 ] = center;
#analysis[ 1 ] = std;
#analysis[ 2 ] = amount;
#analysis[ 3 ] = gof[ i ];
#print(type(anl))
# See description above
print(anl[0][0]) #in rad
print(anl[0][1]) #in rad
print(anl[0][2])
print(anl[0][3])
#result=anl[0] #not used

with open('output.txt', 'a') as f:

output_path = getDirectory("image")+"output.txt";
header = "Filename,Direction,Dispersion,GoF";