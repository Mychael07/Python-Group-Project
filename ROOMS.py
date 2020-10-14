import main


def new_line():
    print("\n")


def accepted_invitation():
    print("You have been invited to the Breakers Mansion Costume Party. Please arrive at the the destination at 2100, "
          "and don't forget to dress up accordingly.")
    response = input("Do you want to play the game? ")
    if response == "yes":
        print("Excellent!")
        new_line()
        enter_house()
    elif response == "no":
        print("Well then, Goodbye......for now")


def enter_house():
    while True:
        print("You've enter and you see the butler")
        response = input("Welcome! Would you like me to take your coat? (yes or no) ")
        if response == "yes":
            print(" The butler takes you coat and says: Please do enjoy the party!")
            new_line()
            enter_parlor()
        elif response == "no":
            print(" Alright then, I guess if you ever get chilly...Please enjoy the party")
            new_line()
            enter_parlor()
            break
        break


def enter_parlor():
    print("You've entered the parlor and are immediately greeted by one of the waiters")
    response = input("Hello, would you care for a drink? (red or blue) ")
    if response == "red":
        print("Red? Excellent choice! The waiter hands you your drink")
        new_line()
    else:
        print("Blue? Excellent choice! The waiter hands you your drink")
        new_line()
    print("As you sip your drink, you enjoy the music and look at the various guests gathered around")
    print("While enjoying the party and talking to the other guest, you notice something strange\n")
    print("You see one the guests sway then drop to the floor in convulsions and begin foaming at the mouth!")
    main.kill()
    new_line()
    print("The music stops, and you hear a sinister voice through the speaker say 'Let the games begin!'\n")
    response = input("You have to play the killer's game to survive! What will do you? (play or refuse) ")
    if response == "play":
        print("You're gonna play? You may regret that decision soon enough..")
        new_line()
        enter_kitchen()
    else:
        print("Refuse? You want to refuse the killer's game? So be it.....")
        new_line()
        print(
            "'You think you're brave for refusing to play the game? Fool' You feel a piercing pain shoot through you "
            "and look down to see a blade through your chest.")
        print("You hear a chuckle and look back to see the waiter from "
              "before. He looks at you and says 'All you had to do was say yes'\n")
        response = input("You have died! See this through to the end and find the killer! Would like to try again? ("
                         "yes or no)")
        if response == "yes":
            new_line()
            enter_parlor()
        else:
            print("Giving up soon? Ah well...Thanks for playing!")


def enter_kitchen():
    print("You and the other guests enter the kitchen and look around There's nothing out the ordinary, "
          "just a dripping sink")
    print("Until, you notice that the dripping increases not only from the sink but also the ceiling")
    print(
        "Soon you hear pipes bursting and shriek as water quickly flows in the room! You race for the door but "
        "realize it has been locked behind you!\n")
    print(
        "The water is up to your waist now! You wade to the corner and notice a pair of valves. One blue and one red ")
    response = input("Which valve do you turn? (blue or red) ")
    if response == "blue":
        print(
            "You quickly reach for the blue valve and began to turn it. As you do, the water begins to cease flowing "
            "and  exits through a now opened drain")
        print("As your feet meet the ground once again, a door opens and you all rush through it ")
        new_line()
        enter_dining_room()
    else:
        print(
            "You quickly reach for the red valve and began to turn it. As you do, the water flow increases soon "
            "submersing you in water. With no way out, you and the other guests drown \n")
        response = input("You have died! See this through to the end and find the killer! Would like to try again? ("
                         "Yes or No)")
        if response == "yes":
            new_line()
            enter_kitchen()
        else:
            print("Giving up soon? Ah well...Thanks for playing!")


def enter_dining_room():
    print("You have now entered the dining room. The guests are very confused as to who the killer could be.")
    print("You are now sitting with the guests eating your meal before moving on. ")
    print("But one of the guests' food was poisoned!")
    main.kill()
    new_line()
    response = input(
        "Do you want to run to the next room? (yes or no) ")
    if response == "yes":
        enter_master_room()
    if response == "no":
        print("The other guests are not leaving you behind. Stay safe... for now.")
        enter_master_room()
        new_line()


