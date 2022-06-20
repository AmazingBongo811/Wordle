from gui_final import *
from dict1 import *

rounds = int(input("how many rounds do you want to play "))
word_length = int(input("how many characters? "))
total_guess = int(input("how many guesses do you want? "))


statistic_file = "{}{}-statistics.txt".format(word_length,total_guess)

create_words_file(word_length)


def import_stat(stat_file):
    stat = {}
    try:
        file = open(stat_file,"r")
        for i in file:
            string,value = i.split(":")
            stat[string] = value.strip()
        file.close()
    except:
        stat["Total games"] = 0
        stat["Solved games"] = 0
        stat["Failed games"] = 0
        
    return stat
        
def statistics(solved,stat):
    stat["Total games"] = int(stat["Total games"]) + 1
    if solved == True:
        stat["Solved games"] = int(stat["Solved games"]) + 1
    else:
        stat["Failed games"] = int(stat["Failed games"]) + 1
    return stat

def write_stat(stat,stat_file):
    file = open(stat_file,"w")
    for i in stat:
        file.write("{}:{}\n".format(i,stat[i]))
    file.close()



stat = import_stat(statistic_file)

for i in range(rounds):
    word_to_guess = pick_word()
    display_grid(word_to_guess,total_guess,word_length)

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
    for i in file:
        words.append(i.strip())
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


    guess = first_guess[0]
    letters_grid(guess,0)

    letters_colors = check_word(guess,word_to_guess)
    color_gird(letters_colors,0)


    letters_not_in_word = []
    letters_not_black = []
    letters_in_word = {}

    row_pos = 1
    guesses = 0
    while guesses < total_guess - 1: 
    #for c in range(5):
        position_letters = {}
        for i in range(word_length):
            position_letters[i] = ""
        letters_position = {}
        temp_pos = []
        pos_index2 = 0
        for i in letters_colors:
            if letters_colors[i] == "g":
                position_letters[pos_index2] = i
                letters_position[i] = pos_index2
                if i[0] not in letters_not_black:
                    letters_not_black.append(i[0])
                if i in letters_in_word:
                    del letters_in_word[i]
            if letters_colors[i] == "o":
                try:
                    letters_in_word[i].append(pos_index2)
                except:
                    letters_in_word[i] = []
                    letters_in_word[i].append(pos_index2)
                if i[0] not in letters_not_black:
                    letters_not_black.append(i[0])
            if letters_colors[i] == "b":
                if i[0] not in letters_not_in_word:
                    if i[0] not in letters_not_black:
                        letters_not_in_word.append(i[0])
                if i in letters_in_word:
                    del letters_in_word[i]
            pos_index2 += 1

        pos_index3 = 0

        for  i in letters_not_black:
            if i[0] in letters_not_in_word:
                del letters_not_in_word[letters_not_in_word.index(i[0])]

        
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
                for i in words:
                    if i == None:
                        words.remove(i)
            except:
                pass

        words_value = {}
        for i in words:
            score = 0
            for b in i:
                score += letters[b]
            words_value[i] = score
                    
        sorted_words = sorted(words_value.items(), key=lambda x: x[1], reverse=True)

        solved = False
        try:
            guess = sorted_words[0][0]
            letters_grid(guess,row_pos)
            letters_colors = check_word(guess,word_to_guess)
            color_gird(letters_colors,row_pos)
            del words[words.index(guess)]
        except:
            solved = True
            break

        solved_counter = 0
        for i in letters_colors:
            if letters_colors[i] == "g":
                solved_counter += 1
        if solved_counter == 5:
            solved = True
        
        row_pos+=1
        guesses += 1

    stat = statistics(solved,stat)
            
write_stat(stat,statistic_file)
print("******************")
print("Finished")
print(stat)
print("******************")


            
    
