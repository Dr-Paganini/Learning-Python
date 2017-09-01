import random
import sys
import tkinter
import os





#list, tuples, dictionarys,

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

print("My favorite rap song:")
print((rap['Eminem']))
rap['Post Malone'] = 'Congratulations'
print((rap.get('Kendrick Lemar')))

#if statements
if len(rap) <= len(colleges):
    print("Kill me please")

if len(rap) >= len(colleges):
    print("Qing4 sha1 le wo3")





