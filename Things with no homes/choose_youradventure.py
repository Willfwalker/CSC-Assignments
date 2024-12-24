print("Welcome to Story time with Will, you will control this story")

fightorrun = input("In the trenches, you are awken by bombs, do you want to fight or run? (fight/run)").lower()

if fightorrun == "run":
    print("you sprint back through the trenches. Do you run to an escape car or motorcycle?").lower()
    motorcycleorcar = input("DO you choose the motorcycle or the car?")

    if motorcycleorcar == "car":
        print("you sprint to the car and start the car")
    else:
        print("you run to the motorcycle and speed off")

elif fightorrun == "fight":
    print("You grab your Gun and join your comrades on the frontline and help the fight.")
    twofriends = input("you see your two friends from back home fighting two differnt fights; do you help Josh or John?").lower()

    if twofriends == "josh":
        print("you rush to josh's side and help him in the fight and you all lose the battle")
    else: 
        print("you rush to john's side and help him in the fight and you all win the battle")

else: 
    print("You did not enter a valid option")