horn = 0
cup = 0
totalIce = 0

def stap1():
    global cup
    flavorList = []
    try:
        ice = int(input("Hoeveel bolletjes wilt u?\n"))
        if ice >= 1 and ice <= 3:
            for i in range(1, ice+1):
                flavor = smaakjes(i)
                flavorList.append(flavor)
            stap2(str(ice))
        elif ice >= 4 and ice <= 8:
            print("Dan krijgt u van mij een bakje met " + str(ice) + " bolletjes")
            cup += 1
            for x in range(1, ice+1):
                flavor = smaakjes(x)
                flavorList.append(flavor)
            stap3(str(ice), "bakje")
        else:
            print("Sorry, zulke grote bakken hebben we niet")
            stap1()
    except:
        print("Sorry dat snap ik niet...")
        stap1()

def smaakjes(bolletjeNummer):
    smaak = input("Welke smaak wilt u voor bolletje nummer " + str(bolletjeNummer) + "? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?\n").lower()
    if smaak == "a":
        return "aardbei"
    elif smaak == "c":
        return "chocolade"
    elif smaak == "m":
        return "munt"
    elif smaak == "v":
        return "vanille"
    else:
        print("Sorry dat snap ik niet...")
        smaakjes(bolletjeNummer)

def stap2(bolletjes):
    global horn
    global cup
    hornCup = input("Wilt u deze " + ice + " bolletje(s) in A) een hoorntje of B) een bakje?\n").lower()
    if hornCup != "hoorntje" and hornCup != "bakje":
        print("Sorry dat snap ik niet...")
        stap2(bolletjes)
    else:
        hoorn = horn + 1 if hornCup == "hoorntje" else horn + 0
        bakje = cup + 1 if hornCup == "bakje" else cup + 0
        stap3(ice, hornCup)

def stap3(ice, hornCup):
    global totalIce
    choice = input("Hier is uw " + hornCup + " met " + ice + " bolletje(s). Wilt u nog meer bestellen? (Y/N)\n").lower()
    if choice == "y":
        totalIce += int(ice)
        stap1()
    elif choice == "n":
       totalIce += int(ice)
        print("Bedankt en tot ziens!")
        bon(int(ice), hornCup)
    else:
        print("Sorry dat snap ik niet...")
        stap3(ice, hornCup)

def bonnetje(bolletjes, hornCup):
    totalIce = round(totalIce * 1.1, 2)
    totalHorn = round(horn * 1.25, 2)
    totalCup = round(cup * 0.75, 2)
    total = totalCup + totalHorn + totalIce
    print('---------["Papi Gelato"]---------')
    a = print("Bolletjes    " + str(totalIce) + " x 1.10   = " + str(totalIce)) if ice > 0 else 0
    b = print("Horrentje    " + str(horn) + " x 1.25   = " + str(totalHorn)) if horn > 0 else 0
    c = print("Bakje        " + str(cup) + " x 0.75   = " + str(totalCup)) if cup > 0 else 0
    print("                        ------ +\nTotaal                  = " + str(total))

print("Welkom bij Papi Gelato")

stap1()