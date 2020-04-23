import random
import math



def play_game(guesses_left,total_guesses, max_number):
   number_of_guesses = 0
   number = random.randrange(1, max_number)
   while number_of_guesses < total_guesses:
      while True:
         note = "\nGuess the number i'm thinking of between 1 - {} , you have {} guesses\n"
         print(note.format(max_number, guesses_left))
         guess = input()
         try:
            val = int(guess)
            break;
         except ValueError:
            print("This is not a number....Try again")
      number_of_guesses += 1
      guesses_left -= 1

      if number == val:
         print("YOU GOT IT RIGHT! ")
         break
      else:
         if guesses_left == 1:
            message = "THAT WAS WRONG - {} guess left \n"
            print(message.format(guesses_left))
         else:
            message = "THAT WAS WRONG - {} guesses left \n"
            print(message.format(guesses_left))

   if(guesses_left == 0):
      print("--------------")
      print("GAME OVER !")
      print("--------------")

      

      


def start_game():
   while True:
      print("\n-------------------------------------------------------")
      print("WELCOME TO MY NUMBER GUESSING GAME, PICK YOUR LEVEL")
      print("-------------------------------------------------------")
      level = int(input("1.Easy\n2.Medium\n3.Hard\n4.Exit\n"))
      if level == 1:
         play_game(6,6,10)

      if level == 2:
         play_game(4,4,20)

      if level == 3:
         play_game(3,3,50)
      if level == 4:
         exit()
         

start_game()
      


