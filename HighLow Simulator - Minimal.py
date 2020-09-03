run = True
import random
while run == True:
    tests = int(input("How many loops? Enter 0 to end."))
    if tests == 0:
        run = False
    else:
        finalScore = []
        while tests > 0:
            score = 1
            cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
            correct = True
            cardNumber = len(cards) - 1
            card = cards.pop(random.randint(0,cardNumber))
            #print("Drawn a " + str(card))
            while correct == True:
                drawn = False
                while drawn == False:
                    if card <= 7:
                        guess = "H"
                    elif card >= 8:
                        guess = "L"
                    #print("Player guesses " + str(guess))
                    cardNumber = len(cards) - 1
                    #print("Current size of deck is " + str(len(cards)))
                    newCard = cards.pop(random.randint(0,cardNumber))
                    #print("Drawn a " + str(newCard))
                    if score == 52:
                        drawn = True
                    elif newCard != card:
                        drawn = True
                    else:
                        cards.append(newCard)
                        #print("Returning card to deck")
                if score == 52:
                    correct = False
                elif guess == "L":
                    if newCard < card:
                        #print("Guessed lower correctly!")
                        score = score + 1
                        card = newCard
                    else:
                        #print("Guessed(H) incorrectly!")
                        correct = False
                elif guess == "H":
                    if newCard > card:
                        #print("Guessed higher correctly!")
                        score = score + 1
                        card = newCard
                    else:
                        #print("Guessed(L) incorrectly!")
                        correct = False
            finalScore.append(score)
            print("Test ended with a score of " + str(score) + ", " + str(tests) + " tests left!")
            tests = tests - 1
        print("List of scores " + str(finalScore))
        print("Average score of all the tested games " + str(sum(finalScore)/len(finalScore)))
        
    
