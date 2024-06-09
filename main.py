# Play the game
play = "yes"



# Introduction
print("hello there")
name= input("what is your name?\n")
print("welcome, {} to this quiz on what to do if you encounter a bear".format(name))


# Number of attempts
while True:
  try:
    tries = int(input("How many attempts do you want for each question? 1-4\n"))
    tries = int(tries)
    break
  except:
    print("That's not a number")
  # attempts = attempts - 1

while play == "yes":
  score = 0

  # Statement
  print("if it's brown lay down, if it's black fight back, if it's white good night")

  QUESTION_FORMAT = "{}\nA.{}\nB.{}\nC.{}\nD.{}"

  # Question 1
  question = "If you ever encounter a polar bear, what do you do?"
  a = "Lay down"
  b = "Fight back"
  c = "Theres nothing you can do"
  d = "Run at it and give it a hug\n"
  guess = input(QUESTION_FORMAT.format(question, a, b, c, d)). lower ()

  # Guess 1
  if guess == c.upper() or guess == "c":
    print("correct")
    score += 5
    print("if you encounter a polar bear there is nothing you can do.")
  elif guess == "":
    print("not sure?")
    score -= 1
  elif guess != a and guess != "a" and guess != "b" and guess != "b" and guess != "c" and guess != "d":
    print("that was not an option, please try again")
    score -= 1
  else:
    print("Incorrect, if you encounter a polar bear there is nothing you can do.")
    score += 3





  # Question 2 
  input("\nif you see a brown bear what do you do?\n").lower()

  # Guess 2
  if guess == "nothing".lower():
    print("correct")
    score += 5
    print("if you encounter a polar bear there is nothing you can do.")
  elif guess == "":
    print("Not sure?")
  else:
    print("Incorrect, if you encounter a polar bear there is nothing you can do.")
    score += 3




  # Make this a multichoice
  # Question 3
  # input("if you see a black bear what do you do?\n").lower()


  # Statement
  print("With a brown bear, pretending to be dead is your best chance. With a black bear, scaring it off is your best chance.")

  # End of quiz
  print("that is the end of the quiz, thank you {} for filling this out, your final score is {}.".format(name, score))

  print("Your final score is", score)

  # Play again
  play = input ("do you want to play again?").lower()
print("Goodbye")