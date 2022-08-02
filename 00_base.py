# statement_generator function
def statement_generator(statement, decoration):

    side = decoration * 3

    statement = "{} {} {}".format(side, statement, side)
    top_bottom = decoration * len(statement)\

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return""

# information
def user(name):
    # question
    user_name = input(name)

def number_checker(age):

    user_age = int(input(age))

    # number checking
    if user_age >= 14:
        print("You should try the Cybersmart Youth Quiz but is all good to play our quiz")
        statement_generator("Let's start the Quiz ", "%")
        print()
    else:
        statement_generator("Let's start the Quiz ", "%")
        print()



# question function
def Qusetion(question,A ,B ,C ,D , answer):

    trile = 3
    score = 0

    vlide = False

    # Loop start
    while not vlide:

        # asking the question
        number_1 = input(question).lower()

        if number_1 == answer:

            # Checking the triles
            if trile == 3:
                statement_generator("correct get one point", "!")
                score += 1
            else:
                statement_generator("correct", "!")
            # Break the loop
            vlide = True

        else:
            statement_generator("incorrect", "^")
            trile -= 1
            statement_generator(" {} more chance left".format(trile), "+")

        if trile == 0:
            # Break the loop
            vlide = True
            statement_generator("the answer is {}".format(answer), "-")
    # returning the score
    return score

# start of the output
statement_generator("Hello ", "*")

statement_generator("Welcome to the game", "*")
print()

# asking name
user = user("What is your name")
# asking age
person = number_checker("How old are you")

# Question 1
game_1 = Qusetion("If you sew a group of people beat up one person what should you do? ",
                  print("A = go help the group of people beat up the person"),
                  print("B = go help that person you might gat beat up"),
                  print("c = call the police "),
                  print("d = run away do nothing"),
                  "c")
# Question2
game_2 = Qusetion("if your friend are start not play with you and start get away from you?",
                  print("A = find the problem on you and change them"),
                  print("B = start please them to play with you"),
                  print("C = don't care just be yourself"),
                  print("D = find a new friend abandon your old friend"), "c")

# Question 3
game_3 = Qusetion("if all of your friend are going to a same university but you don't like that university?",
                  print("A = just go to your friend's university friend are best."),
                  print("B = choose a university you like and abandon your friend."),
                  print("C = tall your friend to go to the university you like."),
                  print("D = keep contact with your friend and go to the university you like."), "d")

# Question 4
game_4 = Qusetion("Your friend sends you a text that is hurtful and makes you feel bad about yourself. What should you do?",
                  print("A = Go beat up your friend and tell him to shut up "),
                  print("B = don't care and go do some thing you like "),
                  print("C = go kill your self"),
                  print("D = sent a same text back "), "b")

# the total score calculation and print the score
total = game_1 + game_2 + game_3 + game_4
statement_generator("Your score is {} ".format(total), "&")
statement_generator("Thanks for doing the quiz", ")")
