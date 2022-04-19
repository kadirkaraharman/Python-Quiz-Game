print("Welcome to my Geography quiz \t")

play = input("Do you wanna play ? (yes/no) : ")

#Checking game state
if play.lower() != "yes":
    quit()

print("Let's play :3 ")
score = 0

#First question 
answer = input("Which country has the largest population in the world? :")
if answer.lower() == "china":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#Second question
answer = input("What is the name of the longest river in Africa? :")
if answer.lower() == "the nile river":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
#Third question
answer = input("What U.S. state is home to no documented poisonous snakes? :")
if answer.lower() == "alaska":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#fourth question
answer = input("What is the capital of Canada? :")
if answer.lower() == "ottawa":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#Last question
answer = input("What country are the Great Pyramids of Giza located in? :")
if answer.lower() == "egypt":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#Final desicion
if score > 3:
    print("Good job, score = ",score)
else:
    print("Meh, score = ",score)
