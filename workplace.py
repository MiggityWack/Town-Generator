import citizen as Adult
import random
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
        self.jobs = list(self.jobs)
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
            seed = random.randrange(0, 2, 1)
            if seed == 0:
                self.pretitle = name_split[0] + "'s "
            if seed == 1:
                self.pretitle = name_split[1] + "'s "

    def assign_workers(self):
        for x in self.jobs:
            new_jobholder = Adult.Adult.unemployed_list[0][0], x, Adult.Adult.unemployed_list[0][2], Adult.Adult.unemployed_list[0][3]
            Adult.Adult.employed_list.append([new_jobholder])
            Adult.Adult.unemployed_list.pop(0)
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
        seed = random.randrange(0, len(type_list_parced) - 1, 1)
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
        if 8 > seed > 4:
            f = open(
                r"C:\Users\jaden\OneDrive\Documents\Northeastern\Northeastern\2022 Spring\Computing Fundamentals\final project\pretitles.txt")
            pretitle_list = f.read()
            pretitle_list_parced = pretitle_list.split("\n")
            seed = random.randrange(0, 3, 1)
            self.pretitle = pretitle_list_parced[seed]
            return (self.pretitle)

