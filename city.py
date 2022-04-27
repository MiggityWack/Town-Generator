import youngin as Child
import citizen as Adult
import residence as House
import workplace as Building
import random


class Town:
    def __init__(self, size):
        """initializes the town"""
        self.size = size #town sizeas given in the input
        self.houses = [] #list of houses
        self.buildings = [] #list of buildings
        self.stores = 0 #various counting vars
        self.house_count = 0
        self.building_count = 0
        self.generate_houses() #command to make houses and therefore people
        self.generate_buildings() #command to make buildings and therefore assign jobs
        self.population = len(Child.Child.child_list) + len(Adult.Adult.unemployed_list) + len(
            Adult.Adult.employed_list)
        self.unemployed_jobs() #assign retirement and at home jobs

    def display_building(self, index):
        """given an index, it will search through the children and display their age and gender """
        if index < len(Building.Building.building_list): #if the number asked for is a legal input
            print("      " + Building.Building.building_list[index][0] + " is a " +
                  Building.Building.building_list[index][1] + " with the following workers:")
            i = 0
            while i < len(Building.Building.building_list[index][2]): #print the workers, then their jobs
                if i % 2 == 0:
                    print("      " + str(int(((i + 2) / 2))) + ") " + str(
                        Building.Building.building_list[index][2][i][0]) + " is a ", end="")
                if i % 2 == 1:
                    print(str(Building.Building.building_list[index][2][i]))
                i += 1

    def display_all_buildings(self, start, finish):
        """given a range, it will display the first and last names of the adults between the two marks, unemployed
        and then employed """
        index = start
        finish = finish
        if finish > len(Building.Building.building_list): #if index goes too high, cut it off
            finish = len(Building.Building.building_list)
        while index < finish:
            print(str(index + 1) + ") " + Building.Building.building_list[index][0]) #print all building names
            index += 1

    def display_house(self, index):
        """given an index, it will search through the children and display their age and gender """
        print("      The " + str(House.House.house_list[index][0]) + " Household is a house with the following "
                                                                     "residents:")
        for x in House.House.house_list[index][1]:
            for y in x:
                if y[1] > 16:
                    print("      " + y[0] + " is a " + str(y[1]) + " year old " + y[2]) #print children
                if y[1] <= 16:
                    print("      " + y[0] + " is a " + str(y[1]) + " year old " + y[2]) #print adults

    def display_all_houses(self, start, finish):
        """given a range, it will display the first and last names of the adults between the two marks, unemployed
        and then employed """
        index = start
        finish = finish
        if finish > len(House.House.house_list):
            finish = len(House.House.house_list) #set max index
        while index < finish:
            print((str(int(index) + 1)) + ") The " + str(House.House.house_list[index][0]) + " Household") #print surnames and household
            index += 1

    def display_child(self, index):
        """given an index, it will search through the children and display their age and gender """
        if index < len(Child.Child.child_list): #if legal target
            print("      " + Child.Child.child_list[index][0] + " is a " + str(
                Child.Child.child_list[index][2]) + " year old " + Child.Child.child_list[index][1]) #print child details

    def display_children(self, start, finish):
        """given a range, it will display the first and last names of the adults between the two marks, unemployed
        and then employed """
        index = start
        if finish > len(Child.Child.child_list):
            finish = len(Child.Child.child_list) - 1 #if legal target
        while index < finish:
            print(str(index + 1) + ") " + Child.Child.child_list[index][0]) #print the names
            index += 1

    def display_adult(self, index):
        """given an index, it will search through the unemployed and then employed adults and display their
        attributes """
        if index < len(Adult.Adult.unemployed_list): #if the adult is unemployed
            print("      " + Adult.Adult.unemployed_list[index][0] + " is a " + str(
                Adult.Adult.unemployed_list[index][3]) + " year old " + Adult.Adult.unemployed_list[index][
                      2] + " with no job")
        if index >= len(Adult.Adult.unemployed_list): #if the adult is employed
            index -= len(Adult.Adult.unemployed_list) #reset index to only the adult list
            print(index)
            if index < len(Adult.Adult.employed_list):
                workplace = self.check_workplace(Adult.Adult.employed_list[index - 1][0][1]) #find if the adult works at a building
                if workplace == "":
                    print("      " + Adult.Adult.employed_list[index - 1][0][0] + " is a " + str(
                        Adult.Adult.employed_list[index - 1][0][3]) + " year old " +
                          Adult.Adult.employed_list[index - 1][0][2]) #print details except job
                    if Adult.Adult.employed_list[index][0][2] == "male": #if male, use he
                        print("      He works as a " + Adult.Adult.employed_list[index - 1][0][1])
                    if Adult.Adult.employed_list[index][0][2] == "female": #if female, use she
                        print("      She works as a " + Adult.Adult.employed_list[index - 1][0][1])
                if workplace != "": #if they work
                    print("      " + Adult.Adult.employed_list[index - 1][0][0] + " is a " + str(
                        Adult.Adult.employed_list[index - 1][0][3]) + " year old " +
                          Adult.Adult.employed_list[index - 1][0][2]) #print their job
                    if Adult.Adult.employed_list[index][0][2] == "male": #if male, use he
                        print("      He works as a " + Adult.Adult.employed_list[index - 1][0][1] + " at " + workplace)
                    if Adult.Adult.employed_list[index][0][2] == "female": #if female, use she
                        print("      She works as a " + Adult.Adult.employed_list[index - 1][0][1] + " at " + workplace)

    def check_workplace(self, job):
        """return if the person works somewhere"""
        for x in Building.Building.building_list: #return buildings
            for y in x[2]: #return jobs that the buildings have
                if job == y: #if there's a match
                    workplace = x[0] #set workplace and return
                    return workplace
        return False #else, False

    def display_adults(self, start, finish):
        """given a range, it will display the first and last names of the adults between the two marks, unemployed
        and then employed """
        #FOR ANY DOCUMENTATION, SEE DISPLAY_CHILDREN
        index = start
        finish = finish
        unemployed = 0
        while index < finish and unemployed == 0:
            if index > len(Adult.Adult.unemployed_list) - 1:
                finish -= index
                index = 0
                unemployed = 1
            else:
                print(str(index + 1) + ") " + Adult.Adult.unemployed_list[index][0])
                index += 1
        while index < finish and unemployed == 1:
            if index < len(Adult.Adult.employed_list):
                print(
                    str(index + 1 + len(Adult.Adult.unemployed_list)) + ") " + Adult.Adult.employed_list[index - 1][0][
                        0])
                index += 1
            else:
                unemployed = 2

    def unemployed_jobs(self):
        """will go through the list of unemployed adults and assign them either a job at home, keep them unemployed,
        or if they are old enough, retire them """
        for x in enumerate(Adult.Adult.unemployed_list):
            seed = random.randrange(0, 3, 1) #66% they get a home job, 33% they are unemployed
            if x[1][3] > 50: #if they are over 50, retire them
                Adult.Adult.unemployed_list.append([x[1][0], "Retired", x[1][2], x[1][3]])
                Adult.Adult.unemployed_list.pop(x[0]) #replace the old person instead of updating for ease
            if (seed == 0 or seed == 1): #66% chance as before
                f = open(
                    r"Text Files/homejobs.txt")
                home_jobs = f.read()
                home_jobs_parced = home_jobs.split("\n") #split into possible jobs
                seed2 = random.randrange(0, len(home_jobs_parced) - 1, 1) #pick one
                home_job = home_jobs_parced[seed2] #assign chosen
                new_jobholder = [Adult.Adult.unemployed_list[1][0], home_job, Adult.Adult.unemployed_list[1][2],
                                 Adult.Adult.unemployed_list[1][3]] #make new adult
                Adult.Adult.employed_list.append([new_jobholder]) #replace old adult
                Adult.Adult.unemployed_list.pop(x[0])

    def generate_buildings(self):
        """returns a random number of buildings based in ranges based on the town size"""
        if self.size == "Small":
            building_count = random.randrange(3, 7, 1) #small town, few buildings
        if self.size == "Medium":
            building_count = random.randrange(12, 18, 1) #medium town, more buildings
        if self.size == "Large":
            building_count = random.randrange(20, 30, 1) #large town, most buildings
        i = 0
        while i < building_count:
            self.random_building() #call the building making function until enough are made
            i += 1
        return ()

    def generate_houses(self):
        """returns a random number of houses of varying sizes based in ranges based on the town size"""
        if self.size == "Small":
            house_count = random.randrange(4, 10, 1) #small town, few houses
        if self.size == "Medium":
            house_count = random.randrange(14, 22, 1) #medium town, more houses
        if self.size == "Large":
            house_count = random.randrange(24, 35, 1) #large town, most houses
        i = 0
        while i < house_count:
            self.random_house() #call the house making function
            i += 1
        return ()

    def random_building(self):
        """creates a building, adds it to the list"""
        b = Building.Building() #make new building
        self.buildings += [[b.name], [len(b.workers)]] #add to list
        self.building_count += 1 #update count

    def random_house(self):
        """creates a house, adds it to the list"""
        house_size = random.randrange(0, 2, 1) #gives a random size to the building (will be used for population
        if house_size == 0:
            h = House.House("Small") #calls the house
        if house_size == 1:
            h = House.House("Medium") #calls the house
        if house_size == 2:
            h = House.House("Large") #calls the house
        self.houses += [[h.name], [h.r_count]] #adds it to the list
        self.house_count += 1 #count +1



