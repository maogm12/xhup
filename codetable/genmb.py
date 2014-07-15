#!/usr/bin/env python
# encoding: utf-8
import os
bdxh = open("bdxh.txt")

mb = {}

# date,date,time
bdxh.readline()
bdxh.readline()
bdxh.readline()

line = bdxh.readline()
code = ''
ch = ''
order = 1
cont = ''

while line:
    # read a line and remove the leading number and the line-break at the end.
    line = bdxh.readline().rstrip('\n\r')
    if ',' in line:
        (order, cont) = line.split(',')[:2]
    else:
        continue

    # convert order to number
    try:
        order = int(order)
    except ValueError:
        continue

    # get the code and character
    if '=' in cont:
        (code, ch) = cont.split('=')[:2]
    else:
        continue

    if mb.get(code, False) is False:
        mb[code] = {}
    mb[code][order] = ch

# gen mb file for table ime
out_mb = open('flypy.txt', 'w')
out_mb.write(''';fcitx Version 0x03 Table file
KeyCode=abcdefghijklmnopqrstuvwxyz;'/
Length=4
Pinyin=@
PinyinLength=4
Prompt=&
ConstructPhrase=^
[Rule]
e2=p11+p12+p21+p22
e3=p11+p21+p31+p32
a4=p11+p21+p31+n11
[Data]
''')

# gen pysym for pinyin input
out_pySym = open('pySym.mb', 'w')

for code in sorted(mb):
    for order in sorted(mb[code]):
        out_mb.write('%s %s\n'%(code, mb[code][order]))
        out_pySym.write('%s %s\n'%(code, mb[code][order]))

# close file
bdxh.close()
out_mb.close()
out_pySym.close()

os.system("txt2mb flypy.txt flypy.mb")
