import random as rd
import sys
#SCRAMBLE GAME

def word_indexes(woord,cht):
    woord = list(woord)
    x = 0
    index_count = []
    
    for i in woord:
        if i == cht:
            index_count.append(x)
            x += 1
        x += 1
    
    return index_count


with open("scramble.txt","r+") as f:
    lst_words = f.readlines()

playing_word = rd.choice(lst_words)
playing_word = playing_word[0:(len(playing_word)-1)]

removal_word = playing_word

word_block = []

for i in range(len(playing_word)):
    word_block.append("-")

print(*word_block)

x = 0
y = 10

while True:
    question_1 = input("Please choose a character. Otherwise if you know the asnwer please write yes -> ")
    if question_1 == "yes":
        question_2 = input("What is the word we are looking for? ")
        if question_2 == playing_word:
            print("Congratulations¡. The word we were looking for was",playing_word)
            sys.exit()
        else:
            y-=1
        print("Incorrect answer, you have",y,"more tries")
        if y ==0:
            print("Too many attempts. Please try again")
            print("The word we were looking for was", playing_word)
            sys.exit()
            
    elif question_1 in playing_word:
        a = word_indexes(playing_word,question_1)
        for i in a:
            word_block = list(word_block)
            word_block[i + x] = question_1
            word_block = "".join(word_block)
            x +=-1
        x = 0
        print(word_block)
    else:
        y-=1
        print("Incorrect answer, you have",y,"more tries")
        if y == 0:
            print("Too many attempts. Please try again")
            print("The word we were looking for was", playing_word)
            sys.exit()
            
