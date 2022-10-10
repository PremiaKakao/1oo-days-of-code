print("Welcome to Treasure Island. Your mission is to find the treasure.")
step1 = input("Would you like to go towards Trixie Mattel holding a flag on the left or Katya Zamolodchikova holding "
              "a candle stick to the right?\n").lower()
if step1 == "left":
    step2 = input("Trixie blessed you with the power of Pride and informed you that to reach the treasure you must go "
                  "to the Enchanted lake.\nThere you have an option to take a luxurious ship called Titanic across or "
                  "swim to the other side which seems far far away.\nWill you ride or swim?\n").lower()
    if step2 == "ride":
        step3 = input("Titanic took you to a place with three doors.\nThe place is on land btw, that's how much better"
                      " Titanic DOO technology has become\nThere are three doors in front of you\n"
                      "Which door will you take? Red, the yellow or the blue?\n").lower()
        if step3 == "blue":
            print("Your stupid ass entered the main chambers of Poseidon's harem! Game over! You lose!\n"
                  "Unless you're into that")
        elif step3 == "red":
            print("When they said 'the floor is lava' they weren't kidding! You die and lose! Game over!")
        else:
            print("Congratulations! You have found the greatest treasure of all!\nThe friend you made along the way!")
    else:
        print("Game over loser! If one Titanic sank, that does not necessarily mean every single one will!\n"
              "Which part of 'far, far' away did you not understand?")
else:
    print("Katya engulfed your cheap wig in candle flames! Game over!")