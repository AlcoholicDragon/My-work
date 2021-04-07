import turtle, random

def startUp():
  '''
  Function to draw the gallows and output the introductory text
  for the game.
  '''
  t = turtle.Turtle()
  t.pu() #pen up
  t.setx(-250)
  t.sety(80)
  t.pd() #pen down
  t.speed(50)
  t.fd(100)
  t.rt(180)
  t.fd(50)
  t.rt(90)
  t.fd(170)
  t.rt(90)
  t.fd(100)
  t.rt(90)
  t.fd(50)
  t.ht() #hides the turtle to remove the arrow that is displayed on screen
  #the code above is used to drawn the gallows for the hangman

  print ("-"*26)
  print ("Welcome to HANGMAN!")
  print ("-"*26)
  print ("Categories...")
  print ("")
  print ("(1) Technology")
  print ("(2) Food")
  print ("(3) Sports")
  print ("(4) Animals")
  print ("")
  #code above is all instructional for the user
  
  main(t)

def main(t):
  '''
  Main function for the hangman gameplay.
  '''
  #categories containing different potential words for the game
  technology = ["apple", "computer", "phone", "processor", "memory", "storage", "data"]
  food = ["banana", "mango", "steak", "chicken", "cucumber", "chocolate", "soup", "pasta"]
  sports = ["soccer", "hockey", "football", "baseball", "basketball", "rowing", "wrestling"]
  animals = ["cat", "dog", "lion", "tiger", "mouse", "bird", "shark", "dolphin", "alligator"]
  categories = [technology, food, sports, animals] #list of lists to contain all the categories
  categoryStrings = ["Technology", "Food", "Sports", "Animals"] #used later for outputting the selected category
  alphabet = ["a","b","c", "d", "e", "f", "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] #used to ensure the user's input is a letter
  guessedLetters = [] #list to keep track of the letters the user has guessed
  while True:
    userCategory = input("Which category would you like to play? (ex: 1):")
    if userCategory == "1" or userCategory == "2" or userCategory == "3" or userCategory == "4": #makes sure the user gives a proper input
      userCategory = int(userCategory) #converts the user's input into string
      userCategory -= 1 #must be decreased by one since lists begin counting at zero
      break #loop asking for an input is exited
    else: #if the user has not entered a valid input
      print ("Invalid input!") #notifies the user of an improper input
  categoryWord = random.choice(categories[userCategory]) #a random word is selected from the category chosen by the user
  word = [] #a list is initialized for the word that will be guessed
  for i in range(len(categoryWord)):
    word.append(categoryWord[i]) #each letter is appended to the list so that they can be individually changed later (into asterisks)
  hiddenWord = [] #list for the version of the word displayed to the user
  for i in range(0, len(word)):
    hiddenWord.append("*") #hiddenWord becomes asterisks for the length of the word
  totalCorrect = 0 #keeps track of correct guesses
  incorrect = 0 #keeps track of incorrect guesses
  print ("")
  print "Category:", categoryStrings[userCategory] #notifies the user of the category they selected
  print ("The game has begun!")
  print ("Remember to click the other window to view the hangman drawing!")
  print ("")
  print ("Can you guess my word?")
  print ("".join(hiddenWord)) #outputs the word which is currently being stored as a list, in a string format
  print ("")
  #code above is simply instructional code for the user
  while True:
    correct = 0 #used to check if current guess is correct (not total)
    while True:
      newLetter = True #used to determine if the letter has already been guessed
      found = False #used to check if the guessed letter has been found in the unguessed letters
      outputStatement = False #avoids multiple error output statements
      print ("")
      guess = input("Enter a guess:")
      for i in guessedLetters: #checks if the letter has already been guessed
        if guess == i:
          print ("You've already guessed this letter!")
          print ("".join(hiddenWord)) #word is outputted as a string
          outputStatement = True #prevents duplicate error statements
          newLetter = False #letter has already been guessed
      if newLetter == True: #the following code only functions if the guess is not a repeated letter
        for i in alphabet:
          if guess == i: #checks that the letter is in the alphabet
            #del alphabet[alphabet.index(i)]
            guessedLetters.append(guess) #guessed letter is added to a list to keep track of the previous guesses
            found = True #the letter has been found in the word
          elif len(guess) > 1: #checks if the input is larger than 1 character
            print ("Invalid input. Must be one letter!")
            print ("".join(hiddenWord)) #word is outputted as a string
            outputStatement = True #prevents duplicate error statements
            break #exits to allow a new user input
      if found == True: #if the letter has been found, the loop to allow the user to guess is broken
        break
      elif found == False: #if the letter is not a single unguessed letter, a corresponding statement is outputted and the loop continues
        if outputStatement == False: #prevents duplicate error statements
          print ("Not a valid input!")
          print ("".join(hiddenWord)) #word is outputted as a string
    for i in range(0, len(word)): 
      if guess == word[i]:
        correct = 1 #updated to identify that a letter has successfully been guessed
        totalCorrect += 1 #the number of correct letters is increased
        hiddenWord[i] = guess #the hidden word is updated to display the guessed letters to the user
        word[i] = "*" #the actual word is updated to hide to guessed letters with asterisks
        print ("You guessed a letter!")
        print ("".join(hiddenWord)) #word is outputted as a string
    if correct == 0: #checks if the user guessed zero letters right
      incorrect += 1 #tally for incorrect guesses is increased
      print ("That letter is not in the word!")
      print ("".join(hiddenWord)) #word is outputted as a string
      drawHangman(t,incorrect) #the function is called to draw a piece on the hangman
    stringWord = "".join(word) #word is joined as a string
    check = len(stringWord) * "*" #a string is created which is asterisks equal in length to the word
    if stringWord == check: #checks if word has been guessed by seeing if the word is now all asterisks (since each letter is replaced in the word with asterisks as they are guessed)
      print ("")
      print ("YOU WIN!")
      print ("")
      print "Score:", incorrect,"(# of incorrect guesses - a lower score is better!)"
      break
    elif incorrect == 6: #ends the game if the user makes 6 incorrect guesses
      print ("")
      print ("You guessed 6 wrong! GAME OVER")
      break

  endGame(t) 

def drawHangman(t,incorrect):
  '''
  This function is called each time the player makes an incorrect guess.
  The corresponding body part is drawn until the man is completed,
  signifying a GAME OVER. This function will draw a different piece
  for each of the six incorrect guesses. The main function ends the game after the sixth incorrect guess.
  '''
  if incorrect == 1:
    t.pu()
    t.setx(-120)
    t.sety(180)
    t.pd()
    t.circle(20)
    t.ht() #hides the turtle to remove the arrow that is displayed on screen
  elif incorrect == 2:
    t.pu()
    t.setx(-100)
    t.sety(160)
    t.pd()
    t.fd(50)
    t.ht() #hides the turtle to remove the arrow that is displayed on screen
  elif incorrect == 3:
    t.rt(45)
    t.fd(30)
    t.ht() #hides the turtle to remove the arrow that is displayed on screen
  elif incorrect == 4:
    t.pu()
    t.rt(-90)
    t.setx(-100)
    t.sety(110)
    t.pd()
    t.fd(30)
    t.ht() #hides the turtle to remove the arrow that is displayed on screen
  elif incorrect == 5:
    t.pu()
    t.rt(-45)
    t.setx(-100)
    t.sety(135)
    t.pd()
    t.fd(30)
    t.ht() #hides the turtle to remove the arrow that is displayed on screen
  elif incorrect == 6:
    t.pu()
    t.rt(180)
    t.setx(-100)
    t.sety(135)
    t.pd()
    t.fd(30)
    t.pu()
    t.ht() #hides the turtle to remove the arrow that is displayed on screen

def endGame(t):
  '''
  Function used to ask the user if they wish to play again, 
  restarting the game if they do and ending it if they do not.
  '''
  print ("")
  playAgain = input("Do you wish to play again? (yes/no):")
  playAgain = playAgain.lower() #makes the input lowercase to account for the fact that the user may input a capital word
  if playAgain == "yes": #replays the game if the user wishes to play again
    t.clear() #clears the turtle window
    print ("") 
    print ("")
    startUp() #restarts the game

#Mainline
startUp()
