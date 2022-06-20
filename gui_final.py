from tkinter import *
import random


root = Tk()
root.title("Wordle")

grid_frame = Frame(root)
word_frame = Frame(root)

grid_frame.grid()
word_frame.grid()

def display_grid(word_to_guess,total_guess,word_length):

    for r in range(total_guess):
       for c in range(word_length):
            Label(grid_frame, text="",height=6,width=6,bg="grey",relief="solid",bd=5,).grid(row=r,column=c)

    Label(word_frame,anchor=N, text=word_to_guess,height=1,width=48,bg="grey",relief="solid",bd=5,).grid(row=0,column=0)
    root.update()


def letters_grid(guess,row1):
    col = 0
    for i in guess:
        Label(grid_frame, text=i.upper(),height=6,width=6,bg="grey",relief="solid",bd=5,fg="white").grid(row=row1,column=col)
        col += 1
    root.update()

def color_gird(letters_colours,row1):
    col = 0
    for i in letters_colours:
        if letters_colours[i] == "g":
             Label(grid_frame,text=i[0].upper(),height=6,width=6,bg="green",relief="solid",bd=5,fg="white").grid(row=row1,column=col)
        if letters_colours[i] == "o":
             Label(grid_frame, text=i[0].upper(),height=6,width=6,bg="orange",relief="solid",bd=5,fg="white").grid(row=row1,column=col)
        if letters_colours[i] == "b":
             Label(grid_frame, text=i[0].upper(),height=6,width=6,bg="grey",relief="solid",bd=5,fg="white").grid(row=row1,column=col)
        col +=1
    root.update()

def pick_word():
    file = open("words1.txt","r")
    words = file.readlines()
    file.close()
    word_to_guess = words[random.randint(0,len(words))]
    
    return word_to_guess


def check_word(guess,to_guess):
    letters_colors_pos  = {}
    word_to_guess = to_guess
    letter_freq_to_guess = {}
    for i in word_to_guess:
        letter_freq_to_guess[i] = word_to_guess.count(i)

    current_freq = {}
    counter = 2

    for i in range(len(guess)):

        if guess[i] == word_to_guess[i]:

            if guess[i] not in letters_colors_pos:
                letters_colors_pos[guess[i]] = ["g",i]
            else:
                letters_colors_pos["{}{}".format(guess[i],counter)] = ["g",i]
                counter += 1



    for i in guess:
        current_freq[i] = 0


    for i in range(len(guess)):
        current_freq[guess[i]] += 1
        try:
            if current_freq[guess[i]] == letter_freq_to_guess[guess[i]]:
                if guess[i] in word_to_guess and guess[i] != word_to_guess[i]:
                    try:
                        if letters_colors_pos[guess[i]][0] != "g":
                            if guess[i] not in letters_colors_pos:
                                letters_colors_pos[guess[i]] = ["o",i]
                            else:
                                letters_colors_pos["{}{}".format(guess[i],counter)] = ["o",i]
                                counter += 1
                        else:
                            letters_colors_pos["{}{}".format(guess[i],counter)] = ["b",i]
                            counter += 1
                    except:
                        letters_colors_pos[guess[i]] = ["o",i]

               
            if current_freq[guess[i]] < letter_freq_to_guess[guess[i]]:
                if guess[i] in word_to_guess and guess[i] != word_to_guess[i]:
                    if guess[i] not in letters_colors_pos:
                        letters_colors_pos[guess[i]] = ["o",i]
                    else:
                        letters_colors_pos["{}{}".format(guess[i],counter)] = ["o",i]
                        counter += 1

                    
            if current_freq[guess[i]] > letter_freq_to_guess[guess[i]]:
                if guess[i] != word_to_guess[i]:
                    letters_colors_pos["{}{}".format(guess[i],counter)] = ["b",i]
                    counter += 1

        except:
            pass

           
                
    for i in range(len(guess)):
        if guess[i] not in word_to_guess:
            if guess[i] not in letters_colors_pos:
                letters_colors_pos[guess[i]] = ["b",i]
            else:
                letters_colors_pos["{}{}".format(guess[i],counter)] = ["b",i]
                counter += 1

##   print("letters-colors-position: {}".format(letters_colors_pos))

    letters_colors = {}

    index_counter = 0
    while index_counter != len(letters_colors_pos):
        for i in letters_colors_pos:
            if letters_colors_pos[i][1] == index_counter:
                letters_colors[i] = letters_colors_pos[i][0]
                index_counter += 1

##    print("letters_colors: {}".format(letters_colors))


    return letters_colors
        
        
        
    
    




    


    

                 





