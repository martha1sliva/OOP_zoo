##Parent class
class Animal(object):
    """A virtual animal"""
    
    ##information of animal
    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.hunger = 0
        self.visible = True

    ##prints animal's information
    def __str__(self):
        reply = "\n" + self.species + " Name: " + self.name
        if self.hunger <= 2:
            reply += "\nStatus: Fine\n"
        elif self.hunger ==3 or self.hunger ==4:
            reply += "\nStatus: Somewhat Hungry\n"
        elif self.hunger >= 5:
            reply += "\nStatus: HUNGRY\n"
        return reply

    ##animal loses one hunger point from pacing
    ##animal disappears if hunger level reaches 5
    def pace(self):
        if self.visible == True:
            self.hunger += 1
        if self.hunger == 5:
            self.visible = False
            print "Exhibit CLOSED: " + self.name + "!\n"

    ##compares hunger to other animals
    ##this determines which animal the zookeeper feeds
    def __cmp__(self, other):
        if self.hunger > other.hunger:
            return 1
        elif self.hunger == other.hunger:
            return 0
        elif self.hunger < other.hunger:
            return -1     

class Facility(object):
    """A virtual facility"""
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    ##prints all open exhibits
    def open_exhibits(self):
        reply = "\nOPEN Exhibits at " + self.zoo_name + ":"
        for i in self.animals:
            if i.visible == True:
                reply += str(i)
        return reply

    ## prints closed exhibits
    def closed_exhibits(self):
        reply = "\nCLOSED Exhibit at " + self.zoo_name + ":"
        animal_check = False
        for i in self.animals:
            if i.visible == False:
                reply += str(i)
                animal_check = True
        if animal_check == False:
            reply += "\nNONE"
        return reply

    ##finds the hungriest visible animal
    def hungriest(self):
        visible_animals = []
        for animal in self.animals:
            if animal.visible:
                visible_animals.append(animal)
        ##sorts by the hungriest animal
        visible_animals.sort(reverse = True)
        ##returns hungriest animal
        return visible_animals[0]

##creates the zookeeper
class Keeper(object):
    def __init__(self, zoo, name):
        self.name = name
        self.zoo = zoo

    ##prints which animal exhibits are open, which depends on their hunger status  
    def status(self):
        print "-" * 25 + "\n"
        for i in self.zoo.animals:
            if i.visible == True:
                print i.name + "\t\t" + str(i.hunger) + "(OPEN)"
            else:
                print i.name + "\t\t" + str(i.hunger) + "(CLOSED)"
                
    ##calls previous methods to 'work'
    def work(self):
        most_hungry = self.zoo.hungriest()
        most_hungry.hunger = 0
        print self.name
        for i in self.zoo.animals:
            if i.name != most_hungry.name:
                i.pace()
        self.status()
        
        
##main
national_zoo = Facility("the National Zoo")
national_zoo.animals.append(Animal("Tiger", "Stripes"))
national_zoo.animals.append(Animal("Monkey", "Aldo"))
national_zoo.animals.append(Animal("Monkey", "Mandem"))
national_zoo.animals.append(Animal("Monkey", "Dr.Milo"))
national_zoo.animals.append(Animal("Seal", "Hoover"))
national_zoo.animals.append(Animal("Penguin", "Salty"))
national_zoo.animals.append(Animal("Lion", "Metro"))

fred = Keeper(national_zoo, "Fred")

##fred works 10 times
for i in range(10):
    fred.work()
