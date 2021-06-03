#read file and store in list
file = open("filename.text", "r")
print(file.readlines())
file.close()

# number of days
from datetime import date
date1 = int(input())
date2 = int(input())
dt = abs(date1 - date2)
print(dt)


#dict to json
import json
dict = {"Ramya":"30", "Arun":"25", "Meghana":"24"}
save = json.dumps(dict,indent = 4)
print(save)


# sorting list of dict
lst = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2',
'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print(sorted(lst, key=lambda x:x["color"]))


#len of words
file = open("filename", "r")
words = file.read()
words.replace(",","")
lines = (data.split(words))
print(len(words))
file.close()


#array to binary
from array import *
A1= array('i', [1, 2, 3, 4, 5, 6])
print(A1.tobytes())


#log text
filelog = "C:\Users\A Pallavi\Desktop\demo\text.log"
echolog()
(
    echo "$@"
    echo "$@" >> $filelog

)

echo "text"
echolog "more text"



#import os
number = 0
size = 0
wile true:
    if file <2e+6:
      try:
        file = open("text%d.text"%number, "x")
      except:
          pass
      file = open("text%d.text"%number)
      words = file.read()
      file = open("text%d.text"%number, "w")
    file.write(words)

size = os.start("text%d.text"%number).st_size
if size > 2e+6:
    number += 1
    size = 0



#active ips
import sh
for n in range (0,254):
    ip = "1.0.0.1." + str(n)
    try:
        sh.ping(ip, "-c1",_out"/dev/null" )
            print ip, "ACTIVE"
