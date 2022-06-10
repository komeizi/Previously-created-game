#import
import functools
import tkinter as tk
from tkinter.constants import X
from typing import Text

#=============================
l = [["?" for _ in range(8)] for _ in range(8)]
chpoin_siro=[]
chpoin_kuro=[]

chpoin_kuro1=[]
chpoin_kuro2=[]
chekmake = []
chekmake2 = []
chekmake2_1=[]
chekmake2_2=[]
chekmake3_1=[]
chekmake3_2=[]
chekmake4_1=[]
chekmake4_2=[]
ccc = 0
dame4_1 =0
ppp = 1
rrr =0
o = 0
japann=0
c=1
cc = 0
cccc=0
aa =1
C=1
siroo=0
kuroo=0
s = "a"










dame = 0
dame2 = 0
dame3=0
dame4=0
a = 1
sirokuro = ["◇","〇","●"]
#横===============================
def line_i(y,x):
    global chpoin_siro
    global chpoin_kuro
    global dame
    global dame2
    global o
    global chekmake
    global sirokuro
    global c
    global a
    global cc
    global aa
    global C

    chekmake=[]

    chpoin_kuro=[]
    dame2=0
    o=0

    for i in range(x):
        if dame == 0:
            if sirokuro[aa+C] in m[y][x-i-1].get():
                chpoin_kuro.append(x-i-1)
                chekmake.append(x-i-1)
                dame2+=1
                o+=1

            elif sirokuro[0] in m[y][x-i-1].get() and dame2>0 and dame==0:
                ccc = 0
                while len(chpoin_kuro)>0:
                    chpoin_kuro.pop(chpoin_kuro.index(chekmake[ccc]))
                    ccc+=1
                dame += 1
                o+=1
            
            else:
                dame+=1
                o=0

    if o<1 and dame2>0:
        for i in chpoin_kuro:
            m[y][i].set(sirokuro[aa] )
        if a==1 and cc ==0:
            a=2
            c=-1
            cc+=1
        elif a==2 and cc == 0:
            c=1
            a=1
            cc+=1
    o=0
    chpoin_kuro=[]
    dame2=0
    dame = 0
    chekmake=[]
    for i in range(x+1,8):
        if dame == 0:
            if sirokuro[aa+C] in m[y][i].get():
                chpoin_kuro.append(i)
                chekmake.append(i)
                o+=1
                dame2+=1
            elif sirokuro[0] in m[y][i].get() and dame2>0 and dame==0:
                ccc = 0
                while len(chpoin_kuro)>0:
                    chpoin_kuro.pop(chpoin_kuro.index(chekmake[ccc]))
                    ccc+=1
                dame += 1
                o += 1
            else:
                o=0
                dame += 1
    dame = 0
    
    if o<1 and dame2>0:

        for i in chpoin_kuro:
            m[y][i].set(sirokuro[aa] )

        if a==1 and cc ==0:
            a=2
            c=-1
            cc+=1

        elif a==2 and cc == 0:
            c=1
            a=1
            cc+=1            
    dame2 = 0

#==========================



