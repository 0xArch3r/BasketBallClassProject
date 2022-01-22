"""
Python Development Project
Basketball Stats
Author: Anthony Almaguer
"""

from constants import PLAYERS,TEAMS
from classes import *
from time import sleep
from menu_system import *

def assign_players(teams, players):
    if len(players) % len(teams) != 0:
        raise ValueError(f"Not enough players to divide equally amongst {len(teams)} teams!!!")

    inexp = []
    exp = []

    for plyr in players:
        if plyr['experience'] == "YES":
            exp.append(plyr)
        else:
            inexp.append(plyr)

    mod_teams = len(exp) % len(teams)
    if mod_teams != 0:
        print(f"WARNING: {mod_teams} will be short one experienced player")

    def roundrobin_players(exp,inexp):
        for p in exp:
            plyr = player(p['name'],p['guardians'],p['experience'],p['height'])
            yield plyr
        for p in inexp:
            plyr = player(p['name'],p['guardians'],p['experience'],p['height'])
            yield plyr

    x = roundrobin_players(exp,inexp)

    count = len(players)
    while count > 0:
        for team in teams:
            team.add_player(next(x))
            count -= 1


def main():
    # Importing Data
    my_teams = []
    for t in TEAMS:
        my_teams.append(team(t))

    assign_players(my_teams, PLAYERS)
    # End Importing Data

    while True:
        main_menu = menu("Main Menu")
        main_menu.add_to_menu("Display Team Statistics")
        main_menu.add_to_menu("Exit")
        main_menu.display_menu()


        choice = input("\nPlease select an option: ")

        if choice == "1":
            team_menu = menu("Team Selection")
            counter = 1
            for t in my_teams:
                team_menu.add_to_menu(t.name())
                counter += 1
            team_menu.display_menu()
            choice = input("\nPlease select a team: ")

            try:
                choice = int(choice)
                my_teams[choice - 1].get_stats()
                input("Press Enter to Continue...")
            except:
                raise ValueError(f"{choice} is not a valid option")
        elif choice == "2":
            exit()
        else:
            print('Not a valid choice')
            sleep(1)





    #for t in my_teams:
    #    print(t.name())
    #    print("=" * 10)
    #    for x in t.list_players():
    #        print(f"{x.name()} | {x.experience()}")
    #    print("\n")


if __name__ == "__main__":
    main()

