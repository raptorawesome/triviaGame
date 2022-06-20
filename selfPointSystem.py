import sys as s
import time
playerName = input('\nEnter your name: ')
def selfSystem(playerName): 
  global score # needs to be global so exit can use it
  score = 0
  global timer
  try:
    timeLimit = int(input(("\nEnter how long you want your game to last in seconds (If you don't want a time press enter): ")))
  except:
    timeLimit = 1000000 # if the player doesn't want a tome limit it enters this as the time which is seemingly indefinite
  from questions import choice
  choice() # gets the choice of which quiz the user wants to run
  try:
    amount = int(input('How many questions would you like to have? '))
  except:
    amount = 10
  input('Wait till you want to start round. ')
  t_end = time.time() + timeLimit # End time is calculated by the current time + the amount of second input by the user
  downtime = 0
  timer = time.time()
  x = 0
  while time.time() - downtime < t_end: # runs till the current time - downtime is greater than the end time defined by the user
    while x < amount:
      from questions import ask
      from questions import questions
      ask(questions) # prints values from the questions dictionary
      answer = input('What is your answer? ')
      from questions import z # we need z because it gets the index of the dictionary
      answer = answer.capitalize()
      answer = list(answer.split("  ")) # turns the input into a list that isn't split at all
      print(answer)
      if answer == questions[z+1]: # we add 1 to z since the answers are always after the question in the dictionary
        print('Correct!')
        score+=1 # increments the score if the user gpt the question right
        print('You have', score, 'points!') 
      else:
        print('Wrong :(')
        score-=1
        print('You have', score, 'points!') # prints score everytime
        print('Correct answer is', questions[z+1]) # prints correct answer
        try:
          downtime = time.time()
          a = int(input('Enter 1 if you think you should\'ve got it correct: ')) # in case computer made a mistake user can override and add points
          if a == 1:
            score+=2
            print('You have', score, 'points!')
            downtime = time.time() - downtime # downtime is added in order to add back time lost from this interaction
        except:
          downtime = time.time() - downtime
        x+=1
    break  
  timer = time.time() - timer # gets the final time of the player
  
def exit(playerName, points, timer): # returns an exit phrase
  print('\n', playerName, 'has earned a total of', points, 'points with a time of', int(timer), 'seconds! Thank you for playing!')


selfSystem(playerName)
exit(playerName, score, timer)
s.exit()