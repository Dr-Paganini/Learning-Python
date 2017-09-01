import random
import sys
import tkinter
import os




#Just notes on Python


a = "December 21, 2001"
pi_tuple = "12/21/02"
ti_tuple = pi_tuple
new_tuple = ti_tuple

colleges = ["NYU", "UCLA", "UNT"]
places = ["New York", "California", "North Texas"]
new_list = colleges + places

print("Where you going for College?" 
      "\n\n\n\n""%s""\n\n\n""Where's that?""\n\n\n""%s" % (colleges[0], places[0]))
#tuples
print("When is your birthday? \n" 
      "\n\n\n%s" % new_tuple)


if len(new_tuple) <= 8:
    print("\n\nCool, Bro")

#dictionary
rap = {'Eminem': 'Rap God',
       'Kendrick Lemar': 'Humble',
       'Pink Guy': 'STFU',
       'Post Malone': 'Kill Yourself'}
print((rap.keys()))
print("My favorite rap song:")
print((rap['Eminem']))
rap['Post Malone'] = 'Congratulations'
print((rap.get('Kendrick Lemar')))


#if statements
if len(rap) == len(colleges):
    print("Kill me please")
elif len(rap) > len(colleges):
    print(new_list)
else:
    print("It's wrong my dude")

if (len(rap) <= len(new_list)) and (len(rap) >= len(colleges)):
    print("my pussy stank")
elif (len(new_list) != len(new_tuple)) or (len(rap) != len(new_tuple)):
    print("these are just notes bro so you can look back and ""\n"""
          "know what everything does incase i forget")
elif not(len(colleges) == len(rap)):
    print("die montherfucker")

#looping

for x in range(0, 10):
    print(x, " ", end=" ")
print('\n')
for y in colleges:
    print(y)
print('\n')
for z in [2, 4, 7, 10]:
    print(z)
    print('\n')

random_num = random.randrange(0, 100)

while random_num != 21:
    print(random_num)
    random_num = random.randrange(0, 100)

i = 0

while i <= 0:
    if i % 2 == 0:
        print(i)
    elif i == 9:
        break
    else:
        i += 1          #i +=1 same as( i = i + 1)
        continue

        i += 1



#Functions
number = 0

def add_num(fnum, lnum):
    sum_num = fnum + lnum
    return sumNum


string = add_num(6, 10)






