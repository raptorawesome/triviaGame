filename = "smTech.txt" 
def dictMaker(filename):
  myfile = open(str(filename), "r", encoding="utf8") # opens the line in read mode
  Trivia = { } # empty dictionary
  i = 0
  for line in myfile: # 
    x = line.strip().split("\t") # splits at every line break
    values = x[0:] # gets all the values up till the split
    i += 1 # need this as a key, it's also a integer since we can use randrange with it
    Trivia.setdefault(i, []).extend(values) # new list for each value, .extend(values) sets the value of the line to it

  #import pdb; pdb.set_trace()
  return Trivia

dictMaker(filename)