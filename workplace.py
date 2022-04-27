import citizen as Adult
import random
class Building:
    kind = "building"
    building_list = []
    building_list = list(building_list) #list for future reference, double called to prevent tupling

    def __init__(self):
        """creates building, runs subfunctions"""
        self.type = "" #the type of building
        self.pretitle = "" #title that goes before they type for the name
        self.title = "" #title that goes after they type for the name
        self.name = "" #full name of the building
        self.jobs = []  # the jobs that must be filled
        self.jobs = list(self.jobs)
        self.workers = []  # the workers
        self.determine_type() #makes it a certain kind of building
        self.assign_workers() #finds adults to fill jobs
        self.give_title() #gives the building a title or pretitle
        self.description = ""  # will give space for some quirks about the place
        self.designate_ownership() #if no title, makes a worker "own" the shop
        self.name_assembler() #puts the name together
        Building.building_list.append([self.name, self.type, self.workers]) #adds it to the list

    def designate_ownership(self):
        """grants owning title"""
        if self.title == "" and self.pretitle == "":
            name = self.workers[0][0] #picks the first worker
            name_split = name.split(" ") #separates into first and last name
            seed = random.randrange(0, 2, 1) #random split between choosing last or first name for ownership
            if seed == 0:
                self.pretitle = name_split[0] + "'s "
            if seed == 1:
                self.pretitle = name_split[1] + "'s "

    def assign_workers(self):
        """gives the building its adult workers"""
        for x in self.jobs:
            new_jobholder = Adult.Adult.unemployed_list[0][0], x, Adult.Adult.unemployed_list[0][2], Adult.Adult.unemployed_list[0][3]
            Adult.Adult.employed_list.append([new_jobholder]) #add the adult with a job to the employed list
            Adult.Adult.unemployed_list.pop(0) #remove the person whos attributes you stole from existence
            self.workers += [[new_jobholder[0]], new_jobholder[1]] #the building gets the adult as its own

    def name_assembler(self):
        """puts name together using type and titles"""
        if self.pretitle != "": #if it got a pretitle add it
            self.name = self.pretitle + " " + self.type
        if self.title != "": #if it got a title, add it
            self.name = self.type + " " + self.title

    def determine_type(self):
        """gives type of building and assigns joblist"""
        f = open(
            r"Text Files/jobsfixed.txt")
        type_list = f.read()
        type_list_parced = type_list.split("\n") #split list by lines
        seed = random.randrange(0, len(type_list_parced) - 1, 1)
        type_info = type_list_parced[seed] #pick a line
        list = type_info.split() #split into type and then workers
        self.type = list[0]
        i = 1
        while i < len(list): #add jobs to the building
            self.jobs += [list[i]]
            i += 1
        return ()

    def give_title(self):
        """finds a random title for the building to use"""
        seed = random.randrange(0, 9, 1) #roll a d9 (11% it gets nothing, so ownership title)
        if seed < 4: #44% of the time add a title
            f = open(
                r"Text Files/titles.txt")
            title_list = f.read()
            title_list_parced = title_list.split("\n")
            seed = random.randrange(0, len(title_list_parced), 1)
            self.title = title_list_parced[seed]
            return (self.title)
        if 8 > seed > 4: #44% of the time add a pretitle
            f = open(
                r"Text FIles/pretitles.txt")
            pretitle_list = f.read()
            pretitle_list_parced = pretitle_list.split("\n")
            seed = random.randrange(0, len(pretitle_list_parced), 1)
            self.pretitle = pretitle_list_parced[seed]
            return (self.pretitle)

