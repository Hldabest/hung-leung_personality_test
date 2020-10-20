#This project is to help people understand more about themselves

print("Title of program: Hung Leung personality test")
print()
print("Welcome to the test! Please answer the following questions truthfully and you'll learn more about yourself!")
print("Please respond with a number 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()

happy1 = input("I am happy every day.")
happy2 = input("I am grateful for what I have now.")
sad1 = input("I am always sad.")
sad2 = input("I am having a tough time in life now.")
extrovert1 = input("I love to meet new people.")
extrovert2 = input("At parties, I usually talk to strangers.")
introvert1 = input("I rarely attempt to meet new people.")
introvert2 = input("I only talk to my close friends.")

happy_final = int(happy1) + int(happy2)
sad_final = int(sad1) + int(sad2)
extrovert_final = int(extrovert1) + int(extrovert2)
introvert_final = int(introvert1) + int(introvert2)

print()

if happy_final > sad_final:
  print("you are a happy person")
else:
  print("you are a sad person")

if extrovert_final > introvert_final:
  print("you are an extrovert")
else:
  print("you are an introvert")