def enter_master_room():
    print(
        "You are now in the master bedroom, but there is a huge storm raging outside and is thundering and lighting "
        "very hard.")
    response = input(
        "You hear a a loud boom from the thunder outside, the lights went out. "
        "Turn the lights back on. Do you want to go the attic or the basement? ")
    if response == "attic":
        print("Be careful and do not split up!")
        new_line()
        enter_attic()
    elif response == "basement":
        print("Be careful and do not split up!")
        new_line()
        enter_basement()


def enter_attic():
    print("You have made it safely to the attic but it is very dark and scary down here.")
    response = input(
        "The light switch is not up here. Do you want to meet the host and the group in the office? ")
    if response == "yes":
        print("Good choice.")
        new_line()
        enter_office()

    elif response == "no":
        print("Your friends are not allowing you to stay by yourself in the attic. You are now going to the office.")
        new_line()
        enter_office()


def enter_basement():
    print("You have entered the basement. It is very dark and scary down here.")
    response = input("Good job, the light switch is in the basement! "
                     "Do you want to meet the host a long with the group in the office? ")
    if response == "yes":
        print("Good choice.")
        new_line()
        enter_office()

    if response == "no":
        print("The other guests are not allowing you to stay by yourself in the basement. "
              "You are now going to the office.")
        new_line()
        enter_office()


def enter_office():
    print(
        "You meet the host in the office. The door locks behind you, no other way out. You all search in hopes of "
        "finding a way to get out ")
    response = input("You need to search too! But where? the desk or cabinet? ")
    if response == "desk" or "the desk":
        print("You approach the desk and begin to search through the drawers and find a remote there.")
        print(
            "You press the button and you hear click and part of the wall opens revealing a entryway. You all walk "
            "through it")
        new_line()
        guest_room()
    elif response == "cabinet" or "the cabinet":
        print(
            "You open the cabinet and see its filled with golden egyptian artifacts. You notice a silver artifact "
            "among them on the "
            "bottom shelf when you reach to grab it, it bend like a handle")
        print("You hear click and part of the wall opens revealing a entryway. You all walk through it")
        new_line()
        guest_room()


def guest_room():
    print("As you walk through the doorway you enter the guest room.")
    print("There is a lot of old paintings and old masks.")
    print("You need to find the mask that opens the door to the library"
          "There are three masks to choose from and two of them can open the door.")
    response = input("Which mask will you choose? (horse, crow, or shark)")
    if response == "horse" or "crow":
        print("Good job you can move onto the next room now.")
        new_line()
        enter_library()
    elif response == "shark":
        print(
            "Uh oh you chose wrong.. Now the killer is angry and the tasks are getting harder. Good luck with the "
            "next one.")
        new_line()
        enter_library()


def enter_library():
    print("You and the rest of the guests enter the grand library and you hear the door lock behind you")
    print("As you look around you see several bookshelves throughout the room separated by writing tables and desks ")
    print("What will the killer have you do here?")
    new_line()
    print("Instead of finding a needle in a haystack, find a key among the books will will unlock the door at the end "
          "of the room. If you don't find it in time,"
          "I will release toxic gas into the room and kill you all. Good Luck")
    print("You approach one of the many bookcases, this one is smaller than the rest with only 3 rows: fairytales,"
          "horror stories, and encyclopedias")
    response = input("Which row will you choose? (fairytales, horror, or encyclopedias) ")
    if response == "encyclopedias":
        print("You search through the books adorning the row and come across a book slightly out of place. You grab "
              "it and trail your fingers along the spine. You feel a lump there,find a letter opener to cut it, "
              "and get the key")
        print("You alert the other guests and unlock the door")
        new_line()
        enter_hallway()
    else:
        print(
            "You search through the books adorning that row but find nothing. Soon you hear a sound as cyanide gas "
            "fills the room. Death is imminent")
        response = input("You have died! See this through to the end and find the killer! Would like to try again? ("
                         "Yes or No)")
        if response == "yes":
            new_line()
            enter_library()


