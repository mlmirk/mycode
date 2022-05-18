#!/usr/bin/env python3
from pprint import pprint
def main():
    Gambit={'Real Name':'Remy LeBeau',
        'First Appearance':'Uncanny X-Men Annual #14 (July, 1990), Uncanny X-Men #266 (August, 1990)',
        'Creators':['Chris Claremont','Jim Lee'],
        'Team Affliations':['X-Factor','X-Men','Marauders','Horsemen of Apocalypse,'],'Base of Operations':'Salem Centre, New York'}

    #print(f"Gambit aka {Gambit['Real Name']} was created by two gents {Gambit['Creators'][0]} and {Gambit['Creators'][1]} he first appeared in {Gambit['First Appearance'][0]} on team {Gambit['Team Affliations'][0]}! ")
    
    Gambit['fav_food']='pizza'
    pprint(Gambit.keys())
    pprint("choose a key from above to show a value")
    userInput = input()
    temp = Gambit.get(userInput)
    pprint(f"Gambit's {userInput} is {temp }" )


main()
