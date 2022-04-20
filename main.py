# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Building:
    kind = "building"

    def __init__(self, type, title):
        self.t = type  # the type of building
        self.d = ""  # will give space for some quirks about the place
        self.n = type + title  # the name, like "Museum" + " of the Dead"
        self.j = []  # the jobs that must be filled
        self.w = []  # the workers


class Adult:
    kind = "person"

    def __init__(self, house, job, name, attribute):
        self.n = ""  # first name will be randomized, last name will be the household name, blank until generated later
        self.h = house  # last name/house they live in
        self.j = job  # profession
        self.g = ""  # the gender of the person


class Child:
    kind = "person"

    def __init__(self, house, job, name, attribute):
        self.n = ""  # first name will be randomized, last name will be the household name, blank until generated later
        self.h = house  # last name/house they live in
        self.j = job  # profession
        self.g = ""  # the gender of the person
        self.a = 0 #the age of the person

    def assign_age(self):

        self.a = random.randrange(17,85,1)


class Store:
    kind = "building"

    def __init__(self, name, size, type):
        self.n = name
        self.s = size
        self.t = type


class House:
    kind = "building"

    def __init__(self, name, size):
        self.n = name
        self.s = size
        self.a = 0  # number of adults
        self.c = 0  # number of children
        self.r = 0  # number of residents

    def headcount(self):
        return self.r

    def add_r
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
