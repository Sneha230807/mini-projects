print("Welcome!")
score = 0
answer1 = input("1. What is capital of India? ")
if answer1.lower() == "delhi":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
answer2 = input("2.National bird of India")
if answer2.lower() == "peacock":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
answer3 = input("3. What is the brain of the computer? ")
if answer3.lower() == "cpu":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
print("Quiz ended!")
print("Your total score is: " + str(score) + " out of 3")