#縦===============================
def row_i(y,x):
    global chpoin_siro
    global chpoin_kuro
    global dame
    global dame2
    global rrr
    global chekmake
    global o
    global sirokuro
    global c    
    global a
    global cc
    global aa
    global C

    o=0
    chpoin_kuro=[]
    chekmake=[]
    dame2=0
    dame=0

    for i in range(y):
        if dame == 0:
            if sirokuro[aa+C] in m[y-1-i][x].get():
                chpoin_kuro.append(y-1-i)
                chekmake.append(y-1-i)
                dame2+=1
                o+=1

            elif sirokuro[0] in m[y-1-i][x].get() and dame2>0 and dame==0:
                ccc = 0
                while len(chpoin_kuro)>0:
                    chpoin_kuro.pop(chpoin_kuro.index(chekmake[ccc]))
                    ccc+=1
                o+=1
                dame += 1
            
            else:
                o=0
                dame+=1

    if o<1 and dame2>0:
        for i in chpoin_kuro:
            print(i)
            m[i][x].set(sirokuro[aa] )
        if a==1 and cc ==0:
            a=2
            c=-1
            cc+=1
        elif a==2 and cc == 0:
            c=1
            a=1
            cc+=1
    o=0
    chpoin_kuro=[]

    dame = 0
    dame2 =0
    chekmake=[]
    for i in range(y+1,8):
        if dame == 0:
            if sirokuro[aa+C] in m[i][x].get():
                chpoin_kuro.append(i)
                chekmake.append(i)
                print(m[i][x].get())
                o+=1
                dame2+=1
            elif sirokuro[0] in m[i][x].get() and dame2>0 and dame==0:
                ccc = 0
                while len(chpoin_kuro)>0:
                    chpoin_kuro.pop(chpoin_kuro.index(chekmake[ccc]))
                    ccc+=1
                dame += 1
                o+=1
            else:
                o=0
                dame+=1
    dame = 0
    
    if o<1 and dame2>0:
        for i in chpoin_kuro:
            m[i][x].set(sirokuro[aa] )
        if a==1 and cc ==0:
            a=2
            c=-1
            cc+=1
        elif a==2 and cc == 0:
            c=1
            a=1
            cc+=1
    dame2=0

#==========================



#斜め==============================

