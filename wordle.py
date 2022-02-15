from termcolor import colored
import requests
from random import randrange
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def return_right_color(letter,index,word):
    if(word[index]==letter):
        return 'green'
    elif letter in word:
        return 'yellow'
    else:
        return 'white'


def clear_and_print_info():
    cls()
    print(colored("\n\nStarting a new game of Wordly.\n\n",'green'))
    print("You must try to guess a 5 letter word.\n")
    print(colored('[','cyan')+colored("GREEN",'green',attrs=['bold'])+colored(']','cyan')+" letters mean correct letter in the correct place.\n")
    print(colored('[','cyan')+colored("YELLOW",'yellow',attrs=['bold'])+colored(']','cyan')+" letters mean correct letter but in the wrong place.\n")
    print(colored('[','cyan')+colored("WHITE",'white',attrs=['bold'])+colored(']','cyan')+" letters mean the letters are not in the word.\n")
    print("You have 6 guesses, good luck!\n")
    print("Type 'exit' at any time to leave.\n")


def main():
    allwords=requests.get("https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt").text.split('\n')
    word=allwords[randrange(len(allwords))]
    guess=""
    i=1
    guess_stack=[]
    clear_and_print_info()
    while i<8:
        
        if(i==7 or guess==word):
            if(guess==word):
                print(colored("\nYou Won! :)","green"))
            else:
                print("\n\nGame over you lost, the word was: "+colored(word,'red',attrs=['bold','underline']))
            res=input(f"\nWanna play again? (y/n): ")
            if(res=='y'):
                word=allwords[randrange(len(allwords))]
                guess=""
                guess_stack=[]
                i=1
                clear_and_print_info()
            else:
                print("\nThanks for playing :)\n")
                break

        guess=""
        while len(guess)>5 or len(guess)<5 or (not guess in allwords):
            guess=input(f"\nGuess #{i}: ")
            if(not guess in allwords and not guess=='exit'):
                print(colored("That is not a word as far as I know... try again",'red'))
            elif guess=='exit':
                break

        if guess=='exit':
            print("\nThanks for playing :)\n")
            break
        
        guess_stack.append(guess)
        clear_and_print_info()
        for users_guess in guess_stack:
            print(colored(list(users_guess)[0],return_right_color(list(users_guess)[0],0,word),attrs=['bold']),colored(list(users_guess)[1],return_right_color(list(users_guess)[1],1,word),attrs=['bold']),colored(list(users_guess)[2],return_right_color(list(users_guess)[2],2,word),attrs=['bold']),colored(list(users_guess)[3],return_right_color(list(users_guess)[3],3,word),attrs=['bold']),colored(list(users_guess)[4],return_right_color(list(users_guess)[4],4,word),attrs=['bold']))

        i=i+1
    
if "__main__":
    main()
