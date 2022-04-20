import random
class Child:
    kind = "person"
    child_list = []
    child_list = list(child_list)

    def __init__(self, house):
        """initializes child"""
        self.gender = None
        self.name = None  # first name will be randomized, last name will be the household name, blank until generated later
        self.house = house  # last name/house they live in
        self.assign_gender()  # the gender of the person
        self.give_name(self.gender)
        self.age = random.randrange(1, 16, 1)  # the age of the person
        self.full_name = self.name + " " + self.house
        Child.child_list += [(self.full_name, self.gender, self.age)]

    def assign_gender(self):
        """grants a random binary gender"""
        gender_seed = random.randrange(0, 2, 1)
        if gender_seed == 0:
            self.gender = "female"
        if gender_seed == 1:
            self.gender = "male"

    def give_name(self, gender):
        """chooses list to run name function with, assigns name"""
        if gender == "male":
            self.name = self.random_name(
                r"C:\Users\jaden\OneDrive\Documents\Northeastern\Northeastern\2022 Spring\Computing Fundamentals\final project\malenames.txt")
        if gender == "female":
            self.name = self.random_name(
                r"C:\Users\jaden\OneDrive\Documents\Northeastern\Northeastern\2022 Spring\Computing Fundamentals\final project\femalenames.txt")

    def random_name(self, names):
        """separates external .txt into a list, gets a random name, assigns it"""
        f = open(names)
        name_list = f.read()
        name_list_parced = name_list.split()
        seed = random.randrange(0, len(name_list_parced) - 1, 1)
        self.name = name_list_parced[seed]
        return (self.name)

