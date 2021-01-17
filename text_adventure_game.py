# Rachele Cort
# Safe Haven
# This code is a survival game where the user must input a decision that will effect the output of the game
print('Safe Haven')
print('Try to survive and make it somewhere safe!')
print('Available options are in CAPITAL letters or numbers')
print('Any other options exits the program')
print('type GO to start the game')

go = input('::')
if go == 'GO':
    print('You are at the mall')
    print('Do you want to go to Forever 21 or Tillys?')
    print('OPTIONS: go FOREVER 21 or TILLYS')
    shop = input('::')
    if shop == 'FOREVER21':
        print('You walk to Forever 21')
        print('Do you want to buy a crop top with that skirt?')
        print('OPTIONS: YES or NO')
        notneeded = input('::')

    elif shop == 'TILLYS':
        print('You go to Tillys')
        print('Do you want to buy a backpack and those jeans?')
        print('OPTIONS: YES or NO')
        notneeded2 = input('::')

    else:
        print('You can only do actions given')
        print('Try again')
        exit()
else:
    print('You can only do actions given')
    print('Try again')
    exit()
print('You drive home')
print('Your radio starts playing weird music')
print('You try fixing it but you loose control of the stirring wheel')
print('Do you swerve or brake?')
print('OPTIONS: SWERVE or BRAKE')

drive = input('::')
if drive == 'SWERVE':
    print('You hit a tree')
elif drive == 'BRAKE':
    print('You do not brake hard enough')
else:
    print('You can only do actions given')
    print('Try again')
    exit()

print('You are unconscious')
print('You see a figure in the distance')
print('Do you want to run or investigate?')
print('OPTIONS: RUN or INVESTIGATE')