def enter_hallway():
    print("You all enter the hallway and are faced with several doors. A black door, an orange door, and a white door")
    print("You each have to choose a door to enter. Be Careful! That door may lead to your death.")
    response = input("Which door will you choose? (Black,orange, or white?) ")
    if response == "white":
        print("You enter through the door and you make out on the other side! But don't celebrate just yet....")
        print("You look around and notice that your group is smaller now, two others aren't here. Where did they go?")
        new_line()
        theater_room()
    else:
        print("You enter the door and the door slams behind you! You hear gears turning and is the room getting "
              "smaller?")
        print("Yes, yes it is! The walls are closing in, you run to the door and bang on it asking for help,but to no "
              "response")
        print("The walls are inching closer and closer. You shut your eyes....It is too late for you now")
        new_line()
        response = input("You have died! See this through to the end and find the killer! Would like to try again? ("
                         "Yes or No)")
        if response == "yes":
            new_line()
            enter_hallway()
        else:
            print("Giving up soon? Ah well...Thanks for playing!")


def theater_room():
    print("As you and the remaining people walk in there is a guy in a mask talking on the movie screen.")
    print("He says that there is going to be more people dying very soon and to watch your back.")
    response = input("The killer is directing you to the wine cellar and choose a drink the host gives you wisely."
                     "Choose the right door or the left door to get there.")
    if response == "right":
        new_line()
        enter_wine_cellar()
    else:
        print("Then you will have to go to the laundry room first.")
        new_line()
        enter_laundry_room()


def enter_laundry_room():
    print("You have entered the laundry room and now you have to complete your task."
          "It is a very simple task all you have to do it answer a simple riddle.")
    response = input("The riddle is: I look at you, you look at me, I show the opposite, but I show the same thing."
                     "hint- it is in a bathroom and is above your sink.")
    if response == "mirror":
        print("Good job! you will now go to the wine cellar with the guests.")
        new_line()
        enter_wine_cellar()
    else:
        print("Better luck next time")
        print("Due to your mistake")
        main.kill()
        new_line()
        enter_wine_cellar()


def enter_wine_cellar():
    print("You open the creaking door to the cellar. You and the remaining guests descend down the stairs")
    print("There you see several goblets placed in a row on a long ornate table")
    print("There is a golden jeweled goblet, a skull goblet, and an emerald goblet")
    new_line()
    print("Care for a drink? But be careful, choose the right cup and you live! But choose the wrong cup and you die")
    response = input("Be wise in your choice! Which goblet will you choose? (Golden,Skull,Emerald,) ")
    if response == "skull":
        print("You take a sip from the goblet and nothing happens")
        print("CRASH! Behind you,"
              " One of the guests has fallen along with their goblet,choking. You and the other rush "
              "to them but by then it is too late. "
              "There's nothing any of you could do and you watch in horror as their face "
              "begins to turn blue")
        main.kill()
        print("Just one? Really? For sure, I thought more of you would choose the wrong one. Ah well! There's more "
              "where that came from")
        print("You've survived..for now")
        new_line()
        enter_random_room()
    else:
        print("You take a sip from the ", response, "goblet and nothing happens")
        print(
            "Until a sudden feeling of tightness fills in your chest and you soon realize that you can't breathe!"
            " The guests rush over to assist but by then it is too late...")
        response = input("You have died! See this through to the end and find the killer! Would like to try again? ("
                         "Yes or No)")
        if response == "yes":
            new_line()
            enter_wine_cellar()
        else:
            print("Giving up soon? Ah well...Thanks for playing!")


