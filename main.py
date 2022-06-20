'''
Coded by Arush Nandyala
Project is called triviaGame
Packages imported are random, sys, and time
Coded in python 5.3
'''

def system():
  print('\nHello', 'player, Welcome! Which mode do you want to choose?')
  print('\nIf you want to use the one player mode which ends when you answer the amount of questions you want OR when time runs out, press 1')
  print('\nIf you want to use the host system where players answer till time runs out, press 2 \nHowever this system is NOT self grading and you will need a host to use this.\n')
  sys = int(input())
  if sys == 1:
    import selfPointSystem
    selfPointSystem()
  if sys == 2:
    from hostPointSystem import startGame
    startGame()

system()