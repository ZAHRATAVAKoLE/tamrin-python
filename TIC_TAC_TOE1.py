# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 23:29:54 2022

@author: zahra 
tic_tac_toe
"""


a=[['- ','- ','- ']
   ,['- ','- ','- ']
   ,['- ','- ','- ']]
def board():
    for row in a:
        for item in row:
            print(item,end='')
        print()

def chek_free(row,col):
    if a[row][col]=='- ':
        return True
    return False
    

board()
while True:
    while True:
        print("player 1:")
        row=int(input("player1 enter your row: "))
        col=int(input("player1 enter your col: "))
        if chek_free(row,col)==True:
            a[row][col]='X'
            break
        else :
            print("dont select this row and col")
    board()

    while True:
        print("player 2:")
        row=int(input("player2 enter your row: "))
        col=int(input("player2 enter your col: "))
        if chek_free(row,col)==True:
            a[row][col]='O'
            break
        else :
            print("dont select this row and col")
    board()
