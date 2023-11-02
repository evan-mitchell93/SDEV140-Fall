'''
SDEV 140 Module 3
Evan Mitchell
11/1/2023
'''

#reading and writting from files
#step one is to open the file
# Modes include w - write, r - read, a - append, x - exclusive creation

# Mode w - writting to a file
# will create the file if it does not exist
# and you have permissions in the directory
f = open("writting.txt","w")
f.write("Hello\n")
#always close the files when you are done manipulating them
f.close()

#Mode r - will allow you to read data from the file
f = open("reading.txt","r")
#read() will read all lines of text from the file at once
text = f.read()
print(text)
f.close()

f = open("reading.txt","r")
while 1:
    #readline() will read a single line of text ending with \n
    line = f.readline()
    if line == "":
        break
    print(line)

f.close()

scores = open("scores.txt","r")
sum = 0
lines = scores.readlines()
for line in lines:
    sum += int(line.split(',')[1])

avg = sum/len(lines)
print(f'{sum}, {len(lines)}, {avg}')