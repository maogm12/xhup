# -*- coding:utf-8 -*-
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

output = open('flypy.txt', 'w')
output.write(''';fcitx Version 0x03 Table file
KeyCode=abcdefghijklmnopqrstuvwxyz;',./
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

for code in sorted(mb):
    for order in sorted(mb[code]):
        output.write('%s %s\n'%(code, mb[code][order]))

# close file
bdxh.close()
output.close()

os.system("txt2mb flypy.txt flypy.mb")
