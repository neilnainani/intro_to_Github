"""
Write a function called "count_e" that takes in one string argument.  It should return the number of "e"s (uppercase or lowercase).
For instance,
count_e("Ello Poppet") --> 2
count_e("Hey Dude! What's happening?") --> 3
"""
def count_e(thing):
  testThing = thing.lower()
  finalCount = 0
  for num in range (0, len(thing)):
    if "e" in testThing[num]:
      finalCount = finalCount + 1
  if "e" in testThing:
    print("There were", finalCount, "e's in the text you submitted!")
  else:
    print("There were no e's in the text you submitted!")

uservar = input("Welcome to the E counter!\nType up a sentence and we will let you know how many e's there are in the sentence!\n")
count_e(uservar)
