import random

print('''
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.
''')


def number_check(number, secret_number):
  index_check = [i for i in range(3) if number[i] == secret_number[i]]
  if number == secret_number:
     print("You got it!") 
     return True
  elif len(index_check) > 0:
     print("Femi")
  elif any(n in secret_number for n in number):
     print("Pico")
  else:
     print("Bagel")
  return False

while True:
  secret_number = str(random.randint(100, 999))
  guess_counter = 1

  while True:
      if guess_counter > 10:
        print(f"You lose! The number was {secret_number}")
        break
      
      number = input(f"Guess #{guess_counter}: ")
      if len(number) == 3 and number.isdigit():
        correct = number_check(number, secret_number)
        if correct:
          break
        else: 
          guess_counter += 1
      else: 
        print("That is invalid! Enter a three digit number.")
      
  answer = input('Want to play again?(Y/N) ')

  if answer.strip().lower() == "n":
     break


 
    