def cross(y,x):
    global chpoin_siro
    global chpoin_kuro
    global chpoin_kuro1
    global chpoin_kuro2
    global chekmake
    global chekmake2
    global dame
    global dame2
    global dame3
    global dame4
    global chekmake2_1
    global chekmake2_2
    global chekmake3_1
    global chekmake3_2
    global chekmake4_1
    global chekmake4_2
    global ccc
    global dame4_1
    global o
    global sirokuro
    global c
    global a
    global cc
    global aa
    global C

    chpoin_kuro1=[]
    chpoin_kuro2=[]
    dame4_1 = 0
    chekmake=[]
    chekmake2=[]

    for i in range(1,8):

        if dame == 0:

            if (x+i < 8) and (y+i < 8):##
                if sirokuro[aa+C] in m[y+i][x+i].get():
                    chpoin_kuro2.append(y+i)
                    chekmake.append(y+i)
                    chpoin_kuro1.append(x+i)
                    chekmake2.append(x+i)
                    dame4_1 +=1
                    o+=1

                elif sirokuro[0] in m[y+i][x+i].get() and dame4_1>0 and dame==0:
                    ccc = 0

                    while len(chpoin_kuro1)>0:
                        chpoin_kuro2.pop(chpoin_kuro2.index(chekmake[ccc]))
                        chpoin_kuro1.pop(chpoin_kuro1.index(chekmake2[ccc]))
                        ccc+=1
                    dame+=1
                    o+=1



                else:
                    dame+=1
                    o=0
                    
    if o<1 and dame4_1>0:
        for i in range(len(chpoin_kuro2)):
            m[chpoin_kuro2[i]][chpoin_kuro1[i]].set(sirokuro[aa] )
            
        if a==1 and cc ==0:
            a=2
            c=-1
            cc+=1

        elif a==2 and cc == 0:
            c=1
            a=1
            cc+=1

    chpoin_kuro1=[]
    chpoin_kuro2=[]
    chekmake=[]
    chekmake2_1=[]
    chekmake2_2=[]

    dame4_1=0
    for i in range(1,8):
        if dame2==0:        

            if  x-i >= 0 and y-i >= 0:
                if sirokuro[aa+C] in m[y-i][x-i].get():
                    print(aa,c)
                    chpoin_kuro2.append(y-i)
                    chpoin_kuro1.append(x-i)
                    chekmake2_1.append(y-i)
                    chekmake2_2.append(x-i)
                    dame4_1 +=1
                    o+=1

                elif sirokuro[0] in m[y-i][x-i].get() and dame4_1>0 and dame2==0:
                    ccc = 0

                    while len(chpoin_kuro1)>0:
                        chpoin_kuro2.pop(chpoin_kuro2.index(chekmake2_1[ccc]))
                        chpoin_kuro1.pop(chpoin_kuro1.index(chekmake2_2[ccc]))
                        ccc+=1
                    dame2+=1
                    o+=1

                else:
                    dame2+=1
                    o=0

    if o<1 and dame4_1>0:
        for i in range(len(chpoin_kuro2)):
            m[chpoin_kuro2[i]][chpoin_kuro1[i]].set(sirokuro[aa] )
        
        if a==1 and cc ==0:
            a=2
            c=-1
            cc+=1

        elif a==2 and cc == 0:
            c=1
            a=1
            cc+=1   

    chpoin_kuro1=[]
    chpoin_kuro2=[]
    chekmake=[]

    dame4_1 = 0
    chekmake3_1=[]
    chekmake3_2=[]

    for i in range(1,8):
        if dame3==0:

            if  x-i >= 0 and y+i < 8:
                if sirokuro[aa+C] in m[y+i][x-i].get():
                    chpoin_kuro2.append(y+i)
                    chpoin_kuro1.append(x-i)
                    chekmake3_1.append(y+i)#
                    chekmake3_2.append(x-i)#
                    dame4_1 +=1
                    o+=1

                elif sirokuro[0] in m[y+i][x-i].get() and dame4_1>0 and dame3==0:
                    ccc = 0

                    while len(chpoin_kuro1)>0:
                        chpoin_kuro2.pop(chpoin_kuro2.index(chekmake3_1[ccc]))
                        chpoin_kuro1.pop(chpoin_kuro1.index(chekmake3_2[ccc]))
                        ccc+=1
                    dame3+=1
                    o+=1


                else:
                    o=0
                    dame3+=1

    if o<1 and dame4_1>0:                
        for i in range(len(chpoin_kuro2)):
            m[chpoin_kuro2[i]][chpoin_kuro1[i]].set(sirokuro[aa] )
        
        if a==1 and cc ==0:
            a=2
            c=-1
            cc+=1
        elif a==2 and cc == 0:
            c=1
            a=1
            cc+=1

    chpoin_kuro1=[]
    chpoin_kuro2=[]
    chekmake=[]                    

    dame4_1 = 0

    chekmake4_1 = []
    chekmake4_2 = []

    for i in range(1,4):
        if dame4==0:
 
            if  x+i < 8 and y-i >= 0:
                if sirokuro[aa+C] in m[y-i][x+i].get():
                    chpoin_kuro2.append(y-i)
                    chpoin_kuro1.append(x+i)
                    chekmake4_1.append(y-i)
                    chekmake4_2.append(x+i)
                    o+=1
                    dame4_1 +=1
                    
                elif sirokuro[0] in m[y-i][x+i].get() and dame4_1>0 and dame4==0:
                    ccc = 0

                    while len(chpoin_kuro1)>0:
                        chpoin_kuro2.pop(chpoin_kuro2.index(chekmake4_1[ccc]))
                        chpoin_kuro1.pop(chpoin_kuro1.index(chekmake4_2[ccc]))
                        ccc+=1
                    dame4+=1
                    o+=1

                else:
                    o=0
                    dame4+=1
            
    dame = 0
    dame2 =0
    dame3=0
    dame4=0
    chekmake=[]
    if o<1 and dame4_1>0:
        for i in range(len(chpoin_kuro2)):
            m[chpoin_kuro2[i]][chpoin_kuro1[i]].set(sirokuro[aa] )
        
        if a==1 and cc ==0:
            a=2
            c=-1
            cc+=1
        elif a==2 and cc == 0:
            c=1
            a=1
            cc+=1
    

