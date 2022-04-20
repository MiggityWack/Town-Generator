import random
import citizen as Adult
import youngin as Child
import residence as House
import city as Town

good_size = 0
while (good_size != 1):
    size = input("Input your size! Small, Medium, or Large?")
    if size != "Small" and size != "Medium" and size != "Large":
        print("Incorrect size given, remember to capitalize the first letter!")
    else:
        good_size = 1
t = Town.Town(size)
print("\n\n\n\n\n"+ t.size + " Sized Town Generated")
print("The Town has " + str(t.population) + " People, " + str(int(len(t.houses) / 2)) + " Houses, and " + str(
    int(len(t.buildings) / 2)) + " Other Buildings")
print("To view the Following Aspects, Enter the Number Given:")
print("1: The Houses")
print("2: The Other Buildings")
print("3: The Adults")
print("4: The Children")
print("5: Exit")
done = 0
while done != 1:
    aspect = int(input("\n"))
    if aspect == 1:
        t.display_houses()
    if aspect == 2:
        t.display_buildings()
    if aspect == 3:
        done_adults = False
        start = 0
        last = 10
        while done_adults == False:
            t.display_adults(start, last)
            choice = input("For next list type N, for previous type P, to view a person, type their number, and to leave, type D")
            if choice == "N" or choice == "n":
                start += 10
                last += 10
            if choice == "P" or choice == "p" and start > 0:
                start -= 10
                last -= 10
            if choice == "P" or choice == "p" and start == 0:
                print("Cannot go to previous")
            if choice != "N" and choice != "P" and choice != "p" and choice != "n" and choice != "d" and choice != "D":
                t.display_adult(int(choice)-1)
            if choice == "D" or choice == "d":
                done_adults = True
    if aspect == 4:

        done_children = False
        start = 0
        last = 10
        while done_children == False:
            t.display_children(start, last)
            choice = input("For next list type N, for previous type P, to view a child, type their number, and to leave, type D")

            if choice == "N" or choice == "n":
                start += 10
                last += 10
            if choice == "P" or choice == "p" and start > 0:
                start -= 10
                last -= 10
            if choice == "P" or choice == "p" and start == 0:
                print("Cannot go to previous")
            if choice != "N" and choice != "P" and choice != "p" and choice != "n" and choice != "d" and choice != "D":
                t.display_child(int(choice) - 1)
            if choice == "D" or choice == "d":
               done_children = True
        if aspect == 5:
            done = True