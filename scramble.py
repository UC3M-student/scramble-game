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
    
