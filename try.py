

def Qusetion(question, A, B, C, D, answer):

    trile = 3
    score = 0

    vlide = False

    while not vlide:

        number_1 = input(question).lower()

        if number_1 == answer:

            if trile == 3:
                print("correct get one point")
                score += 1
            else:
                print("correct")
            vlide = True

        else:
            print("incorrect")
            trile -= 1
            print(" {} more chance left".format(trile))

        if trile == 0:
            vlide = True
            print("the answer is {}".format(answer))
    return score


game_1 = Qusetion("If you sew a group of people beat up one person what should you do? ",
                  print("A = go help the group of people beat up the person"),
                  print("B = go help that person you might gat beat up"),
                  print("c = call the police "),
                  print("d = run away do nothing"),
                  "c")

game_2 = Qusetion("what is the answer for Q2 ",
                  print("A = tie"),                                                                                           
                  print("B = ti"),
                  print("c = i"),
                  print("d = t"),
                  "c")

total = game_1 + game_2
print("you have got {}".format(total))

