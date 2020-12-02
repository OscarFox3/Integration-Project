import random  # Random module used for random number generation

"""StarDraft"""
"""This program is for creating fantasy NBA lineups by drafting 5 NBA.
players for each lineup and competing against a friend based on their
players in-game performance."""
__author__ = "Oscar Fox"


def roll_dice():
    """Function for rolling a random number on a six-sided dice."""
    dice_number = random.randint(1, 6)  # Returns an integer number from the
    # specified range
    return dice_number


def sum_numbers(num_1, num_2, num_3, num_4, num_5):
    """Function for finding the sum of numbers"""
    # Parameter passing function
    sum_of_numbers = 0
    sum_of_numbers += num_1
    sum_of_numbers += num_2
    sum_of_numbers += num_3
    sum_of_numbers += num_4
    sum_of_numbers += num_5
    return sum_of_numbers  # Value returning function


def main():
    """Function for main program"""
    # Starpoints Values
    one_point = 1  # assignment operator
    three_point_shot = .5
    assist = 1
    rebound = 1
    block = 1.5
    steal = 1.5
    turnover = 2

    # Game Menu
    print("Welcome to StarDraft" + " By Oscar Fox")  # string addition operator
    print("Please enter a number from the menu below:")  # print function
    print("1. Start a Competition")
    print("2. How to Play")
    print("3. Quit")
    menu_choice = int(input())  # input function

    # Start Game
    if menu_choice == 1:  # relational operator equal

        # Assignment of competitors
        new_comp_1 = input("Please enter the name of the first competitor: ")
        new_comp_2 = input("Please enter the name of the second competitor: ")

        # Assignment of first draft pick
        print("Lets roll a dice to see who drafts an NBA player first.")
        print("The competitor with the biggest rolled number goes first.")
        print("If both competitors get the same number, re-roll.")

        comp_roll = False  # Not valid roll of dice

        # Used in most programming languages
        while comp_roll != True:  # While loop with condition and not-equal-to
            # relational operator
            comp_1_roll = roll_dice()  # Call to function roll_dice
            print(new_comp_1, "rolled the dice and got", comp_1_roll)
            comp_2_roll = roll_dice()
            print(new_comp_2, "rolled the dice and got", comp_2_roll)

            if comp_1_roll > comp_2_roll:  # Greater than relational operator
                print(new_comp_1, "goes first!")
                comp_1 = new_comp_1
                comp_2 = new_comp_2
                comp_roll = True

            elif comp_1_roll < comp_2_roll:  # Less than relational operator
                print(new_comp_2, "goes first!")
                comp_1 = new_comp_2
                comp_2 = new_comp_1
                comp_roll = True

            else:  # comp_1_roll == comp_2_roll
                print(new_comp_1, "and", new_comp_2, "re-rolled the dice.")
                comp_roll = False

        for num_of_players in range(1, 6):  # Range iterative structure
            print("StarDraft will ask for a NBA player", num_of_players,
                  "for each team.")

        # Entry of NBA players
        print("Each competitor cannot choose the same NBA player.")
        team_selection_player_1 = False
        while not team_selection_player_1:
            print(comp_1, "please enter the name of your first NBA player.")
            comp_1_player_1 = input()
            print(comp_2, "please enter the name of your first NBA player.")
            comp_2_player_1 = input()
            if not (comp_1_player_1 == comp_2_player_1):  # Boolean operator
                # Not
                break
            else:
                team_selection_player_1 = False

        team_selection_player_2 = False
        while not team_selection_player_2:
            print(comp_1, "please enter the name of your second NBA player.")
            comp_1_player_2 = input()
            print(comp_2, "please enter the name of your second NBA player.")
            comp_2_player_2 = input()
            if not (comp_1_player_2 == comp_2_player_2):
                break
            else:
                team_selection_player_2 = False

        team_selection_player_3 = False
        while not team_selection_player_3:
            print(comp_1, "please enter the name of your third NBA player.")
            comp_1_player_3 = input()
            print(comp_2, "please enter the name of your third NBA player.")
            comp_2_player_3 = input()
            if not (comp_1_player_3 == comp_2_player_3):
                break
            else:
                team_selection_player_3 = False

        team_selection_player_4 = False
        while not team_selection_player_4:
            print(comp_1, "please enter the name of your fourth NBA player.")
            comp_1_player_4 = input()
            print(comp_2, "please enter the name of your fourth NBA player.")
            comp_2_player_4 = input()
            if not (comp_1_player_4 == comp_2_player_4):
                break
            else:
                team_selection_player_4 = False

        team_selection_player_5 = False
        while not team_selection_player_5:
            print(comp_1, "please enter the name of your fifth NBA player.")
            comp_1_player_5 = input()
            print(comp_2, "please enter the name of your fifth NBA player.")
            comp_2_player_5 = input()
            if not (comp_1_player_5 == comp_2_player_5):
                break
            else:
                team_selection_player_5 = False

        print("Congratulations! Both NBA lineups have been created.")
        print("Return with the stats of your NBA players after the "
              "live games.")

        # comp_1 inputs player statistics
        print(comp_1, "you will now enter the stats of all five players you "
                      "drafted.")

        # Points
        print(comp_1, "please enter how many points", comp_1_player_1,
              "scored.")
        comp_1_player_1_p = int(input())
        print(comp_1, "please enter how many points", comp_1_player_2,
              "scored.")
        comp_1_player_2_p = int(input())
        print(comp_1, "please enter how many points", comp_1_player_3,
              "scored.")
        comp_1_player_3_p = int(input())
        print(comp_1, "please enter how many points", comp_1_player_4,
              "scored.")
        comp_1_player_4_p = int(input())
        print(comp_1, "please enter how many points", comp_1_player_5,
              "scored.")
        comp_1_player_5_p = int(input())

        # 3-point Shots
        print(comp_1, "please enter how many 3-point shots", comp_1_player_1,
              "scored.")
        comp_1_player_1_tp = int(input())
        print(comp_1, "please enter how many 3-point shots", comp_1_player_2,
              "scored.")
        comp_1_player_2_tp = int(input())
        print(comp_1, "please enter how many 3-point shots", comp_1_player_3,
              "scored.")
        comp_1_player_3_tp = int(input())
        print(comp_1, "please enter how many 3-point shots", comp_1_player_4,
              "scored.")
        comp_1_player_4_tp = int(input())
        print(comp_1, "please enter how many 3-point shots", comp_1_player_5,
              "scored.")
        comp_1_player_5_tp = int(input())

        # Assists
        print(comp_1, "please enter how many assists", comp_1_player_1, "had.")
        comp_1_player_1_a = int(input())
        print(comp_1, "please enter how many assists", comp_1_player_2, "had.")
        comp_1_player_2_a = int(input())
        print(comp_1, "please enter how many assists", comp_1_player_3, "had.")
        comp_1_player_3_a = int(input())
        print(comp_1, "please enter how many assists", comp_1_player_4, "had.")
        comp_1_player_4_a = int(input())
        print(comp_1, "please enter how many assists", comp_1_player_5, "had.")
        comp_1_player_5_a = int(input())

        # Rebounds
        print(comp_1, "please enter how many rebounds", comp_1_player_1,
              "had.")
        comp_1_player_1_r = int(input())
        print(comp_1, "please enter how many rebounds", comp_1_player_2,
              "had.")
        comp_1_player_2_r = int(input())
        print(comp_1, "please enter how many rebounds", comp_1_player_3,
              "had.")
        comp_1_player_3_r = int(input())
        print(comp_1, "please enter how many rebounds", comp_1_player_4,
              "had.")
        comp_1_player_4_r = int(input())
        print(comp_1, "please enter how many rebounds", comp_1_player_5,
              "had.")
        comp_1_player_5_r = int(input())

        # Blocks
        print(comp_1, "please enter how many blocks", comp_1_player_1, "had.")
        comp_1_player_1_b = int(input())
        print(comp_1, "please enter how many blocks", comp_1_player_2, "had.")
        comp_1_player_2_b = int(input())
        print(comp_1, "please enter how many blocks", comp_1_player_3, "had.")
        comp_1_player_3_b = int(input())
        print(comp_1, "please enter how many blocks", comp_1_player_4, "had.")
        comp_1_player_4_b = int(input())
        print(comp_1, "please enter how many blocks", comp_1_player_5, "had.")
        comp_1_player_5_b = int(input())

        # Steals
        print(comp_1, "please enter how many steals", comp_1_player_1, "had.")
        comp_1_player_1_s = int(input())
        print(comp_1, "please enter how many steals", comp_1_player_2, "had.")
        comp_1_player_2_s = int(input())
        print(comp_1, "please enter how many steals", comp_1_player_3, "had.")
        comp_1_player_3_s = int(input())
        print(comp_1, "please enter how many steals", comp_1_player_4, "had.")
        comp_1_player_4_s = int(input())
        print(comp_1, "please enter how many steals", comp_1_player_5, "had.")
        comp_1_player_5_s = int(input())

        # Turnovers
        print(comp_1, "please enter how many turnovers", comp_1_player_1,
              "had.")
        comp_1_player_1_t = int(input())
        print(comp_1, "please enter how many turnovers", comp_1_player_2,
              "had.")
        comp_1_player_2_t = int(input())
        print(comp_1, "please enter how many turnovers", comp_1_player_3,
              "had.")
        comp_1_player_3_t = int(input())
        print(comp_1, "please enter how many turnovers", comp_1_player_4,
              "had.")
        comp_1_player_4_t = int(input())
        print(comp_1, "please enter how many turnovers", comp_1_player_5,
              "had.")
        comp_1_player_5_t = int(input())

        print("Thank you ", comp_1, ", the stats of all five players have been"
                                    " recorded.", sep="")

        # comp_2 inputs player statistics
        print(comp_2, "you will now enter the stats of all five players you"
                      " drafted.")

        # Points
        print(comp_2, "please enter how many points", comp_2_player_1,
              "scored.")
        comp_2_player_1_p = int(input())
        print(comp_2, "please enter how many points", comp_2_player_2,
              "scored.")
        comp_2_player_2_p = int(input())
        print(comp_2, "please enter how many points", comp_2_player_3,
              "scored.")
        comp_2_player_3_p = int(input())
        print(comp_2, "please enter how many points", comp_2_player_4,
              "scored.")
        comp_2_player_4_p = int(input())
        print(comp_2, "please enter how many points", comp_2_player_5,
              "scored.")
        comp_2_player_5_p = int(input())

        # 3-point Shots
        print(comp_2, "please enter how many 3-point shots", comp_2_player_1,
              "scored.")
        comp_2_player_1_tp = int(input())
        print(comp_2, "please enter how many 3-point shots", comp_2_player_2,
              "scored.")
        comp_2_player_2_tp = int(input())
        print(comp_2, "please enter how many 3-point shots", comp_2_player_3,
              "scored.")
        comp_2_player_3_tp = int(input())
        print(comp_2, "please enter how many 3-point shots", comp_2_player_4,
              "scored.")
        comp_2_player_4_tp = int(input())
        print(comp_2, "please enter how many 3-point shots", comp_2_player_5,
              "scored.")
        comp_2_player_5_tp = int(input())

        # Assists
        print(comp_2, "please enter how many assists", comp_2_player_1, "had.")
        comp_2_player_1_a = int(input())
        print(comp_2, "please enter how many assists", comp_2_player_2, "had.")
        comp_2_player_2_a = int(input())
        print(comp_2, "please enter how many assists", comp_2_player_3, "had.")
        comp_2_player_3_a = int(input())
        print(comp_2, "please enter how many assists", comp_2_player_4, "had.")
        comp_2_player_4_a = int(input())
        print(comp_2, "please enter how many assists", comp_2_player_5, "had.")
        comp_2_player_5_a = int(input())

        # Rebounds
        print(comp_2, "please enter how many rebounds", comp_2_player_1,
              "had.")
        comp_2_player_1_r = int(input())
        print(comp_2, "please enter how many rebounds", comp_2_player_2,
              "had.")
        comp_2_player_2_r = int(input())
        print(comp_2, "please enter how many rebounds", comp_2_player_3,
              "had.")
        comp_2_player_3_r = int(input())
        print(comp_2, "please enter how many rebounds", comp_2_player_4,
              "had.")
        comp_2_player_4_r = int(input())
        print(comp_2, "please enter how many rebounds", comp_2_player_5,
              "had.")
        comp_2_player_5_r = int(input())

        # Blocks
        print(comp_2, "please enter how many blocks", comp_2_player_1, "had.")
        comp_2_player_1_b = int(input())
        print(comp_2, "please enter how many blocks", comp_2_player_2, "had.")
        comp_2_player_2_b = int(input())
        print(comp_2, "please enter how many blocks", comp_2_player_3, "had.")
        comp_2_player_3_b = int(input())
        print(comp_2, "please enter how many blocks", comp_2_player_4, "had.")
        comp_2_player_4_b = int(input())
        print(comp_2, "please enter how many blocks", comp_2_player_5, "had.")
        comp_2_player_5_b = int(input())

        # Steals
        print(comp_2, "please enter how many steals", comp_2_player_1, "had.")
        comp_2_player_1_s = int(input())
        print(comp_2, "please enter how many steals", comp_2_player_2, "had.")
        comp_2_player_2_s = int(input())
        print(comp_2, "please enter how many steals", comp_2_player_3, "had.")
        comp_2_player_3_s = int(input())
        print(comp_2, "please enter how many steals", comp_2_player_4, "had.")
        comp_2_player_4_s = int(input())
        print(comp_2, "please enter how many steals", comp_2_player_5, "had.")
        comp_2_player_5_s = int(input())

        # Turnovers
        print(comp_2, "please enter how many turnovers", comp_2_player_1,
              "had.")
        comp_2_player_1_t = int(input())
        print(comp_2, "please enter how many turnovers", comp_2_player_2,
              "had.")
        comp_2_player_2_t = int(input())
        print(comp_2, "please enter how many turnovers", comp_2_player_3,
              "had.")
        comp_2_player_3_t = int(input())
        print(comp_2, "please enter how many turnovers", comp_2_player_4,
              "had.")
        comp_2_player_4_t = int(input())
        print(comp_2, "please enter how many turnovers", comp_2_player_5,
              "had.")
        comp_2_player_5_t = int(input())

        print("Thank you ", comp_2, ", the stats of all five players have been"
                                    " recorded.", sep="")

        # Calculate total statistics and starpoints for both competitors

        # Calculate comp_1 total number of statistics
        comp_1_team_p = sum_numbers(comp_1_player_1_p, comp_1_player_2_p,
                                    comp_1_player_3_p, comp_1_player_4_p,
                                    comp_1_player_5_p)

        comp_1_team_tp = sum_numbers(comp_1_player_1_tp, comp_1_player_2_tp,
                                     comp_1_player_3_tp, comp_1_player_4_tp,
                                     comp_1_player_5_tp)

        comp_1_team_a = sum_numbers(comp_1_player_1_a, comp_1_player_2_a,
                                    comp_1_player_3_a, comp_1_player_4_a,
                                    comp_1_player_5_a)

        comp_1_team_r = sum_numbers(comp_1_player_1_r, comp_1_player_2_r,
                                    comp_1_player_3_r, comp_1_player_4_r,
                                    comp_1_player_5_r)

        comp_1_team_b = sum_numbers(comp_1_player_1_b, comp_1_player_2_b,
                                    comp_1_player_3_b, comp_1_player_4_b,
                                    comp_1_player_5_b)

        comp_1_team_s = sum_numbers(comp_1_player_1_s, comp_1_player_2_s,
                                    comp_1_player_3_s, comp_1_player_4_s,
                                    comp_1_player_5_s)

        comp_1_team_t = sum_numbers(comp_1_player_1_t, comp_1_player_2_t,
                                    comp_1_player_3_t, comp_1_player_4_t,
                                    comp_1_player_5_t)

        # Calculate comp_1 team starpoint values
        comp_1_team_p_s = comp_1_team_p * one_point  # multiplication operator
        comp_1_team_tp_s = comp_1_team_tp / three_point_shot  # division
        # operator
        comp_1_team_a_s = comp_1_team_a ** assist  # exponentiation operator
        comp_1_team_r_s = comp_1_team_r % rebound  # modulus operator
        comp_1_team_b_s = comp_1_team_b * block
        comp_1_team_s_s = comp_1_team_s * steal
        comp_1_team_t_s = comp_1_team_t // turnover  # floor division operator

        # Calculate comp_1 team total starpoints
        comp_1_team_total_s = 0
        comp_1_team_total_s_nums = [comp_1_team_p_s, comp_1_team_tp_s,
                                    comp_1_team_a_s, comp_1_team_r_s,
                                    comp_1_team_b_s, comp_1_team_s_s]
        for num in comp_1_team_total_s_nums:
            comp_1_team_total_s += num
            comp_1_team_total_s -= comp_1_team_t_s  # subtraction assignment
            # operator

        # Calculate comp_1 team extra starpoints
        if comp_1_team_p_s >= 10 and comp_1_team_a_s >= 10:  # Boolean operator
            # And
            comp_1_team_total_s += 20
        else:
            comp_1_team_total_s += 0

        if comp_1_team_t_s <= 10 or comp_1_team_s_s <= 10:  # Boolean operator
            # Or / Less-than-or-equal-to
            comp_1_team_total_s += 20
        else:
            comp_1_team_total_s += 0

        # Calculate comp_2 total number of statistics
        comp_2_team_p = 0
        comp_2_team_p_nums = [comp_2_player_1_p, comp_2_player_2_p,
                              comp_2_player_3_p, comp_2_player_4_p,
                              comp_2_player_5_p]
        for num in comp_2_team_p_nums:  # For loop iterative structure
            comp_2_team_p += num

        comp_2_team_tp = 0
        comp_2_team_tp_nums = [comp_2_player_1_tp, comp_2_player_2_tp,
                               comp_2_player_3_tp, comp_2_player_4_tp,
                               comp_2_player_5_tp]
        for num in comp_2_team_tp_nums:
            comp_2_team_tp += num

        comp_2_team_a = 0
        comp_2_team_a_nums = [comp_2_player_1_a, comp_2_player_2_a,
                              comp_2_player_3_a, comp_2_player_4_a,
                              comp_2_player_5_a]
        for num in comp_2_team_a_nums:
            comp_2_team_a += num

        comp_2_team_r = 0
        comp_2_team_r_nums = [comp_2_player_1_r, comp_2_player_2_r,
                              comp_2_player_3_r, comp_2_player_4_r,
                              comp_2_player_5_r]
        for num in comp_2_team_r_nums:
            comp_2_team_r += num

        comp_2_team_b = 0
        comp_2_team_b_nums = [comp_2_player_1_b, comp_2_player_2_b,
                              comp_2_player_3_b, comp_2_player_4_b,
                              comp_2_player_5_b]
        for num in comp_2_team_b_nums:
            comp_2_team_b += num

        comp_2_team_s = 0
        comp_2_team_s_nums = [comp_2_player_1_s, comp_2_player_2_s,
                              comp_2_player_3_s, comp_2_player_4_s,
                              comp_2_player_5_s]
        for num in comp_2_team_s_nums:
            comp_2_team_s += num

        comp_2_team_t = 0
        comp_2_team_t_nums = [comp_2_player_1_t, comp_2_player_2_t,
                              comp_2_player_3_t, comp_2_player_4_t,
                              comp_2_player_5_t]
        for num in comp_2_team_t_nums:
            comp_2_team_t += num

        # Calculate comp_2 team starpoint values
        comp_2_team_p_s = comp_2_team_p * one_point
        comp_2_team_tp_s = comp_2_team_tp / three_point_shot
        comp_2_team_a_s = comp_2_team_a ** assist
        comp_2_team_r_s = comp_2_team_r % rebound
        comp_2_team_b_s = comp_2_team_b * block
        comp_2_team_s_s = comp_2_team_s * steal
        comp_2_team_t_s = comp_2_team_t // turnover

        # Calculate comp_2 team total starpoints
        comp_2_team_total_s = 0
        comp_2_team_total_s_nums = [comp_2_team_p_s, comp_2_team_tp_s,
                                    comp_2_team_a_s, comp_2_team_r_s,
                                    comp_2_team_b_s, comp_2_team_s_s]
        for num in comp_2_team_total_s_nums:
            comp_2_team_total_s += num
            comp_2_team_total_s -= comp_2_team_t_s

        # Calculate comp_2 team extra starpoints
        if comp_2_team_p_s >= 10 and comp_2_team_a_s >= 10:
            comp_2_team_total_s += 20
        else:
            comp_2_team_total_s += 0

        if comp_2_team_t_s <= 10 or comp_2_team_s_s <= 10:
            comp_2_team_total_s += 20
        else:
            comp_2_team_total_s += 0

        # The competition results

        # comp_1 statistics
        print(comp_1, "'s team had a total of:\n",
              comp_1_team_p, " points.\n",
              comp_1_team_tp, " made 3-point shots.\n",
              comp_1_team_a, " assists\n",
              comp_1_team_r, " rebounds.\n",
              comp_1_team_b, " blocks.\n",
              comp_1_team_s, " steals.\n",
              comp_1_team_t, " turnovers.\n",
              comp_1_team_total_s, " starpoints.\n", sep="")

        # comp_2 statistics
        print(comp_2, "'s team had a total of:\n",
              comp_2_team_p, " points.\n",
              comp_2_team_tp, " made 3-point shots.\n",
              comp_2_team_a, " assists\n",
              comp_2_team_r, " rebounds.\n",
              comp_2_team_b, " blocks.\n",
              comp_2_team_s, " steals.\n",
              comp_2_team_t, " turnovers.\n",
              comp_2_team_total_s, " starpoints.\n", sep="")

        # Condition for winner
        if comp_1_team_total_s > comp_2_team_total_s:
            print(comp_1, "is the winner of the competition!!")
        elif comp_1_team_total_s < comp_2_team_total_s:
            print(comp_2, "is the winner of the competition!!")
        else:  # Tie if total starpoints are the same for comp_1 and comp_2
            print("The competition resulted in a tie!")

    # How to Play
    elif menu_choice == 2:
        print("StarDraft is a sports fantasy game where you are in control\n",
              "of drafting five NBA players for your team lineup. You can\n",
              "compete against a friend while watching live NBA games to\n",
              "see which individual lineup accumulates more starpoints\n",
              "based on in-game player statistics. Both individuals are\n",
              "given a salary cap of $100 and each NBA player is assigned\n",
              "a salary amount. For a lineup to be valid the total salary\n",
              "of all five NBA players must not be greater than the\n",
              "salary cap of $100. Each individual will roll a dice until\n",
              "one person which rolls the higher number will begin the\n",
              "contest. The winner of the draw will draft the first NBA\n",
              "player and then each individual will alternate taking turns\n",
              "drafting one NBA player until both lineups reach 5 players.\n",
              "After the live NBA game is finished each individual will\n",
              "enter the stats of their five NBA players and the individual\n",
              "with the most star points wins!")

    # Exit
    elif menu_choice == 3:
        print("See you again soon! Exiting.")
    else:  # User enters anything but 1, 2, or 3
        print("Invalid entry. Exiting. " * 2)  # string multiplication operator


# Call to main()
main()
