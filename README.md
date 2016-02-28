# BMPManipulator
Simple bitmap image manipulator project

I made this about a year ago, and it has all of the markings of the newbie I am. First, it doesn't work, not completely. I began with 3x3 pixel images, and worked up to 5x6, 4x3, 4x2, 6x6, and 2x4. They all work. But my code relies on some constants that work for these BMPs, but which aren't true for all BMPs. Primarily this is in my padding variables. <br />
 <br />
That said, my functions do work with these files, which means that my underlying logic works. <br />
 <br />
I have some extra printouts in there for debugging. <br />
 <br />
Parser inputs: <br />
 <br />
-f: required, followed by the image file path <br />
-o: required, followed by the output file path of the new image <br />
--hflip: if set, flips the image horizontally <br />
--vflip: if set, flips the image vertically <br />
--90: if set, rotates the image 90 degrees to the right <br />
--180: if set, rotates the image 180 degrees <br />
--270: if set, rotates the image 270 degrees to the right <br />
 <br />
Example: "python ImageManip2.py -f /imagefile.bmp -o /output.bmp --hflip --90"<br />
This will take in your original imagefile.bmp, flip it horizontally, rotate it 90 degrees to the right, and save the changes in a new output.bmp file.
