import city as Town

good_size = 0 #make sure a legal size is chosen
while (good_size != 1):
    size = input("Input your size! Small, Medium, or Large?") #input from console
    if size != "Small" and size != "Medium" and size != "Large": #if not a choice, reask question
        print("Incorrect size given, remember to capitalize the first letter!")
    else:
        good_size = 1 #if good size, exit loop

t = Town.Town(size) #call town of given size
print("\n\n\n\n\n"+ t.size + " Sized Town Generated") #declare town
print("The Town has " + str(t.population-1) + " People, " + str(int(len(t.houses) / 2)) + " Houses, and " + str(
    int(len(t.buildings) / 2)) + " Other Buildings") #declare populations and counts
done = 0
while done != 1: #until they choose the finish option
    print("To view the Following Aspects, Enter the Number Given:")
    print("1: The Houses")
    print("2: The Other Buildings")
    print("3: The Adults")
    print("4: The Children")
    print("5: Exit")
    aspect = int(input("\n")) #pick a choice to look at
    if aspect == 1: #Houses !
        done_houses = False #when done, cancel loop
        start = 0 #first index
        last = 10 #last index
        while not done_houses:
            t.display_all_houses(start, last)
            choice = input(
                "For next list type N, for previous type P, to view a house, type their number, and to leave, type D")
            if choice == "N" or choice == "n": #If they want next
                start += 10 #progress 10
                last += 10
            if (choice == "P" or choice == "p") and start > 0: #if previous and not at start
                start -= 10 #go back 10
                last -= 10
            if (choice == "P" or choice == "p") and start == 0: #if previous and at start
                print("Cannot go to previous") #throw error
            if choice != "N" and choice != "P" and choice != "p" and choice != "n" and choice != "d" and choice != "D":
                t.display_house(int(choice) - 1) #else, it's a number, check it
            if choice == "D" or choice == "d":
                done_houses = True #if it's d, finish with done
    if aspect == 2: #Other Buildings !
        done_buildings = False #false to allow loop
        start = 0  # first index
        last = 10  # last index
        while not done_buildings:
            t.display_all_buildings(start, last) #show all between indexes
            choice = input(
                "For next list type N, for previous type P, to view a building, type their number, and to leave, type D")
            if choice == "N" or choice == "n":#If they want next
                start += 10#progress 10
                last += 10
            if choice == "P" or choice == "p" and start > 0:#if previous and not at start
                start -= 10
                last -= 10#go back 10
            if choice == "P" or choice == "p" and start == 0:#if previous and at start
                print("Cannot go to previous")
            if choice != "N" and choice != "P" and choice != "p" and choice != "n" and choice != "d" and choice != "D":
                t.display_building(int(choice) - 1)
            if choice == "D" or choice == "d":
                done_buildings = True
    if aspect == 3:
        done_adults = False #false to allow loop
        start = 0  # first index
        last = 10  # last index
        while not done_adults:
            t.display_adults(start, last)
            choice = input("For next list type N, for previous type P, to view an adult, type their number, "
                           "and to leave, type D")
            if choice == "N" or choice == "n":#If they want next
                start += 10#progress 10
                last += 10
            if choice == "P" or choice == "p" and start > 0:#if previous and not at start
                start -= 10
                last -= 10#go back 10
            if choice == "P" or choice == "p" and start == 0:#if previous and at start
                print("Cannot go to previous")
            if choice != "N" and choice != "P" and choice != "p" and choice != "n" and choice != "d" and choice != "D":
                t.display_adult(int(choice)-1)
            if choice == "D" or choice == "d":#if it's d, finish with done
                done_adults = True
    if aspect == 4:
        done_children = False #false to allow loop
        start = 0  # first index
        last = 10  # last index
        while done_children == False:
            t.display_children(start, last)
            choice = input("For next list type N, for previous type P, to view a child, type their number, "
                           "and to leave, type D")
            if choice == "N" or choice == "n":
                start += 10#progress 10
                last += 10
            if choice == "P" or choice == "p" and start > 0:#if previous and not at start
                start -= 10
                last -= 10#go back 10
            if choice == "P" or choice == "p" and start == 0:#if previous and at start
                print("Cannot go to previous")
            if choice != "N" and choice != "P" and choice != "p" and choice != "n" and choice != "d" and choice != "D":
                t.display_child(int(choice) - 1)
            if choice == "D" or choice == "d":#if it's d, finish with done
               done_children = True
        if aspect == 5:
            done = True#if it's 5, finish and exit program