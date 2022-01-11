import csv
import re

words = set()

revisedPossibles = []
incorrectLetters = []
knownLetters = []
possibles = []

def wordList():
  with open('words.csv', 'r') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
          words.add(row[0])

def guess(guess):


  
  # This loop just checks for possibilites matching the guess pattern. Only useful if some known letters are found
  for i in words:
    #TODO - check f strings are not cocking this up but appears to work as expected with and without f string


    if re.match(rf"{guess}",i):
      possibles.append(i)


  # Out of those words which have all the known letters
  for index, word in enumerate(possibles):
    test = 0
    for letter in knownLetters:
      if letter in word:
        test +=1
    if test != len(knownLetters):
      possibles.remove(word)

  print(possibles)

  # Out of the possibles which words contain letters known not to be correct

  if len(incorrectLetters) >0:
    for index, word in enumerate(possibles):
      # Test is used as a test mechanism to try and debug the weirdness 
      test=0
      for letter in incorrectLetters:
        
        # print(letter)
        if letter in word:
          test+=1 

        
    if test == 0:
      revisedPossibles.append(word)


  revisedPossibles.sort()
  print("Possibles:\n")
  for i in revisedPossibles:
    print(i)


if __name__ == "__main__":
  wordList()


  while True:

    print("Please enter your guess with known correct letters and full stops for incorrect letters or letters in the wrong place")
    inputGuess = input("> ")

    print("\nPlease enter letters known not to be in the word")
    inputWrongLetters = input().lower()
    for i in inputWrongLetters:
      incorrectLetters.append(i.lower())

    print("\nEnter letters known to be in the word but wrong location")
    inputLettersInWord = input()
    for i in inputLettersInWord:
      knownLetters.append(i.lower())

    guess(inputGuess)