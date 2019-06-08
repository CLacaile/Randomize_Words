#!/usr/bin/python

import sys
import random

seed = 0
words_list = []

def get_words_from_file():
    words = []
    file = open(".words_list.txt", "r")
    lines = file.readlines()
    for line in lines:
        words.append(line)
    file.close()
    return words

def add_words(words):
    file = open(".words_list.txt", "a")
    for word in words:
        if (word+"\n") in words_list:
            continue
        else:
            words_list.append(word)
            file.write(word + "\n")
    file.close()

def print_words():
    for word in words_list:
        print(word)

def print_help():
    print("randomize_words is a script to print a random word in a given list.\n")
    print("Call the script to print the random word")
    print("Options:\n")
    print("\t -add word : add word to the list;\n")
    print("\t -print : print the list of words in the list\n")
    print("\t -seed nb : set the seed to the value nb (0 is default)\n")
    print("\t -clear : empty the list of words")


words_list = get_words_from_file()

if __name__ == "__main__":
    if len(sys.argv)>1:
        #print(sys.argv)
        if sys.argv[1] == "-help":
            print_help()

        elif sys.argv[1] == "-add":
            if len(sys.argv)<3:
                print("Please add one word or more. Use '-help' to get some help.")
                exit()
            add_words(sys.argv[2:len(sys.argv)])
            
        elif sys.argv[1] == "-print":
            print("The list of words is:\n")
            print_words()

        elif sys.argv[1] == "-seed":
            if len(sys.argv)<3:
                print("Please type in a seed value. Use '-help' to get some help.")
                exit()
            seed = int(sys.argv[2])
            print("Seed has been set to: " + str(sys.argv[2]))
        elif sys.argv[1] == "-clear":
            open(".words_list.txt", "w+").close()
        else:
            print("Invalid argument. Use '-help' to get some help")

    else:
        if words_list == []:
            print("The list of words is empty. Use '-help' to get come help.")
            exit()
        else:
            random.seed = seed
            random_index = random.randint(0, len(words_list)-1)
            print(words_list[random_index])



