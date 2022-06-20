import sys as s
import time

a = []
b = []
playerName = ['del'] # added a dummy value here since we need to delete something when function is called
round = 0
def startGame(): # Runs all the functions
  print('Game has started')
  global numPlayers
  numPlayers = int(input('Enter number of players: '))
  players()
  hostSystem(playerName)
  s.exit()

def players(): # Gets all the player names
  for x in range(numPlayers):
    playerName.append(input('Enter player name: '))

def Convert(lst): # Converts a list into a dictionary
    lst_dct = {lst[i]: 0 for i in range(0, len(lst), 2)}
    return lst_dct
  
def hostSystem(playerName):
  points={} #empty dictionary
  points = Convert(playerName) # Gets all the player names and puts them into an empty dictionary
  numRounds = numPlayers # number of rounds is equal to number of players
  from questions import choice
  choice()
  for round in range(numRounds): 
    while True:
      try:
        kick = int(input("Enter player with lowest score in order to remove (0 for first turn) : "))
        if kick < len(playerName): 
          break
        print("\nInvalid player entered, remember to start with 0") 
        print(playerName) # prints the list of playernames to remind user
      except Exception as e:
        print(e)
        print(playerName) # prints the list of playernames to remind user
    playerName.pop(kick)
    if len(playerName) <= 1:
        pass
    x = int(input('\nWho earned the most points (0 for first round) '))
    if len(playerName) == 1:
      print(playerName[0], 'won!!') # if there is only one player remaining this program runs and that player wins
      s.exit()
    a = playerName[x:]
    b = playerName[0:x] # Redefines playerName to a new order that starts with the top player and goes in that order
    playerName = a + b
    try:
      timeLimit = int(input('\nEnter how long you want the round to last in seconds: '))
    except: timeLimit = 120
    with open('points.txt', 'a') as f:
      f.write('Round ') # Writes the round everytime a new round starts
      f.write(str(round+1))
      f.write('\n')
    input('Press enter when you want to start the round. ') # Allows host to stop between rounds
    print('Round', round+1, ':')
    t_end = time.time() + timeLimit # we put it right before round starts to minimize time loss
    while time.time() < t_end:
       for x in range(len(playerName)):
          print(playerName[x] + '\'s turn:')
          timer = time.time()
          from questions import ask # imported them here so the nested function doesn't run when we call the function
          from questions import questions
          ask(questions)
          answer = int(input('\nDid {} get the question right? (1 for yes, 2 for no, 3 to skip) '.format(playerName[x])))
          timer = time.time() - timer
          if answer == 1:
            points[str(playerName[x])] = points.get(str(playerName[x]), 0) + 1 # Increments the value (points) of the key (playername)
            if timer > 10: # Decreases a point if the player goes over 10 seconds
              points[str(playerName[x])] = points.get(str(playerName[x]), 0) - 1
          elif answer == 2: # if player gets question wrong
            points[str(playerName[x])] = points.get(str(playerName[x]), 0) - 1
            if timer > 10:
              points[str(playerName[x])] = points.get(str(playerName[x]), 0) - 1
          else: # in case of a misinput or skip, doesn't decrease points
            points[str(playerName[x])] = points.get(str(playerName[x]), 0)
            if timer > 10:
              points[str(playerName[x])] = points.get(str(playerName[x]), 0) - 1
              
          with open('points.txt', 'a') as f: # Records the total amount of points earned by each player and the time it took per question
            f.write('{} has '.format(playerName[x]),) # Gets playername
            f.write(str(points[str(playerName[x])])) # Gets points
            f.write(' points with a time of ') 
            f.write(str(timer)) # Gets time
            f.write('\n') # Starts a new line
    
 