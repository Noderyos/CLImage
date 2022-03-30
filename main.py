#!/usr/bin/env python3
from PIL import Image
import sys
if len(sys.argv) != 3:
    print("Usage : " + sys.argv[0] + " [image] [size]")
    exit(255)
colf = lambda x: "\033[38;5;" + str(x) +"m"
colb = lambda x: "\033[48;5;" + str(x) +"m"
res = "\033[0;0m"


def getcode(a):
    c = (0,95,135,175,215,255)
    u = 100
    v = 0
    for i in range(len(c)):
        if abs(a-c[i]) < u:
            u = abs(a-c[i])
            v = i
    return v



im = Image.open(sys.argv[1])
width = im.size[0]
height = im.size[1]

if width < int(sys.argv[2]):
    print("Image too small")
    exit(255)
if height < int(sys.argv[2]):
    print("Image too small")
    exit(255)

rank = int(height / int(sys.argv[2]))

for i in range(0,height,rank):
    pr = ""
    for j in range(0,width,rank):
        r = im.getpixel((j,i))[0]
        g = im.getpixel((j,i))[1]
        b = im.getpixel((j,i))[2]
        ar = getcode(r)
        ag = getcode(g)
        ab = getcode(b)
        pr += colb(ar*36+ag*6+ab+16) + "  "
    print(pr + res)

