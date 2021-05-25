// First application of Directionality

run("32-bit");
mainFolder = getDirectory("image");
//print(mainFolder);

source = getTitle();
//run("Directionality", "method=[Fourier components] nbins=91 histogram_start=-90 histogram_end=90 build");
run("BatchDirectionality ", "method=[Fourier components] nbins=91 histogram_start=-90 histogram_end=90 build");

// saving Orientation map
mapTitle = getTitle();

if (File.exists(mainFolder +"Output")) {
      } else {
      	File.makeDirectory(mainFolder +"Output");
      }
saveAs(mainFolder + "Output/" + mapTitle);
//print("Saved");

// getting Difference image
imageCalculator("Subtract create 32-bit", source, mapTitle);
run("Invert");

// saving Difference image
diffTitle = getTitle();
saveAs("png", mainFolder + "Output/" + diffTitle);

// Creating text file with result data
output_path = mainFolder + "Output/" + "output.txt";

if (File.exists(output_path)) {
	}else {
		header = "Filename,Direction,Dispersion,GoF";
		File.saveString(header, output_path);
           }
// Run python script
//showMessageWithCancel("title","message");
run("DirOutput ");
run("Close All");
print("Script finished for "+source);
