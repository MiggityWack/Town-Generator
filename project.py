import random

class Town:
    def __init__(self, size):
        self.size = size
        self.houses = []
        self.buildings = []
        self.stores = 0
        self.house_count = 0
        self.building_count = 0
        self.generate_houses()
        self.generate_buildings()
        self.population = len(Child.child_list) + len(Adult.unemployed_list) + len(Adult.employed_list)
        self.unemployed_jobs()

    def display_people():
        for x in


    def unemployed_jobs(self):
        for x in Adult.unemployed_list:
            seed = random.randrange(0,2,1)
            if x[3] > 60:
                x = [x[0], "Retired", x[2], x[3]]
            if(seed == 0):
                f = open(
                    r"C:\Users\jaden\OneDrive\Documents\Northeastern\Northeastern\2022 Spring\Computing Fundamentals\final project\homejobs.txt")
                home_jobs = f.read()
                home_jobs_parced = home_jobs.split("\n")
                seed2 = random.randrange(0,len(home_jobs_parced)-1,1)
                home_job = home_jobs_parced[seed2]
                new_jobholder = Adult.unemployed_list[0][0], home_job, Adult.unemployed_list[0][2], Adult.unemployed_list[0][3]
                Adult.employed_list.append([new_jobholder])
                Adult.unemployed_list.pop(0)


    def generate_buildings(self):
        if self.size == "Small":
            building_count = random.randrange(1,4,1)
        if self.size == "Medium":
            building_count = random.randrange(4, 9, 1)
        if self.size == "Large":
            building_count = random.randrange(10, 16, 1)
        i = 0
        while i < building_count:
            self.random_building()
            i += 1
        return()
    def generate_houses(self):
        if self.size == "Small":
            house_count = random.randrange(4,10,1)
        if self.size == "Medium":
            house_count = random.randrange(12, 18, 1)
        if self.size == "Large":
            house_count = random.randrange(24, 35, 1)
        i = 0
        while i < house_count:
            self.random_house()
            i += 1
        return()

    def random_building(self):
        b = Building()
        self.buildings += [[b.name], [len(b.workers)]]
        self.building_count += 1

    def random_house(self):
        house_size = random.randrange(0,2,1)
        if house_size == 0:
            h = House("Small")
        if house_size == 1:
            h = House("Medium")
        if house_size == 2:
            h = House("Large")
        self.houses += [[h.name],[h.r_count]]
        self.house_count += 1
class Adult:
    kind = "person"
    unemployed_list = []
    unemployed_list = list(unemployed_list)
    employed_list = []
    employed_list = list(employed_list)
    def __init__(self, house, job):
        self.gender = None
        self.name = None  # first name will be randomized, last name will be the household name, blank until generated later
        self.house = house  # last name/house they live in
        self.assign_gender()  # the gender of the person
        self.give_name(self.gender)
        self.age = 0
        self.give_age()
        self.full_name = self.name + " " + self.house
        self.job = job
        Adult.unemployed_list += [(self.full_name,self.job, self.gender, self.age)]

    def give_age(self):
        seed1 = random.randrange(17, 85, 1)
        seed2 = random.randrange(17, 85, 1)
        if seed1 <= seed2:
            self.age = seed1
        else:
            self.age = seed2
    def assign_gender(self):
        gender_seed = random.randrange(0, 2, 1)
        if gender_seed == 0:
            self.gender = "female"
        if gender_seed == 1:
            self.gender = "male"

    def give_name(self, gender):
        if gender == "male":
            self.name = self.random_male_name(
                r"C:\Users\jaden\OneDrive\Documents\Northeastern\Northeastern\2022 Spring\Computing Fundamentals\final project\malenames.txt")
        if gender == "female":
            self.name = self.random_female_name(
                r"C:\Users\jaden\OneDrive\Documents\Northeastern\Northeastern\2022 Spring\Computing Fundamentals\final project\femalenames.txt")

    def random_male_name(self, names):
        f = open(names)
        name_list = f.read()
        name_list_parced = name_list.split()
        seed = random.randrange(0, len(name_list_parced)-1, 1)
        self.name = name_list_parced[seed]
        return (self.name)

    def random_female_name(self, names):
        f = open(names)
        name_list = f.read()
        name_list_parced = name_list.split()
        seed = random.randrange(0, len(name_list_parced)-1, 1)
        self.name = name_list_parced[seed]
        return (self.name)


