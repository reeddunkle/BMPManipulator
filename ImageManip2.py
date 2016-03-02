__author__ = 'reed'

import argparse
import binascii

def horizontal_flip(new_hex, offset_val, row_len, padding, height):
    padding_count = 0
    
    #Grabs all of the stuff at the start of the file that isn't related to the pixel placement
    #and adds it to our output string. This is one of the biggest weaknesses of my program.
    temp_hex = new_hex[0:offset_val]

    for runs in range(height):

        #Captures the original file's code, one row at a time.
        og_row = new_hex[offset_val + (row_len*runs) + padding_count:(offset_val + (row_len*(runs+1)) + padding_count)]



        #Works through each character in the 6-character hexidecimal pixel in that original row, 
        #restructuring it for the new output string.
        #The tricky part is that you want to keep the 6-character hex color in the same order for each pixel --
        #that's how you keep the color the same -- but you need to invert the order of the colors for each row.
        
        #This was the first function I made, and I think my code is the crudest here. I change my expression in the
        #later functions, and I think it is better polished as I go. I left this expression in the code to offer
        #comparison.
        for i in range(1,(len(og_row)/6)+1):
            temp_hex += og_row[len(og_row)-i*6:len(og_row)-(i-1)*6]

        #Adds in padding '0's found in my BMPs. Another big weakness.
        for a in range(padding):
            temp_hex += "0"

        padding_count += padding

    #This is an unnecessary step, I know. But it helps me keep the process consistent.
    new_hex = temp_hex

    return new_hex

def vertical_flip(new_hex, offset_val, row_len, padding, width, height):
    temp_hex = new_hex[0:offset_val]
    padding_count = padding * (height - 1)
    start_pos = offset_val + padding_count + ((width + height) * 6)

    for runs in range(height):
        og_row = new_hex[start_pos:start_pos + row_len + padding]
        start_pos -= padding + (width * 6)
        temp_hex += og_row

    new_hex = temp_hex

    return new_hex

def rotate_90(new_hex, offset_val, padding, width, height):
    new_hex = swap_dimensions(new_hex)
    new_padding = get_padding(new_hex)

    temp_hex = new_hex[0:offset_val]

    for runs in range(1,width+1):
        start_pos = offset_val + ((width - runs) * 6)

        for x in range(height):
            og_row = new_hex[start_pos:start_pos + 6]
            print start_pos # For debugging
            temp_hex += og_row


            start_pos += padding + (width * 6)

        for i in range(new_padding):
            temp_hex += "0"

    new_hex = temp_hex

    return new_hex

def rotate_270(new_hex, offset_val, padding, width, height):
    new_hex = swap_dimensions(new_hex)
    new_padding = get_padding(new_hex)

    temp_hex = new_hex[0:offset_val]

    for runs in range(width):
        start_pos = offset_val + (((((height - 1) * width) * 6) + (runs * 6)) + ((height - 1) * padding))

        for x in range(height):
            og_row = new_hex[start_pos:start_pos + 6]
            print start_pos # For debugging
            temp_hex += og_row

            start_pos -= padding + (width * 6)

        for i in range(new_padding):
            temp_hex += "0"

    new_hex = temp_hex

    return new_hex

#Originally I was only working with squares. I built this in to move into rectangles.
def swap_dimensions(bmp_hex):
    temp_hex = bmp_hex[0:36]
    width = bmp_hex[36:44]
    height = bmp_hex[44:52]
    new_width = height
    new_height = width
    temp_hex += new_width + new_height
    temp_hex += bmp_hex[52:len(bmp_hex)]

    new_hex = temp_hex

    return new_hex


def get_offset(bmp_hex):
    offset = bmp_hex[20:28]

    return hex2dec(offset) * 2

def get_width(bmp_hex):
    width = bmp_hex[36:44]

    return hex2dec(width)

def get_height(bmp_hex):
    height = bmp_hex[44:52]

    return hex2dec(height)

def get_padding(bmp_hex):
    width = get_width(bmp_hex)

    padding = width % 4

    return padding * 2

#I built this so that I can do my own conversions. It was also a fun project, albeit simple once you understand it.
def hex2dec(str_hex):
    temp = 0
    total = 0
    tens = True

    for i in range(0,len(str_hex)):
        if i % 2 == 0:
            tens = True
        else:
            tens = False

        if str_hex[i] == "a":
            temp = 10
        elif str_hex[i] == "b":
            temp = 11
        elif str_hex[i] == "c":
            temp = 12
        elif str_hex[i] == "d":
            temp = 13
        elif str_hex[i] == "e":
            temp = 14
        elif str_hex[i] == "f":
            temp = 15
        else:
            temp = int(str_hex[i])

        if tens == True:
            total += temp * 16
        else:
            total += temp

    return total











#Begin the commandline parser. This is all pretty crude, and somewhat arbitrary. It serves the purpose though, and gave
#me a big of practice using a parser.



parser = argparse.ArgumentParser(description='Manipulate an image.')

parser.add_argument('-f', dest='infile', required=True, help='followed by the image file path')
parser.add_argument('-o', dest='outfile', required=True, help='followed by the output file path')
parser.add_argument('--hflip', dest='hflip', action="store_true", help='if set, flips the image horizontally')
parser.add_argument('--vflip', dest='vflip', action="store_true", help='if set, flips the image vertically')
parser.add_argument('--90', dest='ninety', action="store_true", help='if set, rotates the image 90 degrees')
parser.add_argument('--180', dest='oneeighty', action="store_true", help='if set, rotates the image 180 degrees')
parser.add_argument('--270', dest='twoseventy', action="store_true", help='if set, rotates the image 270 degrees')

args = parser.parse_args()

with open(args.infile, 'rb') as inputfile:
    filecontent = inputfile.read()

inputfile.close()

og_hex = binascii.hexlify(filecontent)
temp_hex = og_hex
new_hex = temp_hex
og_row = ""

offset_val = get_offset(og_hex)

width = get_width(og_hex)
row_len = width * 6


height = get_height(og_hex)

padding = get_padding(og_hex)

if args.hflip:
    new_hex = horizontal_flip(new_hex, offset_val, row_len, padding, height)

if args.vflip:
    new_hex = vertical_flip(new_hex, offset_val, row_len, padding, width, height)

if args.oneeighty:
    new_hex = horizontal_flip(new_hex, offset_val, row_len, padding, height)
    new_hex = vertical_flip(new_hex, offset_val, row_len, padding, width, height)

if args.ninety:
    new_hex = rotate_90(new_hex, offset_val, padding, width, height)

if args.twoseventy:
    new_hex = rotate_270(new_hex, offset_val, padding, width, height)

# This to check that the functions work. All for debugging purposes.
print "Offset value:"
print offset_val
print "Width:"
print width
print "Height:"
print height
print "Padding:"
print padding


print og_hex
print
print new_hex

new_bin = binascii.unhexlify(new_hex)
outfile = open(args.outfile,'wb')

outfile.write(new_bin)
outfile.close()

