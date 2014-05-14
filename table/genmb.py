# -*- coding:utf-8 -*-
bdxh = open("bdxh.txt")

mb = {}

# date,date,time
bdxh.readline()
bdxh.readline()
bdxh.readline()

line = bdxh.readline()
code = ''
ch = ''
cont = ''

while line:
    # read a line and remove the leading number and the line-break at the end.
    line = bdxh.readline().rstrip('\n\r')
    if ',' in line:
        cont = line.split(',')[1]
    else:
        continue

    # get the code and character
    if '=' in cont:
        (code, ch) = cont.split('=')[:2]
    else:
        continue

    mb[code] = ch

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
    output.write('%s %s\n'%(code, mb[code]))

# close file
bdxh.close()
output.close()
