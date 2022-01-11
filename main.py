import csv
import re

words = set()


incorrectLetters = []
knownLetters = []


def wordList():
  with open('words.csv', 'r') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
          words.add(row[0])

def guessWord(guess):
  possibles = []
  revisedPossibles = []
  for i in words:
    if re.match(rf"{guess}",i):
      possibles.append(i)

  print(len(knownLetters))
  # Out of those words which have all the known letters
  for index, word in enumerate(possibles):
    test = 0
    for letter in knownLetters:
      if letter in word:
        test += 1
    if test != len(knownLetters):
      possibles.remove(word)

  # Out of the possibles which words contain letters known not to be correct

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
    if len(inputWrongLetters) > 0:
      for i in inputWrongLetters:
        incorrectLetters.append(i.lower())

    print("\nEnter letters known to be in the word but wrong location")
    inputLettersInWord = input()
    for i in inputLettersInWord:
      knownLetters.append(i.lower())

    guessWord(inputGuess)