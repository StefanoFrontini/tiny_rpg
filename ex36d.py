from sys import exit
from random import randint
import winsound

# dead function
def dead(why):
    print why
    winsound.Beep(200, 300)
    winsound.Beep(200, 1000)
    print "Play again? (y/n)"
    choice = raw_input("> ")
    if "y" in choice:
        start()
    else:
        exit(0)

def win(why):
    print why
    winsound.Beep(200, 100)
    winsound.Beep(600, 100)
    winsound.Beep(800, 1000)
    print "Play again? (y/n)\n"
    choice = raw_input("> ")
    if "y" in choice:
        start()
    else:
        exit(0)
def fire_sword_select():
    global fire_sword
    global super_fire_sword
    dice_rolling = 0
    dice_rolling = randint(0, 2)
    if dice_rolling == 0 or dice_rolling == 1:
        print "After you recover you look inside the chest and you find a... Fire Sword!\n"
        fire_sword = True
    else:
        print "After you recover you look inside the chest and you find a... SUPER Fire Sword!\n"
        super_fire_sword = True

    door_choice()

def goblin_attack():
    dice_rolling = 0
    dice_rolling = randint(0, 2)
    if dice_rolling == 0:
        print "The goblin misses you!\n"
    else:
        print "The goblin hits you for %d\n" % dice_rolling
    return dice_rolling

def user_base_attack():
    dice_rolling = 0
    dice_rolling = randint(0, 2)
    return dice_rolling

def fire_sword_attack():
    dice_rolling = 0
    dice_rolling = randint(1, 3)
    return dice_rolling

def super_fire_sword_attack():
    dice_rolling = 0
    dice_rolling = randint(2, 4)
    return dice_rolling

def total_user_attack():
    if goblin_presence == True:
        monster = 'goblin'
    else:
        dead("Something has gone wrong! Sorry!")

    user_base_dmg = user_base_attack()
    fire_dmg = fire_sword_attack()
    super_dmg = super_fire_sword_attack()


    if user_base_dmg == 0:
        print "You miss the %s!\n" % monster
        return user_base_dmg

    elif user_base_dmg > 0 and fire_sword == True:
        print "You hit the %s for %d\n\t and an additional fire dmg of %d!\n" % (monster, user_base_dmg, fire_dmg)
        return user_base_dmg + fire_dmg

    elif user_base_dmg > 0 and super_fire_sword == True:
        print "You hit the %s for %d\n\t and an additional SUPER fire dmg of %d!\n" % (monster, user_base_dmg, super_dmg)
        return user_base_dmg + super_dmg

    else:
        print "You hit the %s for %d\n" % (monster, user_base_dmg)
        return user_base_dmg


# start of the game
def start():
    global user_hit_points
    user_hit_points = 10
    global fire_sword
    fire_sword = False
    global super_fire_sword
    super_fire_sword = False
    print "\nYou walk through the underground of an old castle looking for the King's treasure\n"
    print "You notice a large chest. Do you try to 'open' it or 'leave' it?\n"


    while True:
        choice = raw_input("> ")
        if "open" in choice:
            dice_rolling = 0
            dice_rolling = randint(4,5)
            user_hit_points = user_hit_points - dice_rolling
            print "\nYou hear a 'click', but it comes from a trap! you get burned by the flames!\n"
            print "You lose %d points and your health is now %d\n" % (dice_rolling, user_hit_points)
            fire_sword_select()
        elif "leave" in choice:
            door_choice()
        else:
            print "Man, don't piss me off you know!\n"


def door_choice():
    print "You carry on walking through the underground until you find two doors, 'left' or 'right'?\n"


    while True:
        choice = raw_input("> ")
        if "left" in choice:
            goblin_room()
        elif "right" in choice:
            dead("Wrong choice, you go insane and die. Bye bye!\n")
        else:
            print "Man, don't piss me off you know!\n"

#  goblin_room
def goblin_room():
    global user_hit_points
    global goblin_presence
    goblin_presence = True
    print "You open the door and you see a chest by the table and a goblin eating some food\n"
    print "How dare you to come here?\n"
    print "The goblin attacks you!\n"
    goblin_hit_points = 10

    i = 0
    # start of the fight
    while True:
        i += 1
        print "ROUND: %d\n" % i

        user_hit_points = user_hit_points - goblin_attack()

        if user_hit_points <= 0 and goblin_hit_points > 0:
            dead("You die!\n")
        else:
            goblin_hit_points = goblin_hit_points - total_user_attack()

            if user_hit_points > 0 and goblin_hit_points <= 0:
                print "You win!\n"
                winsound.Beep(200, 100)
                winsound.Beep(600, 100)
                winsound.Beep(800, 1000)
                goblin_presence = False
                gold_room()
            else:
                print "Your health is %d\n" % user_hit_points
                print "Goblin's health is %d\n" % goblin_hit_points
                print "Press 'Enter' for next round\n"
                raw_input("> ")

def gold_room():
    print "The chest behind the goblin is full of gold. How much do you take?\n"

    while True:
        choice = raw_input("> ")

        if "0" in choice or "1" in choice or "2" in choice or "3" in choice or "4" in choice or "5" in choice or "6" in choice or "7" in choice or "8" in choice or "9" in choice:
            how_much = int(choice)

            if how_much < 50:
                win("Nice, you're not greedy, you win!\n")

            else:
                dead("You greedy bastard!\n")

        else:
            how_much = "Man, don't piss me off you know!\n"
            print how_much



start()
