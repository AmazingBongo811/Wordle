from tkinter import *


root = Tk()

def display_grid(total_guess,word_length):
    for r in range(total_guess):
       for c in range(word_length):
            Label(root, text="",height=6,width=6,bg="grey",relief="solid",bd=5,).grid(row=r,column=c)

    root.update()


def letters_grid(guess,row1):
    col = 0
    for i in guess:
        Label(root, text=i.upper(),height=6,width=6,bg="grey",relief="solid",bd=5,fg="white").grid(row=row1,column=col)
        col += 1
    root.update()

def color_gird(letters_colours,row1):
    col = 0
    for i in letters_colours:
        if letters_colours[i] == "g":
             Label(root,text=i[0].upper(),height=6,width=6,bg="green",relief="solid",bd=5,fg="white").grid(row=row1,column=col)
        if letters_colours[i] == "o":
             Label(root, text=i[0].upper(),height=6,width=6,bg="orange",relief="solid",bd=5,fg="white").grid(row=row1,column=col)
        if letters_colours[i] == "b":
             Label(root, text=i[0].upper(),height=6,width=6,bg="grey",relief="solid",bd=5,fg="white").grid(row=row1,column=col)
        col +=1
    root.update()









