

def Qusetion_1 (something):

    trile = 3

    vlide = False

    while not vlide:
        print("Q1 what is something")
        print("A = something")
        print("B = asdh")
        print("C = ghfhd")
        print("D = ghdls")

        answer = "a"

        number_1 = input(something).lower()

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
    return""

def Qusetion_2 (something):

    trile = 3

    vlide = False

    while not vlide:
        print("Q2 what is something")
        print("A = something")
        print("B = asdh")
        print("C = ghfhd")
        print("D = ghdls")

        answer = "c"

        number_2 = input(something).lower()

        if number_2 == answer:

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
    return""

score = 0

game_1 = Qusetion_1("what is the answer for Q1 ")

game_2 = Qusetion_2("what is the answer for Q2 ")

print(score)
