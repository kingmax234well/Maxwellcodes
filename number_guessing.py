import random

random_number = random.randint(1, 100)
while True:

 try:
   guess = int(input('Guess the hidden number between 1 and 100: '))

   if guess < random_number:
    print('Too low. Try again!')
   elif guess > random_number:
    print("Too high. Try again!")
   else:
    print(f"Congratulations! You guessed the number {random_number} correctly!")
    break
 except ValueError:
    print('Please input a valid number')

