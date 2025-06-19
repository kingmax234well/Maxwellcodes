import random

characters = {'r':'rock', 's':'scissors', 'p':'paper'}
choices = ('r', 'p', 's')

def get_user_choice():
   while True:
     user_choice = input("Rock, Paper, or Scissors? r/p/s: ").lower()
     if user_choice in choices:
      return user_choice
     else:
      print('Invalid choice! Try again!')
   
def display_choices(user_choice, bot_choice):
   print(f'You chose {characters[user_choice]}')
   print(f'Bot chose {characters[bot_choice]}')

def determine_winner(user_choice, bot_choice):
   if user_choice == bot_choice:
    print('Tie!')
   elif(
    (user_choice=='r' and bot_choice=='s') or 
    (user_choice=='p' and bot_choice=='r') or 
    (user_choice=='s' and bot_choice=='p')):
    print('You win!')
   else:
    print('You lose!')

def play_game():
 while True:
  user_choice = get_user_choice()

  bot_choice = random.choice(choices)

  display_choices(user_choice, bot_choice)

  determine_winner(user_choice, bot_choice)

  should_continue = input('Continue? (y/n): ').lower()
  if should_continue == 'n':
      print('Thanks for playing!')
      break
play_game()
   