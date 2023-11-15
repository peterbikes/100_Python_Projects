#! /usr/bin/python
# idea taken from: codewars.com
# view my profile and solutions at: https://www.codewars.com/users/peterbikes

# **************************************************************************** #
#                                                                 __           #
#    top_words_in_text.py                                        / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

def update_list(splitted, word):
    i = 0
    while(i < len(splitted)):
        if(word == splitted[i]):
            splitted.pop(i)
            i = -1
        i += 1
    return splitted

def top_3_words(text):
    text += " "
    splitted = []
    new_word = ""
    for char in text:
        if(char.isalpha() == True or char == '\''):
            new_word += char.lower()
        if (char == ' ' or char == '\0' or (char.isalpha() == False and char != '\'')):
            if(new_word != "" and (new_word.count("\'") != len(new_word))):
                splitted.append(new_word)
            new_word = ""
    top_three = []
    length = len(splitted)
    i = 0
    while(i < 3 and i < length):
        top_scorer = ""
        control = 0
        for word in splitted:
            count = 0;
            for words in splitted:
                if(word == words):
                    count += 1;
            if(count > control):
                control = count
                top_scorer = word
        if(top_scorer != ''):
            top_three.append(top_scorer)
        splitted = update_list(splitted, top_scorer)
        i += 1
    return top_three;


text = input("Give me your text: ")
print("The top three words in your text are", top_3_words(text))
