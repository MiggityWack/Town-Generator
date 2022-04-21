import city as Town
from tkinter import *
import tkinter as tk


def townmaker(args):
    global size
    size = args


root = Tk()
root.geometry("750x500")
var = tk.IntVar()
T = Text(root, height=10, width=1000)
l = Label(root, text="Town Generator")
l.config(font=("Courier", 16))
main_text = "Welcome to the Program! Select a size to make the town!"
bExit = Button(root, bg='red',text="Exit",
            command=root.destroy)
bSmall = Button(root,height=5,width=10,bg='light blue', text="Small", command=lambda: townmaker("Small"))
bMedium = Button(root,height=5,width=10,bg='light blue', text="Medium", command=lambda: townmaker("Medium"))
bLarge = Button(root,height=5,width=10,bg='light blue', text="Large", command=lambda: townmaker("Large"))
bGo = Button(root, text="Make it!",bg='green', command=root.destroy)
bSmall.place(x=250,y=220)
bMedium.place(x=350,y=220)
bLarge.place(x=450,y=220)
bGo.place(x=300,y=320)
bExit.place(x=400,y=320)
l.pack()
T.pack()
T.insert(tk.END, main_text)
tk.mainloop()

t = Town.Town(size)
print(t.size + " Sized Town Generated")
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
                t.display_adult(int(choice) - 1)
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
