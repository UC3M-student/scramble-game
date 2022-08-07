import random as rd
import sys
#SCRAMBLE GAME

with open("scramble.txt","r+") as f:
    lst_words = f.readlines()

playing_word = rd.choice(lst_words)
playing_word = playing_word[0:(len(playing_word)-1)]

word_block = []

for i in range(len(playing_word) - 1):
    word_block.append("-")

print(*word_block)

x = 0

while True:
    question_1 = input("Do yo know the word? (yes/no) -> ")
    if question_1 == "yes":
        print(playing_word)
        question_2 = input("What is the word we are looking for? ")
        
        if question_2 == playing_word:
            print("Congratulations¡. The word we were looking for was ",playing_word)
            sys.exit()
    

    
    
    
    
    
    
    
    
  ------------------------------------------
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


while True:
    question_1 = input("Do yo know the word? (yes/no) -> ")
    if question_1 == "yes":
        print(playing_word)
        question_2 = input("What is the word we are looking for? ")
        
        if question_2 == playing_word:
            print("Congratulations¡. The word we were looking for was",playing_word)
            sys.exit()
    
    question_3 = input("Please choose a character: ")
    if question_3 in playing_word:
        a = word_indexes(playing_word,question_3)
        for i in a:
            word_block = list(word_block)
            word_block[i + x] = question_3
            word_block = "".join(word_block)
            print(word_block)
            x +=-1
        x = 0
    else:
        "We couldn´t find the word"

            
            
        



