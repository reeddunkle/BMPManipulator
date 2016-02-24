# BMPManipulator
Simple bitmap image manipulator project

I made this about a year ago, and it has all of the markings of the newbie I am. First, it doesn't work, not completely. I began with 3x3 pixel images, and worked up to 5x6, 4x3, 4x2, 6x6, and 2x4. They all work. But my code is uses some constants that apply to those size BMPs, but which aren't true for all BMPs. This is mostly true for my counting of padding.

I have some extra printouts in there for debugging.

To use, in a Linux command line:

-f: required, followed by the image file path
-o: required, followed by the output file path of the new image
--hflip: if set, flips the image horizontally
--vflip: if set, flips the image vertically
--90: if set, rotates the image 90 degrees to the right
--180: if set, rotates the image 180 degrees
--270: if set, rotates the image 270 degrees to the right
