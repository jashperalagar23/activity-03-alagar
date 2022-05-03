import a_stat as js
import a_ev as je

counter = 1
while counter == 1:
    print ("\n[1] Stat Calculator")
    print ("[2] EV Calculator")
    num0 = int(input("Choose number: "))

    Bas = int (input("\nBASE STATS:"))
    Level = int (input("LEVEL:"))
    Ev = int (input("EVHP:"))
    Iv = int (input("IVHP:"))
    Stats = int(input("Desired increase in stats:"))

    if num0 == 1:
        print ("\nHP = ", js.asper.hpcal(Bas,Iv,Ev,Level))
        print ("ATTACK = ", js.asper.otherstat(Bas,Iv,Ev,Level))
        print ("DEFENSE = ", js.asper.otherstat(Bas,Iv,Ev,Level))
        print ("SP. DEFENSE = ", js.asper.otherstat(Bas,Iv,Ev,Level))
        print ("SP. DEFENSE = ", js.asper.otherstat(Bas,Iv,Ev,Level))
        print ("SPEED = ", js.asper.otherstat(Bas,Iv,Ev,Level))
        print ("\nThe needed Evs to increase stats is ", je.zer.evneed(Bas,Stats,Iv,Ev,Level))
    
    elif num0 == 2:
        print ("\n[1] Single stats")
        print ("[2] All stats")
        num1 = int (input("Choose a number:"))

        if num1 == 1:
            print ("\n[1] ATTACK")
            print ("[2] DEFENSE")
            print ("[3] SP. ATTACK")
            print ("[4] SP. DEFENSE")
            print ("[5] SPEED")
            print ("[6] HP")
            num20= int (input ("Choose Stats:"))

            if num20 == 1 or 2 or 3 or 4 or 5:
                print ("\nThe Stats is", js.asper.otherstat(Bas,Iv,Ev,Level))
            elif num20 == 6:
                print ("\nHP = ", js.asper.hpcal(Bas,Iv,Ev,Level))

        elif num1 == 2:
            print ("\nHP =", js.asper.hpcal(Bas,Iv,Ev,Level))
            print ("ATTACK =", js.asper.otherstat(Bas,Iv,Ev,Level))
            print ("DEFENSE =", js.asper.otherstat(Bas,Iv,Ev,Level))
            print ("SP. ATTACK =", js.asper.otherstat(Bas,Iv,Ev,Level))
            print ("SP. DEFENSE =", js.asper.otherstat(Bas,Iv,Ev,Level))
            print ("SPEED =", js.asper.otherstat(Bas,Iv,Ev,Level))
    
    print ("\n[1] Perform another calculation")
    print ("[2] End the program")
    num3 = int (input("choose a number:"))
    if num3 ==2:
        break
    elif num3 == 1:
        continue