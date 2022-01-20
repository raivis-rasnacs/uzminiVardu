import random

words = ["UMBRELLA", "CASTLE", "WINDOW", "TRACTOR", "COOKIE"]
word = random.choice(words)

lettersToRemove = int(len(words)/1.5)
hiddenLetters = []
for x in range(lettersToRemove):
  pos = random.randrange(0, len(word))
  if not word[pos] in hiddenLetters:
    hiddenLetters.append(word[pos])

editedWord = word
for x in hiddenLetters:
  editedWord = editedWord.replace(x, "_")

#GUESSING WORD
print("***GUESS THE WORD***")
wordGuessed = False

editedWordList = []
for letter in editedWord:
  editedWordList.append(letter)

while wordGuessed != True:
  
  def printWord():
    for letter in editedWordList:
      print(letter, end="")
  printWord()

  letter = input("\nEnter your guess!")
  letter = letter.upper()
  if letter in hiddenLetters:
    for x in range(len(word)):
      if letter == word[x]:
        editedWordList[x] = letter
    if "_" in editedWordList:
      continue
    else:
      printWord()
      print("\nWord guessed!")
      break