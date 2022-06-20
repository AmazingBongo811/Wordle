import csv
def create_words_file(word_length):
        file = open('dictionary.csv')

        type(file)
        csvreader = csv.reader(file)



        rows = []
        for row in csvreader:
                rows.append(row)

        words = []
        for i in rows:
            words.append(i[0])


        temp = []
        for i in words:
                if len(i.strip()) == word_length:
                    if "-" not in i:
                        if i not in temp:
                            temp.append(i)


        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        temp2 = []

        for i in temp:
                counter = 0
                for c in numbers:
                    if c in i:
                        counter += 1
                if counter == 0:
                    temp2.append(i)

        temp3 = []
        for i in temp2:
                if "/" in i or "," in i or "." in i or "'" in i:
                    pass
                else:
                    temp3.append(i)




        file2 = open("words1.txt" ,"w")
        for i in temp3:
            file2.write("{}\n".format(i.lower()))
        file2.close()