#==========================
##黒が見つかった瞬間終了(if文)と交代プログラム
def pppp():
    global japann
    global sirokuro
    global a
    global c
    global cccc

    print(m[0][0].get())
    for i_1 in range(8):
        for i_2 in range(8):
            
            if (i_1==0 and i_2==0) :
                if (sirokuro[a+c] in m[i_1+1][i_2].get() and sirokuro[a] in m[i_1+3][i_2].get() and  sirokuro[0] in m[i_1][i_2].get()) or  (sirokuro[a+c] in m[i_1][i_2+1].get() and sirokuro[a] in m[i_1][i_2+3].get() and  sirokuro[0] in m[i_1][i_2].get()) or  (sirokuro[a+c] in m[i_1+1][i_2+1].get() and sirokuro[a] in m[i_1+3][i_2+2].get() and  sirokuro[0] in m[i_1][i_2].get()):
                    japann+=1    
            
            elif (i_1==0 and i_2==7):
                if (sirokuro[a+c] in m[i_1+1][i_2].get() and sirokuro[a] in m[i_1+3][i_2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1][i_2-1].get() and sirokuro[a] in m[i_1][i_2-3].get() and  sirokuro[0] in m[i_1][i_2].get()) or  (sirokuro[a+c] in m[i_1+1][i_2-1].get() and sirokuro[a] in m[i_1+3][i_2-3].get() and  sirokuro[0] in m[i_1][i_2].get()):
                    japann+=1

            elif (i_1==7 and i_2==7):
                if (sirokuro[a+c] in m[i_1-1][i_2].get() and sirokuro[a] in m[i_1-3][i_2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1][i_2-1].get() and sirokuro[a] in m[i_1][i_2-3].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1-1][i_2-1].get() and sirokuro[a] in m[i_1-3][i_2-3].get() and  sirokuro[0] in m[i_1][i_2].get()):
                    japann+=1

            elif (i_1==7 and i_2==0):
                if (sirokuro[a+c] in m[i_1-1][i_2].get() and sirokuro[a] in m[i_1-3][i_2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1][i_2+1].get() and sirokuro[a] in m[i_1][i_2+3].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1-1][i_2+1].get() and sirokuro[a] in m[i_1-3][i_2+3].get() and  sirokuro[0] in m[i_1][i_2].get()) :
                    japann+=1
            

            if (i_1==0 and i_2==0) or (i_1==0 and i_2==1) or (i_1==1 and i_2==0):
                if (sirokuro[a+c] in m[i_1+1][i_2].get() and sirokuro[a] in m[i_1+2][i_2].get() and  sirokuro[0] in m[i_1][i_2].get()) or  (sirokuro[a+c] in m[i_1][i_2+1].get() and sirokuro[a] in m[i_1][i_2+2].get() and  sirokuro[0] in m[i_1][i_2].get()) or  (sirokuro[a+c] in m[i_1+1][i_2+1].get() and sirokuro[a] in m[i_1+2][i_2+2].get() and  sirokuro[0] in m[i_1][i_2].get()):
                    japann+=1    
            
            elif (i_1==0 and i_2==7) or (i_1==0 and i_2==6) or (i_1==1 and i_2==7):
                if (sirokuro[a+c] in m[i_1+1][i_2].get() and sirokuro[a] in m[i_1+2][i_2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1][i_2-1].get() and sirokuro[a] in m[i_1][i_2-2].get() and  sirokuro[0] in m[i_1][i_2].get()) or  (sirokuro[a+c] in m[i_1+1][i_2-1].get() and sirokuro[a] in m[i_1+2][i_2-2].get() and  sirokuro[0] in m[i_1][i_2].get()):
                    japann+=1

            elif (i_1==7 and i_2==7) or (i_1==7 and i_2==6) or (i_1==6 and i_2==7):
                if (sirokuro[a+c] in m[i_1-1][i_2].get() and sirokuro[a] in m[i_1-2][i_2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1][i_2-1].get() and sirokuro[a] in m[i_1][i_2-2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1-1][i_2-1].get() and sirokuro[a] in m[i_1-2][i_2-2].get() and  sirokuro[0] in m[i_1][i_2].get()):
                    japann+=1

            elif (i_1==7 and i_2==0) or (i_1==7 and i_2==5) or (i_1==6 and i_2==0):
                if (sirokuro[a+c] in m[i_1-1][i_2].get() and sirokuro[a] in m[i_1-2][i_2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1][i_2+1].get() and sirokuro[a] in m[i_1][i_2+2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1-1][i_2+1].get() and sirokuro[a] in m[i_1-2][i_2+2].get() and  sirokuro[0] in m[i_1][i_2].get()) :
                    japann+=1

            elif i_1==0:
                if (sirokuro[a+c] in m[i_1+1][i_2].get() and sirokuro[a] in m[i_1+2][i_2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1][i_2-1].get() and sirokuro[a] in m[i_1][i_2-2].get() and  sirokuro[0] in m[i_1][i_2].get())or (sirokuro[a+c] in m[i_1][i_2+1].get() and sirokuro[a] in m[i_1][i_2+2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1+1][i_2-1].get() and sirokuro[a] in m[i_1+2][i_2-2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1+1][i_2+1].get() and sirokuro[a] in m[i_1+2][i_2+2].get() and  sirokuro[0] in m[i_1][i_2].get()):
                    japann+=1

            elif i_1==7:
                if (sirokuro[a+c] in m[i_1-1][i_2].get() and sirokuro[a] in m[i_1-2][i_2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1][i_2-1].get() and sirokuro[a] in m[i_1][i_2-2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1][i_2+1].get() and sirokuro[a] in m[i_1][i_2+2].get()) or (sirokuro[a+c] in m[i_1-1][i_2-1].get() and sirokuro[a] in m[i_1-2][i_2-2].get()) or (sirokuro[a+c] in m[i_1-1][i_2+1].get() and sirokuro[a] in m[i_1-2][i_2+2].get()) :
                    japann+=1

            elif i_2==0:
               if (sirokuro[a+c] in m[i_1+1][i_2].get() and sirokuro[a] in m[i_1+2][i_2].get()) or (sirokuro[a+c] in m[i_1-1][i_2].get() and sirokuro[a] in m[i_1-2][i_2].get()) or (sirokuro[a+c] in m[i_1][i_2+1].get() and sirokuro[a] in m[i_1][i_2+2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1+1][i_2+1].get() and sirokuro[a] in m[i_1+2][i_2+2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1-1][i_2+1].get() and sirokuro[a] in m[i_1-2][i_2+2].get() and  sirokuro[0] in m[i_1][i_2].get()):
                    japann+=1
                
            elif i_2==7:
                if (sirokuro[a+c] in m[i_1+1][i_2].get() and sirokuro[a] in m[i_1+2][i_2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1-1][i_2].get() and sirokuro[a] in m[i_1-2][i_2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1][i_2-1].get() and sirokuro[a] in m[i_1][i_2-2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1+1][i_2-1].get() and sirokuro[a] in m[i_1+2][i_2-2].get() and  sirokuro[0] in m[i_1][i_2].get()) or (sirokuro[a+c] in m[i_1-1][i_2-1].get() and sirokuro[a] in m[i_1-2][i_2-2].get() and  sirokuro[0] in m[i_1][i_2].get()):
                    japann+=1
 
            else:
                if sirokuro[a+c] in m[i_1][i_2].get():
                    if (sirokuro[0] in m[i_1-1][i_2].get() and sirokuro[a] in m[i_1+1][i_2].get()) or (sirokuro[0] in m[i_1+1][i_2].get() and sirokuro[a] in m[i_1-1][i_2].get()) or (sirokuro[0] in m[i_1][i_2-1].get() and sirokuro[a] in m[i_1][i_2+1].get())or (sirokuro[0] in m[i_1][i_2+1].get() and sirokuro[a] in m[i_1][i_2-1].get()) or (sirokuro[0] in m[i_1+1][i_2-1].get() and sirokuro[a] in m[i_1-1][i_2+1].get()) or (sirokuro[0] in m[i_1+1][i_2+1].get() and sirokuro[a] in m[i_1-1][i_2-1].get()) or (sirokuro[0] in m[i_1-1][i_2-1].get() and sirokuro[a] in m[i_1+1][i_2+1].get()) or (sirokuro[0] in m[i_1-1][i_2+1].get() and sirokuro[a] in m[i_1+1][i_2-1].get()):
                        japann+=1
                else:
                    pass

    if japann==0:
        if a==1:
            a=2
            c=-1
            cccc+=1
        elif a==2:
            c=1
            a=1
            cccc+=1
    

