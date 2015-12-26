import os
import random

words = [
  'island',
  'finland',
  'brazil',
  'united states',
  'canada',
  'iraq',
  'mexico'
]

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def draw():
  for letter in secret_word:
    if letter in good_guesses:
      print(letter, end='')
    else:
      print('_', end='')

  print('')
  print('Strikes: {}/7'.format(len(bad_guesses)))
  print('')

while True:
  start = input('Press enter/return to start, or enter Q to quit: ')
  if start.lower() == 'q':
    break
  else:

    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while len(bad_guesses) < 5 and len(good_guesses) != len(list(secret_word)):
      draw()

      guess = input('Choose a letter: ').lower()

      if len(guess) != 1:
        print('You can only guess a single letter')
        continue
      elif guess in bad_guesses or guess in good_guesses:
        print('You"ve already choose this letter. Try other')
        continue
      elif not guess.isalpha():
        print('You can only guess letters!')
        continue

      if guess in secret_word:
        good_guesses.append(guess)
        if len(good_guesses) == len(list(secret_word)):
          print('You win. The word was {}'.format(secret_word))
          break
      else:
        bad_guesses.append(guess)
    else:
      print('You did not guess it. My secret word was {}'.format(secret_word))
