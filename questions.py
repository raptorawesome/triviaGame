import random
from formatter import dictMaker
questions = ''
def choice():
  global questions
  choice = int(input('\nEnter what size you want your trivia to be (1 - 10 questions, 2 - 30 questions, 3 - 50+ questions, 4 -custom questions): '))
  if choice == 1:
    smQuizChoice = int(input('\nWhich quiz would you like to take, 1 - Tech, 2 - Superheroes, 3 - Food: ')) # needs to be integer in order to be comparable
    if smQuizChoice == 1:
      questions = dictMaker("smTech.txt") # gives a different txt file for each choice
    elif smQuizChoice == 2:
      questions =  dictMaker("smSprHeroes.txt")
    elif smQuizChoice == 3:
      questions =  dictMaker("smFood.txt")
  elif choice == 2:
    medQuizChoice = int(input('\nWhich quiz would you like to take, 1 - Sports, 2 - Geography, 3 - Science: ')) 
    if medQuizChoice == 1:
      questions =  dictMaker("medSports.txt")
    elif medQuizChoice == 2:
      questions =  dictMaker("medGeography.txt")
    elif medQuizChoice == 3:
      questions =  dictMaker("medScience.txt")
  elif choice == 3:
    lgQuizChoice = int(input('\nWhich quiz would you like to take, 1 - Random, 2 - Funny, 3 - History: '))
    if lgQuizChoice == 1:
      questions =  dictMaker("lgRandom.txt")
    elif lgQuizChoice == 2:
      questions =  dictMaker("lgFunny.txt")
    elif lgQuizChoice == 3:
      questions =  dictMaker("lgHistory.txt")
  elif choice == 4:
    no_of_lines = int(input('\nHow many questions do you have? ')) # Gets the number of questions to determine range
    with open('custom.txt', 'w') as f:
      f.truncate(0) # deletes everything in the custom.txt file in case it had been used before
    question = "" # default values
    answer = ""
    print('\n and REMEMBER to input questions and answers on seperate lines!')
    for i in range(no_of_lines):
      with open('custom.txt', 'a') as f:
        print('Question', i+1) # Increments for each question, starts with i+1 since i's default value is 0
        question+=input()+"\n" # gets the input of the user on a new line
        f.write(question)
        question.capitalize() # so when it autogrades it capitlization won't cause errors
        answer+=input()+"\n"
        answer.capitalize()
        f.write(answer)
        question = "" 
        answer = ""
    questions = dictMaker("custom.txt")


def ask(y):
  global z # important to make it global since it can be autograded since the answers are always after the question
  z = random.randrange(1, len(y)-1, 2) # gets a random number for the length of dictionary y
  print(y[z]) # randrange starts at 1, ends at the length of the dictionary, and skips every even digit since even ones are answers
  