class Child:
    kind = "person"
    child_list = []
    child_list = list(child_list)
    def __init__(self, house):
        self.gender = None
        self.name = None  # first name will be randomized, last name will be the household name, blank until generated later
        self.house = house  # last name/house they live in
        self.assign_gender()  # the gender of the person
        self.give_name(self.gender)
        self.age = random.randrange(1, 16, 1)  # the age of the person
        self.full_name = self.name + " " + self.house
        Child.child_list += [(self.full_name, self.gender, self.age)]

    def assign_gender(self):
        gender_seed = random.randrange(0, 2, 1)
        if gender_seed == 0:
            self.gender = "female"
        if gender_seed == 1:
            self.gender = "male"

    def give_name(self, gender):
        if gender == "male":
            self.name = self.random_male_name(
                r"C:\Users\jaden\OneDrive\Documents\Northeastern\Northeastern\2022 Spring\Computing Fundamentals\final project\malenames.txt")
        if gender == "female":
            self.name = self.random_female_name(
                r"C:\Users\jaden\OneDrive\Documents\Northeastern\Northeastern\2022 Spring\Computing Fundamentals\final project\femalenames.txt")

    def random_male_name(self, names):
        f = open(names)
        name_list = f.read()
        name_list_parced = name_list.split()
        seed = random.randrange(0, 2942, 1)
        self.name = name_list_parced[seed]
        return (self.name)

    def random_female_name(self, names):
        f = open(names)
        name_list = f.read()
        name_list_parced = name_list.split()
        seed = random.randrange(0, 5003, 1)
        self.name = name_list_parced[seed]
        return (self.name)


class Store:
    kind = "building"
    store_list = []
    store_list = list(store_list)
    def __init__(self, name, size, type):
        self.name = name
        self.size = size
        self.type = type


class House:
    kind = "building"
    house_list = []
    house_list = list(house_list)
    def __init__(self, size, name=""):
        self.name = self.generate_name()
        self.size = size
        self.a_count = 0  # number of adults
        self.c_count = 0  # number of children
        self.r_count = 0  # number of residents
        self.random_people_count(self.size)
        self.residents = []
        self.generate_residents(self.c_count, self.a_count)
        House.house_list += [self.name, self.residents]

    def generate_residents(self, children, adults):
        i = 0
        j = 0
        temp_childs = []
        temp_adults = []
        while i < children:
            bonk = Child(self.name)
            temp_childs += [(bonk.name,bonk.age, bonk.gender)]
            i += 1
        while j < adults:
            bonk = Adult(self.name, "None")
            temp_adults += [(bonk.name, bonk.age, bonk.gender)]
            j += 1
        self.residents = [temp_childs + temp_adults]
        return()


    def generate_name(self):
        f = open(
            r"C:\Users\jaden\OneDrive\Documents\Northeastern\Northeastern\2022 Spring\Computing Fundamentals\final project\surnames.txt")
        name_list = f.read()
        name_list_parced = name_list.split()
        seed = random.randrange(0, 1000, 1)
        self.name = name_list_parced[seed]
        return self.name

    def random_people_count(self, size):
        if size == "Small":
            self.a_count = random.randrange(1, 3, 1)
            self.c_count = random.randrange(0, 2, 1)
        if size == "Medium":
            self.a_count = random.randrange(2, 4, 1)
            self.c_count = random.randrange(2, 5, 1)
        if size == "Large":
            self.a_count = random.randrange(2, 7, 1)
            self.c_count = random.randrange(3, 9, 1)
        self.r_count = self.a_count + self.c_count

    def headcount(self):
        return self.r_count

    def add_resident(self, firstname):
        self.residents += firstname

    def return_residents(self):
        for x in self.residents:
            print(x + " " + self.name)