run = input('::')
if run == 'RUN':
    print('You run back to the mall')
    print('You see a bunch of zombies walking around')
    print('Do you call for help')
    print('OPTIONS: YES or NO')
    yesorno = input('::')
    if yesorno == 'YES':
        print('You call 911')
        print('A pre recorded message starts playing')
        print('"ALL CITIZENS SHOULD STAY HOME AND LOCK THEIR DOORS')
    elif yesorno == 'NO':
        print('You gotta get out of here')
    else:
        print('You can only do actions given')
        print('Try again')
        exit()
    print('You decide to hotwire a car so you can leave')
    print('Do you want to go home to your friend Coles house or to the police station')
    print('OPTIONS: HOME, COLES HOUSE, or POLICE STATION')
    place = input('::')
    if place != 'POLICE STATION':
        print('You get to the house and see the door is wide open')
        print('You run in to see whats happening and a zombie attacks you!')
        print('YOU DIED')
        exit()
    elif place == 'POLICE STATION':
        print('You get to the police station but see no one around')
        print('Do you want to go inside')
        print('OPTIONS: YES or NO')
        yesorno1 = input('::')
        if yesorno1 == 'YES':
            print('You enter the police station theres still no one around')
            print('Do you want to investigate or leave')
            print('OPTIONS: INVESTIGATE or LEAVE')
            investorleave = input('::')
            if investorleave == 'INVESTIGATE':
                print('You look around and find the armory')
                print('You enter it and fine a hand gun on the table with 2 bullets')
                print('You think its a good idea to search around for more')
                print('How many minutes do you want to spend looking around')
                print('OPTIONS: Enter a number')
                num = input('::')
                if num < '5':
                    print('You didnt find any more ammo')
                    print('You leave the armory and theres a zombie in the halllway')
                    print('It sees you and starts running you')
                    print('You panic and miss both or your shots')
                    print('The zombie get you')
                    print('YOU DIED')
                    exit()
                elif num > '4':
                    print('You found 10 more bullets')
                    print('You leave the armory and theres a zombie in the halllway')
                    print('Do you want to run or shoot it?')
                    print('OPTIONS: RUN or SHOOT')
                    runorshoot = input('::')
                    if runorshoot == 'RUN':
                        print('you try to run but theres no where to go the zomebie catches you')
                        print('YOU DIED')
                        exit()
                    elif runorshoot == 'SHOOT':
                        print('You fire 3 bullets and the zombie falls')
                        print('You get back in your car and start driving')
                        print('You hear a message on the radio')
                        print('"THE MILITARY HAS ESTABLISHED A SAFE HAVEN AT THE GIANTS FOOTBALL STADIUM"')
                        print('You decide to go to the stadium because it sounds safe')
                        print('You come to a blockade in the road')
                        print('Do you want to get out and investigate or try to find another way around')
                        print('OPTIONS: GET OUT or FIND ANOTHER WAY')
                        getout = input('::')
                        if getout == 'GET OUT':
                            print('You get out and hear a man yell "HANDS UP"')
                            print('Do you want to run or fight')
                            print('OPTIONS: RUN or FIGHT')
                            runorfight = input('::')
                            if runorfight == 'RUN':
                                print('while you try to get back in your car and run you get shot')
                                print('YOU DIED')
                                exit()
                            elif runorfight == 'FIGHT':
                                print('You stay and fight')
                                print('While the man isnt looking you sneak around cover to get behind him')
                                print('Do you want to tell him to put his hands up or shoot him?')
                                print('OPTIONS: SHOOT or LET SURRENDER')
                                shootornot = input('::')
                                if shootornot == 'LET SURRENDER':
                                    print('You yell "PUT YOUR HANDS UP"')
                                    print('The man turns and shoots you')
                                    print('YOU DIED')
                                    exit()
                                elif shootornot == 'SHOOT':
                                    print('You shoot the man and he falls to the ground')
                                    print('You take some more ammo from the man and clear a path for your car')
                                else:
                                    print('You can only do actions given')
                                    print('Try again')
                                    exit()
                            elif getout == 'FIND ANOTHER WAY':
                                print('You find another path and continue on your drive')
                            else:
                                print('You can only do actions given')
                                print('Try again')
                                exit()
                            print('You arrive at the stadium and see a gate with soldiers from the military')
                            print('You drive up and they ask you to step out of the car')
                            print('You step out of the car and they search you for bite marks')
                            print('The soldier yells "Clean" and the gate opens')
                            print('You have made it and you are safe')
                            print('THE END')
                        else:
                            print('You can only do actions given')
                            print('Try again')
                            exit()
                    else:
                        print('You can only do actions given')
                        print('Try again')
                        exit()
                else:
                    print('You can only do actions given')
                    print('Try again')
                    exit()
            elif investorleave == 'LEAVE':
                print('You start driving with the radio on but most stations are static')
                print('You find one thats playing a message')
                print('"THE MILITARY HAS ESTABLISHED A SAFE HAVEN AT THE GIANTS FOOTBALL STADIUM"')
                print('Do you want to go to the football stadium')
                print('OPTIONS: YES or NO')
                yesorno2 = input('::')
                if yesorno2 == 'NO':
                    print('You decide not to go to the stadium and continue driving south')
                    print('You come to a blockade in the road')
                    print('You get out of the car to see if theres away around')
                    print('Then you hear "HANDS UP"')
                    print('Before you can react you get shot')
                    print('YOU DIED')
                    exit()
                elif yesorno2 == 'YES':
                    print('You start driving towards the stadium')
                    print('You come to a blockade in the road')
                    print('You get out of the car to see if theres away around')
                    print('Then you hear "HANDS UP"')
                    print('Before you can react you get shot')
                    print('YOU DIED')
                    exit()
                else:
                    print('You can only do actions given')
                    print('Try again')
                    exit()
            else:
                print('You can only do actions given')
                print('Try again')
                exit()
        elif yesorno1 == 'NO':
            print('You go to turn around but while backing up a zombie jump through the windshield!')
            print('The zomebie grabs you and bites you')
            print('YOU DIED')
            exit()
        else:
            print('You can only do actions given')
            print('Try again')
            exit()
    else:
        print('You can only do actions given')
        print('Try again')
        exit()
elif run == 'INVESTIGATE':
    print('You get close to the figure and see it looks dead like')
    print('The figure sees you and starts running towards you')
    print('You try to run but the zombie is to fast and it gets you')
    print('YOU DIED')
    exit()
else:
    print('You can only do actions given')
    print('Try again')
    exit()