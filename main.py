import csv
import re

words = set()
# Only add letters that are known and '.' for unknown or incorrect (placement)
guess = ".rin."
knownLetters = ['d']
incorrectLetters = ['a','e','u','g']
# Pattern is not currently in use but was for regex
pattern = "|".join(incorrectLetters)
possibles = []


with open('words.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        words.add(row[0])


# This loop just checks for possibilites matching the guess pattern. Only useful if some known letters are found
for i in words:
  #TODO - check f strings are not cocking this up but appears to work as expected with and without f string


  if re.match(rf"{guess}",i):
    possibles.append(i)

newpossibles=[]

print("Known unknown letters: ", pattern)
# Out of those words which have all the known letters
for index, word in enumerate(possibles):
  test = 0
  for letter in knownLetters:
    if letter in word:
      test +=1
  if test == len(knownLetters):
    newpossibles.append(word)

# Out of the possibles which words contain letters known not to be correct

revisedPossibles = []
for index, word in enumerate(newpossibles):
  # Test is used as a test mechanism to try and debug the weirdness 
  test=0
  for letter in incorrectLetters:
    
    # print(letter)
    if letter in word:
      test+=1 #NOPE! Multi letters. You need to keep the flag. Or use any :) smart!

      
  if test == 0:
    revisedPossibles.append(word)


revisedPossibles.sort()
print("Possibles:\n")
for i in revisedPossibles:
  print(i)