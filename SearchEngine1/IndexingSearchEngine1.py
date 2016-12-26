from SearchEngine1 import RGBhistogram
import argparse
#cPickle is used to dump our index to disk 
import cPickle
#glob is used to get the path of the images we are going to index 
import glob
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())

index ={}
desc =RGBhistogram([8,8,8])

#this says that for all the imagePath in the particular datapath 
#and adding a PNG file extension after to take all the images only 
for imagePath in glob.glob(args["dataset"+"/*.png"]):
	#extract the unique image ID (i.e the filename)
	k= imagePath[imagePath.rfind("/")+1:]

	# load the image, describe it using our RGB histogram
	# descriptor, and update the index
	image = cv2.imread(imagePath)
	features = desc.describe(image)
	index[k] = features

f= open(args["index"],"w")
f.write(cPickle.dumps(index))
f.close()
