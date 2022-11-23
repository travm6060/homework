import sys
import random

#arguments = sys.argv[1]

arguments = ''

def pick_rps(list):
    return random.choice(list)

word_list = ['rock', 'paper', 'scissors']

while arguments not in word_list:
	arguments = input("rock, paper or scissors? ")
	arguments = arguments.lower()

print("you pick " + arguments)
comp_rps = pick_rps(word_list)
print("computer picks " + comp_rps)

if arguments  == comp_rps:
    print("you tied")

if arguments == 'scissors':
    if comp_rps == 'rock':
        print("Computer Wins")
    elif comp_rps == 'paper':
        print("You Win!")
        
if arguments == 'rock':
    if comp_rps == 'paper':
        print("Computer Wins")
    elif comp_rps == 'scissors':
        print("You Win!")

if arguments == 'paper':
    if comp_rps == 'scissors':
        print("Computer Wins")
    elif comp_rps == 'rock':
        print("You Win!")
