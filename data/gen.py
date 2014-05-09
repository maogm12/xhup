# -*- coding:utf-8 -*-
import json

bdxh = open("bdxh.txt")

code2ch = {}
ch2code = {}

# date,date,time
bdxh.readline()
bdxh.readline()
bdxh.readline()

line = bdxh.readline()
cont = ''
code = ''
ch = ''
temp = {}

def addcodebych(key, value):
    if ch2code.get(key, False) is False:
        ch2code[key] = []
    
    if value not in ch2code[key]:
        ch2code[key].append(value)

while line:
    # read a line and remove the leading number and the line-break at the end.
    line = bdxh.readline().rstrip('\n')
    if ',' in line:
        cont = line.split(',')[1]
    else:
        continue
    
    # get the code and character
    if '=' in cont:
        (code, ch) = cont.split('=')[:2]
    else:
        continue
    
    # code2ch is a Trie.
    temp = code2ch
    for num in code:
        if temp.get(num, False) is False:
            temp[num] = {}
        temp = temp[num]
    if temp.get("value", False) is False:
        temp["value"] = []
    # duplicate codes
    temp['value'].append(ch)
    
    # this is because 'obxx' print parts of Chinese character, and some parts 
    # does not exist in font, they are be described as something like '比左部'
    # we just not add it into ch2code.
    if code.startswith('ob') and len(ch) > 1:
        continue
    
    # the input file is utf8 encoded.
    ch = ch.decode('utf8')
    
    # ch2code is an one-level dictionary
    addcodebych(ch, code)
    
    # I can not figure out what does the '/xxx' mean output by 'oqxx', ignore it...
    if ch.startswith('/'):
        continue

    for c in ch:
        addcodebych(c, code)

# output json
output = open('code2ch_pretty.json', 'w')
output.write(json.dumps(code2ch, sort_keys=True, indent=4));
output = open('ch2code_pretty.json', 'w')
output.write(json.dumps(ch2code, sort_keys=True, indent=4));

output = open('code2ch.js', 'w')
output.write("var code2ch=");
output.write(json.dumps(code2ch, separators=(',', ':')));
output.write(";");
output = open('ch2code.js', 'w')
output.write("var ch2code=");
output.write(json.dumps(ch2code, separators=(',', ':')));
output.write(";");

# close file
bdxh.close()
output.close()