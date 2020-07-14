import numpy as np
import cv2  as cv
import argparse

parser = argparse.ArgumentParser(description='Change color of black pixels in an image')
parser.add_argument('input', type=str, help='input file')

args = parser.parse_args()

in_img = args.input
out_img = args.input.split('.')[0] + '_blue.' + args.input.split('.')[1]

bw = cv.imread(in_img)

if bw is None:
	ValueError('Unable to open the file ' + in_img)

for arr in bw:
	for pixel in arr:
#		pixel[0] = np.maximum(pixel[0], 200)
		pixel[2] = np.maximum(pixel[2], 200)

cv.imwrite(out_img, bw)
