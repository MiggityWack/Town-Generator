import random
class Adult:
    kind = "person"
    unemployed_list = []
    unemployed_list = list(unemployed_list)
    employed_list = []
    employed_list = list(employed_list)

    def __init__(self, house, job):
        """initializes an adult"""
        self.gender = None
        self.name = None  # first name will be randomized, last name will be the household name, blank until generated later
        self.house = house  # last name/house they live in
        self.assign_gender()  # the gender of the person
        self.give_name(self.gender)
        self.age = 0
        self.give_age()
        self.full_name = self.name + " " + self.house
        self.job = job
        Adult.unemployed_list += [(self.full_name, self.job, self.gender, self.age)]

    def give_age(self):
        """gives them an age, rolling two ages and taking the lower"""
        seed1 = random.randrange(17, 85, 1)
        seed2 = random.randrange(17, 85, 1)
        if seed1 <= seed2:
            self.age = seed1
        else:
            self.age = seed2

    def assign_gender(self):
        """gives them a random binary gender"""
        gender_seed = random.randrange(0, 2, 1)
        if gender_seed == 0:
            self.gender = "female"
        if gender_seed == 1:
            self.gender = "male"

    def give_name(self, gender):
        """grants a first name, based on their gender, from an external list"""
        if gender == "male":
            self.name = self.random_name(
                r"Text Files/femalenames.txt")
        if gender == "female":
            self.name = self.random_name(
                r"Text Files/femalenames.txt")

    def random_name(self, names):
        """separates external .txt into a list, gets a random name, assigns it"""
        f = open(names)
        name_list = f.read()
        name_list_parced = name_list.split()
        seed = random.randrange(0, len(name_list_parced) - 1, 1)
        self.name = name_list_parced[seed]
        return (self.name)