class Building:
    kind = "building"
    building_list = []
    building_list = list(building_list)
    def __init__(self):
        self.type = ""
        self.pretitle = ""
        self.title = ""
        self.name = ""
        self.jobs = []  # the jobs that must be filled
        self.workers = []  # the workers
        self.determine_type()
        self.assign_workers()
        self.give_title()
        self.description = ""  # will give space for some quirks about the place
        self.designate_ownership()
        self.name_assembler()
        Building.building_list.append([self.name, self.type, self.workers])

    def designate_ownership(self):
        if self.title == "" and self.pretitle == "":
            name = self.workers[0][0]
            name_split = name.split(" ")
            seed = random.randrange(0,2,1)
            if seed == 0:
                self.pretitle = name_split[0] + "'s "
            if seed == 1:
                self.pretitle = name_split[1] + "'s "
    def assign_workers(self):
        for x in self.jobs:
            new_jobholder = Adult.unemployed_list[0][0], x, Adult.unemployed_list[0][2], Adult.unemployed_list[0][3]
            Adult.employed_list.append([new_jobholder])
            Adult.unemployed_list.pop(0)
            self.jobs.pop()

            self.workers += [[new_jobholder[0]], new_jobholder[1]]


    def name_assembler(self):
        if self.pretitle != "":
            self.name = self.pretitle + " " + self.type
        if self.title != "":
            self.name = self.type + " " + self.title

    def determine_type(self):
        f = open(
            r"C:\Users\jaden\OneDrive\Documents\Northeastern\Northeastern\2022 Spring\Computing Fundamentals\final project\jobsfixed.txt")
        type_list = f.read()
        type_list_parced = type_list.split("\n")
        seed = random.randrange(0, len(type_list_parced)-1, 1)
        type_info = type_list_parced[seed]
        list = type_info.split()
        self.type = list[0]
        i = 1
        while i < len(list):
            self.jobs += [list[i]]
            i += 1
        return ()

    def give_title(self):
        seed = random.randrange(0, 9, 1)
        if seed < 4:
            f = open(
                r"C:\Users\jaden\OneDrive\Documents\Northeastern\Northeastern\2022 Spring\Computing Fundamentals\final project\titles.txt")
            title_list = f.read()
            title_list_parced = title_list.split("\n")
            seed = random.randrange(0, 3, 1)
            self.title = title_list_parced[seed]
            return (self.title)
        if 8 >seed > 4:
            f = open(
                r"C:\Users\jaden\OneDrive\Documents\Northeastern\Northeastern\2022 Spring\Computing Fundamentals\final project\pretitles.txt")
            pretitle_list = f.read()
            pretitle_list_parced = pretitle_list.split("\n")
            seed = random.randrange(0, 3, 1)
            self.pretitle = pretitle_list_parced[seed]
            return (self.pretitle)




good_size = 0
while(good_size != 1):
    size = input("Input your size! Small, Medium, or Large?")
    if size != "Small" and size != "Medium" and size != "Large":
        print("Incorrect size given, remember to capitalize the first letter!")
    else:
        good_size = 1
t = Town(size)
print(t.size + " Sized Town Generated")
print("The Town has " + str(t.population) + " People, " + str(int(len(t.houses)/2)) + " Houses, and " + str(int(len(t.buildings)/2)) + " Other Buildings")
print("To view the Following Aspects, Enter the Number Given:")
print("1: The Houses")
print("2: The Other Buildings")
print("3: The People")
done = 0
while done != 1:
    aspect = input()
    if aspect == 1:
        t.display_houses()
    if aspect == 2:
        t.display_buildings()
    if aspect == 3:
        t.display_people()