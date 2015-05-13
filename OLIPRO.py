__author__ = 'mAyple'
# FILE OPENING WITH CORRECT SYNTAX
import ast
with open("/Users/mAyple/PycharmProjects/drop/1625-Winnovation-62.txt",'r') as f:
    for line in f:
        print ast.literal_eval(line)
        print type(ast.literal_eval(line))
        LIST0 = ast.literal_eval(line)
"""
LIST0[0] = ast.literal_eval(LIST0[0])
LIST0[1] = LIST0[1]
LIST0[2] = ast.literal_eval(LIST0[2])
LIST0[3] = ast.literal_eval(LIST0[3])
LIST0[4] = ast.literal_eval(LIST0[4])
LIST0[5] = ast.literal_eval(LIST0[5])
LIST0[6] = ast.literal_eval(LIST0[6])
LIST0[7] = ast.literal_eval(LIST0[7])
LIST0[8] = ast.literal_eval(LIST0[8])
LIST0[9] = LIST0[9]
LIST0[10] = ast.literal_eval(LIST0[10])
LIST0[11] = ast.literal_eval(LIST0[11])
LIST0[12] = ast.literal_eval(LIST0[12])
LIST0[13] = ast.literal_eval(LIST0[13])
"""
"""
LIST0[14] = ast.literal_eval(LIST0[14])
LIST0[15] = ast.literal_eval(LIST0[15])
"""
# ORDER OF SCORE FUNCTIONS AND SUCH
"""
WITHIN THE FUNCTION:
FIRST THE PART OF THE LIST TO BE EVALED
THEN THE VARIATABLES THAT ARE NEEDED IN THE FUNCTION
THEN EVAL :)
"""

def LAPPIL(X):
    X[0] = ast.literal_eval(X[0])
    X[1] = True
    if X[1] == True:
        return X[1]

    return ast.literal_eval(X[0])

LAPPIL(LIST0)

def EPALS(Y):
    Y[2] = ast.literal_eval(Y[2])

    if Y[1] >= '2':
        return True
    elif isinstance(Y[0],str):
        return 'error'
    else:
        return False

EPALS(LIST0)









"""
REFFAKEARRAY[0] = "TeamNum (string)DNC/INCLUE"
REFFAKEARRAY[1] = "TeamName (string)DNC/INCLUDE"
REFFAKEARRAY[2] = "The stack height of totes that they can reliably stack (int)DC"
REFFAKEARRAY[3] = "The height of totes on which they can reliably place a bin (int)DC"
REFFAKEARRAY[4] = "If they use the chute (bool)DC"
REFFAKEARRAY[5] = "Match number (string)DNC"
REFFAKEARRAY[6] = "If the robot broke during this match (bool)DC"
REFFAKEARRAY[7] = "If the robot can ONLY use an alternate scoring platform (bool)DC"
REFFAKEARRAY[8] = "If the robot can steal bins from the landfill (bool)DC"
REFFAKEARRAY[9] = "Other notes regarding how the robot functions (string)DNC/INCLUDE"
REFFAKEARRAY[10] = "If they throw noodles(bool)"
REFFAKEARRAY[11] = "If they put a noodle in a recycling container(bool)DC"
REFFAKEARRAY[12] = "If they did coopertition (bool)DC"
REFFAKEARRAY[13] = "On how many OTHER TEAMS totes can they place a bin? 0 being they can't (int)DC"
REFFAKEARRAY[14] = "Do they do autonomous? (bool)DC"
REFFAKEARRAY[15] = "Do they do autonomous tote set? (bool)DC"
"""
# GUI

from Tkinter import *

root = Tk()
# Sectors

upframe = Frame(root)
upframe.pack(side=TOP)
downframe = Frame(root)
downframe.pack(side=BOTTOM)
eastframe = Frame(root)
eastframe.pack(side=LEFT)
westframe = Frame(root)
westframe.pack(side=RIGHT)

# Buttons and start of interface
# UPRFAME

input1 = Button(upframe, text="fill 1", fg="black")
input2 = Button(upframe, text="fill 2", fg="black")
input3 = Button(upframe, text="fill 3", fg="black")
input4 = Button(upframe, text="fill 4", fg="black")
input5 = Button(upframe, text="fill 5", fg="black")
input6 = Button(upframe, text="fill 6", fg="black")
input7 = Button(upframe, text="fill 7", fg="black")
# DOWNFRAME

input8 = Button(downframe, text="fill 8", fg="black")
input9 = Button(downframe, text="fill 9", fg="black")
input10 = Button(downframe, text="fill 10", fg="black")
input11 = Button(downframe, text="fill 11", fg="black")
input12 = Button(downframe, text="fill 12", fg="black")
input13 = Button(downframe, text="fill 13", fg="black")
input14 = Button(downframe, text="fill 14", fg="black")

# Packing area
# GRID GOES FROM 0
input1.grid(row=0,)
input2.grid(row=1,)
input3.grid(row=2,)
input4.grid(row=3,)
input5.grid(row=4,)
input6.grid(row=5,)
input7.grid(row=6,)
input8.grid(row=7,)
input9.grid(row=8,)
input10.grid(row=9,)
input11.grid(row=10,)
input12.grid(row=11,)
input13.grid(row=12,)
input14.grid(row=13,)

root.mainloop()