#==============================
def qui(e):
    quit()

#================================
def end(s):
    global m
    global sirokuro
    global aa

    root2 = tk.Tk()
    win_w = tk.Frame(root2)
    win_w.grid(column=0,row=0,padx=15,pady=15)
    label = tk.Label(win_w, text =s)
    label.grid(column = 0, row = 0, sticky = 'w')
    endb = tk.Button(root2,text="終了")
    endb.grid(row=3,column=3,columnspan=4)
    endb.bind("<Button-1>",qui)
                    



#==================================
#コマ判定

def key(y,x):
    global m
    global l
    global a
    global sirokuro
    global c
    global cccc
    global cc
    global aa
    global C
    global japann
    global siroo
    global kuroo
    global s
    aa=a
    C=c

    pppp()##
    aa=a
    C=c
    if japann==0:
        pppp()
        aa=a
        C=c

        if japann==0:
            for r in range(8):
                for R in range(8):
                    line_i(y,x)
                    row_i(y,x)
                    cross(y,x)
                    if cc==1:
                        m[y][x].set(sirokuro[aa])
                    cc=0
                    if m[r][R].get()=="〇":
                        siroo+=1
                    elif m[r][R].get()=="●":
                        kuroo+=1
                    else:
                        pass
            if kuroo>siroo:
                s = "●勝利"
            elif siroo>kuroo:
                s = "〇勝利"
            else:
                s = "引き分け"   
            end(s)

    japann=0
    aa=a
    C-c

    if cccc==1:
        pass
    cccc=0
    if  sirokuro[0]   in m[y][x].get() :
        if (y == 0 or x == 0 or y == 7  or x == 7):
            pass
        line_i(y,x)
        row_i(y,x)
        cross(y,x)
        if cc==1:
            m[y][x].set(sirokuro[aa])
        cc=0

        if  sirokuro[0]   in m[y][x-2].get() :
            pass
        pass
        if dame2 ==5:
            a=sirokuro[a+c]

    pppp()
    C=c
    aa=a
    if japann==0:
        pppp()
        aa=a
        C=c
        pass

        if japann==0:
            pass

            for r in range(8):
                for R in range(8):
                    cc=0
                    if m[r][R].get()=="〇":
                        siroo+=1
                    elif m[r][R].get()=="●":
                        kuroo+=1
                    else:
                        pass

            if kuroo>siroo:
                s = "●勝利"
            elif siroo>kuroo:
                s = "〇勝利"
            else:
                s = "引き分け"   
            end(s)            
    japann=0
#============================
def GUI():
    global l
    global m
    global I
    global i
    global sirokuro
    n = 0
    m = [["?" for b in range(8)] for b in range(8)]
    root = tk.Tk()
    root.title("オセロ")
    f = tk.Frame(root)
    f.grid(column=0,row=0,padx=15,pady=15)
    for I in range(8):

        for i in range(8):

            l[I][i] = tk.StringVar()
            if (I==4 and i==4)or(I==3 and i==3):
                l[I][i].set(sirokuro[1] )
            elif (I==3 and i==4)or(I==4 and i==3):
                l[I][i].set(sirokuro[2] )
            else:
                l[I][i].set(sirokuro[0] )

            m[I][i] = tk.StringVar()
            if (I==4 and i==4)or(I==3 and i==3):
                m[I][i].set(sirokuro[1] )
            elif (I==3 and i==4)or(I==4 and i==3):
                m[I][i].set(sirokuro[2] )
            else:
                m[I][i].set(sirokuro[0] ) 

            x = i
            y = I
            
            l[I][i] = tk.Button(f,textvariable=m[I][i],command=functools.partial(key,y,x),font=('MSゴシック',32))
            l[I][i].grid(row=I,column=x)
    
    root.mainloop()

GUI()

