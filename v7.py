from gui3 import *
from dict1 import *


total_guess = int(input("how many guesess do you want? "))
word_length = int(input("how many characters? ")) 

create_words_file(word_length)
display_grid(total_guess,word_length)

letters = {"e":26,"a":25,"r":24,"i":23,"o":22,"t":21,"n":20,"s":19,"l":18,"c":17,"u":16,"d":15,"p":14,"m":13,"h":12,"g":11,"b":10,"f":9,"y":8,"w":7,"k":6,"v":5,"x":4,"z":3,"j":2,"q":1}



def find_first_letters(start,end):
    first_letters = ""
    letters1 = []
    counter11 = 0
    for i in letters:
        letters1.append(i)
    for i in range(start,end):
        first_letters += letters1[i]

    return first_letters




words = []

file = open("words1.txt","r")
for lines in file:
    words.append(lines.strip())
file.close()

pos_index = 0
first_guess = []

start = 0
end = word_length

while len(first_guess) == 0:
    first_letters = find_first_letters(start,end)
    for word in range(len(words)):
        while first_letters[pos_index] in words[word]:
            pos_index += 1
            if pos_index == len(first_letters):
                first_guess.append(words[word])
                break
        pos_index = 0
    start += 1
    end += 1




print(first_guess)
guess = first_guess[0]
letters_grid(guess,0)
print(guess)

letters_colors = {}

for letter in guess:
    colour = input("what colour was letter {}? ".format(letter))
    letters_colors[letter] = colour

print(letters_colors)

color_gird(letters_colors,0)

letters_not_in_word = []
letters_not_black = []
letters_in_word = {}

row_pos = 1

guesess = 0
while guesess < total_guess-1:
    position_letters = {}
    for i in range(word_length):
        position_letters[i] = ""
    letters_position = {}
    temp_pos = []
    pos_index2 = 0
    for letter in letters_colors:
        if letters_colors[letter] == "g":
            position_letters[pos_index2] = letter
            letters_position[letter] = pos_index2
            if letter[0] not in letters_not_black:
                letters_not_black.append(letter[0])
            if letter in letters_in_word:
                del letters_in_word[letter]
        if letters_colors[letter] == "o":
            try:
                letters_in_word[letter].append(pos_index2)
            except:
                letters_in_word[letter] = []
                letters_in_word[letter].append(pos_index2)
            if letter[0] not in letters_not_black:
                letters_not_black.append(letter[0])
        if letters_colors[letter] == "b":
            if letter[0] not in letters_not_in_word:
                if letter[0] not in letters_not_black:
                    letters_not_in_word.append(letter[0])
            if letter in letters_in_word:
                del letters_in_word[letter]
        pos_index2 += 1


    for  letter in letters_not_black:
        if letter[0] in letters_not_in_word:
            del letters_not_in_word[letters_not_in_word.index(letter[0])]

    
    letters_potentional_pos = {}
    for m in letters_in_word:
        pos2 = []
        for i in position_letters:
            if position_letters[i] == "":
                pos2.append(i)
        for g in letters_in_word[m]:
            if g in pos2:
                del pos2[pos2.index(g)]
        letters_potentional_pos[m] = pos2


    for key, value in list(letters_potentional_pos.items()):
        if len(letters_potentional_pos[key]) == 1:
            letters_position[key] = letters_potentional_pos[key][0]
            position_letters[letters_potentional_pos[key][0]] = key
            del letters_potentional_pos[key]
        try:
            if len(letters_potentional_pos[key]) == 0:
                del letters_potentional_pos[key]
        except:
            pass



    print("position - letters : {}".format(position_letters))
    print("Letters - position : {}".format(letters_position))
    print("orange letters - position : {}".format(letters_in_word))
    print("grey letters : {}".format(letters_not_in_word))
    print("all letters not grey : {}".format(letters_not_black))      
    print("orange letters - potentional position : {}".format(letters_potentional_pos))


        
    for word in words:
        counter = 0
        counter2 = 0
        counter3 = 0
        if len(letters_position) != 0:
            for n in letters_position:
                try:
                    if word[letters_position[n]] != n[0]:
                        counter += 1
                except:
                    counter += 1
        if len(letters_potentional_pos) != 0:
            for v in letters_potentional_pos:
                try:
                    if word.index(v[0]) not in letters_potentional_pos[v]:
                        counter2 += 1
                except:
                    counter2 += 1
        if len(letters_not_in_word) != 0:
            for h in range(len(letters_not_in_word)):
                if letters_not_in_word[h] not in letters_not_black:
                    if letters_not_in_word[h] in word:
                        counter3 += 1
        if counter != 0 or counter2 != 0 or counter3 != 0:
            words[words.index(word)] = None


    while None in words:
        try:
            for word in words:
                if word == None:
                    words.remove(word)
        except:
            pass

    words_value = {}
    for word in words:
        score = 0
        for letter in word:
            score += letters[letter]
        words_value[word] = score
                
    sorted_words = sorted(words_value.items(), key=lambda x: x[1], reverse=True)
    
    print(sorted_words)

    print()
    print()
    print()
    print()
    
    try:
        guess = sorted_words[0][0]
    except:
        break

    letters_grid(guess,row_pos)
    del words[words.index(guess)]
    print(guess)
    letters_colors = {}
    counter = 2
    for letter in guess:
        colour = input("what colour was letter {}? ".format(letter))
        if letter not in letters_colors:
            letters_colors[letter] = colour
        else:
            letters_colors["{}{}".format(letter,counter)] = colour
            counter += 1
    print("Letters - colours : {}".format(letters_colors))
    color_gird(letters_colors,row_pos)
    row_pos+=1

    guesess += 1

            
    
