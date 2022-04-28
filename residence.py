import youngin as Child
import citizen as Adult
import random
class House:
    kind = "building"
    house_list = []
    house_list = list(house_list)

    def __init__(self, size, name=""):
        """initialize the house class, run functions to create people"""
        self.name = self.generate_name()
        self.size = size #small, medium, or large
        self.a_count = 0  # number of adults
        self.c_count = 0  # number of children
        self.r_count = 0  # number of residents
        self.random_people_count(self.size) #gives an empty population based on size
        self.residents = []
        self.generate_residents(self.c_count, self.a_count) #make people to fill empty slots
        House.house_list.append([self.name, self.residents]) #add the residents to the house list

    def generate_residents(self, children, adults):
        """adds in children and adults, initializes their creation"""
        i = 0
        j = 0
        temp_childs = []
        temp_adults = []
        while i < children:
            bonk = Child.Child(self.name)
            temp_childs += [(bonk.name, bonk.age, bonk.gender)]
            i += 1
        while j < adults:
            bonk = Adult.Adult(self.name, "None")
            temp_adults += [(bonk.name, bonk.age, bonk.gender)]
            j += 1
        self.residents = [temp_childs + temp_adults]
        return ()

    def generate_name(self):
        """gives a surname to the house"""
        f = open(
            r"Text Files/surnames.txt")
        name_list = f.read()
        name_list_parced = name_list.split()
        seed = random.randrange(0, 1000, 1)
        self.name = name_list_parced[seed]
        return self.name

    def random_people_count(self, size):
        """assigns the population of the house based on the size"""
        if size == "Small":
            self.a_count = random.randrange(1, 3, 1)
            self.c_count = random.randrange(0, 3, 1)
        if size == "Medium":
            self.a_count = random.randrange(2, 4, 1)
            self.c_count = random.randrange(2, 5, 1)
        if size == "Large":
            self.a_count = random.randrange(3, 7, 1)
            self.c_count = random.randrange(4, 9, 1)
        self.r_count = self.a_count + self.c_count

    def headcount(self):
        """counts the residents"""
        return self.r_count

