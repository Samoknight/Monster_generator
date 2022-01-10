print("hello world")

import pandas as pd

class Creature:
    def __init__(self, race = "None", job="None", level = 1):
        self.race = race
        self.job = job #Dictionary retun from function
        self.level = level
        self.statReset()
        # self. Creature class

    def statReset(self): # resets stats to race, job level defaults
        attrList = ["ATK", "DEF", "HP", "MP", "DEX", "CON"]
        self.Attributes = {}
        for elem in attrList:
            self.Attributes[elem] = self.StatCalc(elem)

    def Bonus(self,attr): # returns bonus to attribute from job
        job_data = pd.read_csv("C:\\Users\\Samuel\\Documents\\Python_projects\\Monster_project\\definition_files\\Job.csv")
        # print(f"{attr} = {int(boost)}") # print the stat
        return int(job_data.loc[job_data["Job"] == self.job, attr] )

    def StatCalc(self, attr):
        race_data = pd.read_csv("C:\\Users\\Samuel\\Documents\\Python_projects\\Monster_project\\definition_files\\" + self.race + ".csv")
        return int(race_data.loc[race_data["Level"] == self.level, attr]) + self.Bonus(attr)

    def ChangeJob(self, newJob): #Reset stats and apply new job bonuses
        self.job = newJob
        self.statReset()

class Humanoid(Creature):
    def __init__(self):
        super(Humanoid, self).__init__(race = "None", job="None", level = 1)
        self.abilities = []#  list of abilities for the purposes of randomly attacking in battle
        #need to find a way to auto list the abilities or group methods so only say the attack methods were called at random.
        
    def Tackle(self):
        #Standard humanoid attack
        print("Tackle")
        pass

class Dark_Creature(Creature):
    def __init__(self):
        self.weightClass = 5

    def Glare(self):
        # chance to lower dexterity of an opponent for a turn
        print("Glare")
        pass

class Goblin(Humanoid, Dark_Creature):
    def __init__(self):
        self.weakness = ["Fire","Dark"]
        self.resistances = ["Light"]
        self.weightClass = 1

    def Screech(self):
        #uses 1 MP to have a smallchance of reducing opponets chance to hit
        print("Screech")
        pass

Reega = Creature(race = "Goblin", job="Rouge", level = 2)
Goomba = Goblin(race = "Goblin", job="Warrior", level = 3)

Goomba.Screech()
print()
#Calling function from a list
# list[index posistion](arguments)
