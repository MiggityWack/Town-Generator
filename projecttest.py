import city as Town
from tkinter import *
import tkinter as tk


root = Tk()
root.geometry("750x500")
T = Text(root, height=10, width=1000)
l = Label(root, text="Town Generator")
l.config(font=("Courier", 16))
main_text = "Welcome to the Program! Select a size to make the town!"
b2 = Button(root, text="Exit",
            command=root.destroy)
bSmall = Button(root, text="Small", command=lambda:Town.size_chooser("Small"))
bMedium = Button(root, text="Medium", command=lambda:Town.size_chooser("Medium"))
bLarge = Button(root, text="Large", command=lambda:Town.size_chooser("Large"))
l.pack()
T.pack()
bSmall.pack()
bMedium.pack()
bLarge.pack()
b2.pack()
T.insert(tk.END, main_text)
tk.mainloop()

size = 0
t = Town.Town(size)
print("\n\n\n\n\n"+ t.size + " Sized Town Generated")
print("The Town has " + str(t.population) + " People, " + str(int(len(t.houses) / 2)) + " Houses, and " + str(
    int(len(t.buildings) / 2)) + " Other Buildings")
done = 0
while done != 1:
    print("To view the Following Aspects, Enter the Number Given:")
    print("1: The Houses")
    print("2: The Other Buildings")
    print("3: The Adults")
    print("4: The Children")
    print("5: Exit")
    aspect = int(input("\n"))
    if aspect == 1:
        done_houses = False
        start = 0
        last = 10
        while not done_houses:
            t.display_all_houses(start, last)
            choice = input(
                "For next list type N, for previous type P, to view a house, type their number, and to leave, type D")
            if choice == "N" or choice == "n":
                start += 10
                last += 10
            if (choice == "P" or choice == "p") and start > 0:
                start -= 10
                last -= 10
            if (choice == "P" or choice == "p") and start == 0:
                print("Cannot go to previous")
            if choice != "N" and choice != "P" and choice != "p" and choice != "n" and choice != "d" and choice != "D":
                t.display_house(int(choice) - 1)

            if choice == "D" or choice == "d":
                done_houses = True
    if aspect == 2:
        done_buildings = False
        start = 0
        last = 10
        while not done_buildings:
            t.display_all_buildings(start, last)
            choice = input(
                "For next list type N, for previous type P, to view a building, type their number, and to leave, type D")
            if choice == "N" or choice == "n":
                start += 10
                last += 10
            if choice == "P" or choice == "p" and start > 0:
                start -= 10
                last -= 10
            if choice == "P" or choice == "p" and start == 0:
                print("Cannot go to previous")
            if choice != "N" and choice != "P" and choice != "p" and choice != "n" and choice != "d" and choice != "D":
                t.display_building(int(choice) - 1)
            if choice == "D" or choice == "d":
                done_buildings = True
    if aspect == 3:
        done_adults = False
        start = 0
        last = 10
        while not done_adults:
            t.display_adults(start, last)
            choice = input("For next list type N, for previous type P, to view an adult, type their number, "
                           "and to leave, type D")
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
            choice = input("For next list type N, for previous type P, to view a child, type their number, "
                           "and to leave, type D")

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