def enter_random_room():
    print("You and the remaining guests enter the room and are faced with a large tv screen.")
    print(
        "The screen says 'Answer this riddle right and you all live! But answer wrong and you die. Got it? Here's the "
        "riddle:")
    response = input("While on my way to St. Ives, I saw a man with 7 wives. Each wife had 7 sacks. Each sack had 7 "
                     "cats.\n Each cat had 7 kittens. Kitten, cats, sacks, wives, How many were going to St. Ives?")
    if response == "one":
        print(
            "You give your answer hoping it is the right one. As the silence drags on, you hear a click and the door "
            "next to you opens")
        new_line()
        enter_hallway2()
    else:
        print(
            "You give your answer hoping it is the right one. As the silence drags on, you hear a sizzle as "
            "electricity runs through your body, cooking you from the inside")
        response = input("You have died! See this through to the end and find the killer! Would like to try again? ("
                         "Yes or No)")
        if response == "yes":
            new_line()
            enter_random_room()
        else:
            print("Giving up soon? Ah well...Thanks for playing!")


def enter_hallway2():
    print("You are meet with another spacious hallway with Knights lining both sides.")
    print("Near the end are 2 doors, one with a brass knob and another with a glass knob? ")
    response = input("Which knob will you turn? The glass or the brass (Answer with brass or glass)")
    if response == "brass":
        print(" You're sure? Absolutely Positive? Alright then... you turn the knob and enter the next room ")
        new_line()
        enter_random_room2()
    else:
        print(" You're sure? Absolutely Positive? Alright then... you turn the knob and enter the next room ")
        new_line()
        enter_random_room3()


def enter_random_room2():
    print(
        "You and the remaining guests enter the room and the door disappears! You look down notice the floor is "
        "adorned with different symbols: circles, diamonds, and squares")
    print("Only one path leads to the exit on the other side. Choose wisely or die!")
    response = input(
        "Which path will you choose? The circle path, the diamond path, or the square path (Answer with circle, "
        "diamond, or square)")
    if response == "square":
        print("You follow the path and safely make it across. You hears a scream behind you watch in horror one of "
              "the guests "
              "are burned alive!")
        main.kill()
        print("You have no choice but continue so you enter the now unlocked door")
        new_line()
        enter_finale()
    elif response == "circle" or "diamond":
        print("You follow the path and you make it to the middle of it when all of sudden, you feel heat and you look "
              "up and you see "
              "a blazing ring of fire come down on you. Burning you alive!")
        response = input("You have died! See this through to the end and find the killer! Would like to try again? ("
                         "Yes or No)")
        if response == "yes":
            enter_random_room2()
        else:
            print("Giving up soon? Ah well...Thanks for playing!")


def enter_random_room3():
    print("You hear muffled sobs as you enter the room.")
    print("You look and see one of the missing guests crying",
          "They run up to you all exclaiming ' The killer, he made us play for our lives in a game of chess! "
          "I didn't want to but I had no choice")
    print("You and your fellow guests look at the games table to see the other MIA guest face down on the chess table")
    main.kill()
    print(
        "The room erupts in shrieks,gasps, and cries as you gave upon their body. What kind of sick game is this? "
        "What will you do now?")
    response = input(
        "Will you continue to play into the killer's hand? Will you continue to play the game? (yes or no) ")
    if response == "yes":
        print("Then so be it..")
        new_line()
        enter_finale()
    else:
        print("If only you had a choice...")
        print("Your comrade drags you to the next room")
        enter_finale()


def enter_finale():
    print("This is the final room and you see that there's a working phone! You can call for help!")
    print("There is only two people remaining. "
          "You realize that the other person with you is the killer!")
    print("The truth is revealed! Congrats! Now will you get out of this damned house!")
    print(
        "They laugh as you realize who they really are. 'You have the played the game well so here's what I'll do. "
        "I'll let you live  ")
    print(
        "The storm outside brings great thunder that blinds you! As your visions readjusts, you find that the killer "
        "has disappeared!")
    response = input(
        "Congratulations you have made it to the phone and help is on the way. "
        "You survived. Would you like to play again?")
    if response == "yes":
        accepted_invitation()
    if response == "no":
        print("Good Game!")
