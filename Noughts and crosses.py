






def play():
    A1 = " "
    A2 = " "
    A3 = " "
    B1 = " "
    B2 = " "
    B3 = " "
    C1 = " "
    C2 = " "
    C3 = " "
    for turn in range(9):
        print("***TURN", turn + 1, "***")
        print("┌───┬───┬───┐")
        print("│", A1, "│", A2, "│", A3, "│")
        print("├───┼───┼───┤")
        print("│", B1, "│", B2, "│", B3, "│")
        print("├───┼───┼───┤")
        print("│", C1, "│", C2, "│", C3, "│")
        print("└───┴───┴───┘")
        if turn == 0 or turn == 2 or turn == 4 or turn == 6 or turn == 8:



            

            #crosses
            not_won = True
            print("Cross's go")
            not_played = True
            while not_played and not_won:
                play = input("Grid square: ")
                if play == "A1":
                    if A1 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        A1 = "X"
                        not_played = False
                if play == "A2":
                    if A2 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        A2 = "X"
                        not_played = False
                if play == "A3":
                    if A3 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        A3 = "X"
                        not_played = False
                if play == "B1":
                    if B1 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        B1 = "X"
                        not_played = False
                if play == "B2":
                    if B2 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        B2 = "X"
                        not_played = False
                if play == "B3":
                    if B3 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        B3 = "X"
                        not_played = False
                if play == "C1":
                    if C1 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        C1 = "X"
                        not_played = False
                if play == "C2":
                    if C2 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        C2 = "X"
                        not_played = False
                if play == "C3":
                    if C3 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        C3 = "X"
                        not_played = False
                

                

        #noughts
        else:
            print("Nought's go")
            not_played = True
            while not_played and not_won:
                play = input("Grid square: ")
                if play == "A1":
                    if A1 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        A1 = "O"
                        not_played = False
                if play == "A2":
                    if A2 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        A2 = "O"
                        not_played = False
                if play == "A3":
                    if A3 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        A3 = "O"
                        not_played = False
                if play == "B1":
                    if B1 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        B1 = "O"
                        not_played = False
                if play == "B2":
                    if B2 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        B2 = "O"
                        not_played = False
                if play == "B3":
                    if B3 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        B3 = "O"
                        not_played = False
                if play == "C1":
                    if C1 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        C1 = "O"
                        not_played = False
                if play == "C2":
                    if C2 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        C2 = "O"
                        not_played = False
                if play == "C3":
                    if C3 !=  " ":
                        print("That square is full. Choose again.")
                    else:
                        C3 = "O"
                        not_played = False
        #PRINT GRID
        #print("***TURN", turn + 1, "***")
        #print("┌───┬───┬───┐")
        #print("│", A1, "│", A2, "│", A3, "│")
        #print("├───┼───┼───┤")
        #print("│", B1, "│", B2, "│", B3, "│")
        #print("├───┼───┼───┤")
        #print("│", C1, "│", C2, "│", C3, "│")
        #print("└───┴───┴───┘")
        #CHECK FOR WIN
        #crosses
        if A1 == "X" and A2 == "X" and A3 == "X":
            print("Crosses win!")
            not_won = False
        elif B1 == "X" and B2 == "X" and B3 == "X":
            print("Crosses win!")
        elif C1 == "X" and C2 == "X" and C3 == "X":
            print("Crosses win!")
            not_won = False
        elif A1 == "X" and B1 == "X" and C1 == "X":
            print("Crosses win!")
            not_won = False
        elif A2 == "X" and B2 == "X" and C2 == "X":
            print("Crosses win!")
            not_won = False
        elif A3 == "X" and B3 == "X" and C3 == "X":
            print("Crosses win!")
            not_won = False
        elif A1 == "X" and B2 == "X" and C3 == "X":
            print("Crosses win!")
            not_won = False
        elif C1 == "X" and B2 == "X" and A3 == "X":
            print("Crosses win!")
            not_won = False


        #noughts
        if A1 == "O" and A2 == "O" and A3 == "O":
            print("Noughts win!")
            not_won = False
        elif B1 == "O" and B2 == "O" and B3 == "O":
            print("Noughts win!")
        elif C1 == "O" and C2 == "O" and C3 == "O":
            print("Noughts win!")
            not_won = False
        elif A1 == "O" and B1 == "O" and C1 == "O":
            print("Noughts win!")
            not_won = False
        elif A2 == "O" and B2 == "O" and C3 == "O":
            print("Noughts win!")
            not_won = False
        elif A3 == "O" and B3 == "O" and C3 == "O":
            print("Noughts win!")
            not_won = False
        elif A1 == "O" and B2 == "O" and C3 == "O":
            print("Noughts win!")
            not_won = False
        elif C1 == "O" and B2 == "O" and A3 == "O":
            print("Noughts win!")
            not_won = False
        
        
        
    print("***GAME OVER***")
    print("┌───┬───┬───┐")
    print("│", A1, "│", A2, "│", A3, "│")
    print("├───┼───┼───┤")
    print("│", B1, "│", B2, "│", B3, "│")
    print("├───┼───┼───┤")
    print("│", C1, "│", C2, "│", C3, "│")
    print("└───┴───┴───┘")
                
            
            







        
        


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


chosen = True
while chosen == True:
    print("**NOUGHTS AND CROSSES**")
    print("1)Play game")
    print("2)Instructions/controls")
    print("3)Quit game")
    menu = input("Choice: ")
    
    if menu == 1 or menu == "1" or menu == "play" or menu == "Play":
        play()
    elif menu == 2 or menu == "2" or menu == "help" or menu == "instructions" or menu == "controls":
        pass
    elif menu == 3 or menu == "3" or menu == "quit" or menu == "close":
        chosen = False
