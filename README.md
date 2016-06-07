# BMPManipulator
My first Python project!
*January 17, 2015*

----

## Example

I've got a few small example images you can use.

**Before & After**

<img src=http://i.imgur.com/CatMypQ.png>


## Using it

To do the 90 degree rotation above, on the **fivebysix.bmp** file in the same directory:

```
python ImageManip2.py -f fivebysix.bmp -o rotated.bmp --90
```

- Notice the print statement debugging
- Also notice the **rotated.bmp** file now in the directory

<img src=http://i.imgur.com/LogwFBy.png>

----

### Well

This is pretty darn rough. I made this about two years ago after completing the Codecademy Python course. I had a lot of fun, and learned a thing or two.

Now, I'm glad I've improved enough to recognize the many ways that I should refactor this.

I've only got 3 weeks left at RC. I'm tempted to re-write this to show myself how I've improved. But for now I'm going to spend my time trying to get [Pressure Pong](https://github.com/reeddunkle/pressure_pong) going.

I'll come back to you, BMP Project.

----





In addition to the code being a bit rough on the eyes, it also doesn't work, not completely.








I began with 3x3 pixel images, and worked up to 5x6, 4x3, 4x2, 6x6, and 2x4. These all work. But my code relies on some constants that seem to only work for these BMPs, but which aren't true for all BMPs.

I suspect a lot of this has to do with my padding variables. <br />
 <br />
That said, my functions do work with these files, which means that my underlying logic works. <br />
 <br />
I have some extra printouts in there for debugging. <br />
 <br />
Parser inputs: <br />
 <br />
 
 <img src=http://i.imgur.com/ViD0gb9.png>
 
-f: required, followed by the image file path <br />
-o: required, followed by the output file path of the new image <br />
--hflip: if set, flips the image horizontally <br />
--vflip: if set, flips the image vertically <br />
--90: if set, rotates the image 90 degrees to the right <br />
--180: if set, rotates the image 180 degrees <br />
--270: if set, rotates the image 270 degrees to the right <br />
 <br />

#### Example



