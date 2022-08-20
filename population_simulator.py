import random
import pandas as pd
# Assumed random genders and random ages between 18 to 50 initially
class Person:
    def __init__(self, gender, age, die):
        self.gender = gender
        self.age = age
        self.die = die
        
    
    def __repr__(self):
        return 'Person:  ' + str(self.gender)  +'   ' +  str(self.age) 

#Enough food available for 50 people to servive initially
class Food:
    def __init__(self):
        self.available_food = 5


class Simulation:
    def __init__(self):
        self.list_per = []
        self.genders = ['Male', 'Female']
        self.years = 0
        self.disaster = False
        self.print_log = []
        self.food = Food()

    def beginSim(self):
        for i in range(0, 50):
            self.list_per.append(Person(random.sample(self.genders, 1)[0], random.randint(18, 50), False))

        print(self.list_per, len(self.list_per))

    
    def check_dead(self):
        #Person is dead if age greater than 80 
        for person in self.list_per:
            if person.age > 80:
                person.die = True

        #Person is dead if he/she can not get enough food
        for person in self.list_per:
            if person.age <= 8:
                continue
            elif person.age >8 and self.food.available_food > 1:
                continue
            else:
                person.die = True


    def chance_of_infant_mortality(self):
        for person in self.list_per:
            if person.age<=1 and random.randint(1, 101) < 5:
                person.die = True


    def chance_of_natural_disaster(self):
        pop_died = random.randint(5, 15)
        if pop_died > len(self.list_per):
            pop_died = len(self.list_per)
        for i in range(0, pop_died):
            self.list_per.remove(random.choice(self.list_per))


        
    def reproduce(self):
        for person in self.list_per:
            if person.gender == 'Female' and person.age>=18 and person.age<=35 and random.randint(1, 101) <= 20:
                self.list_per.append(Person(random.sample(self.genders, 1)[0], 0, False))

        #print(self.list_per, len(self.list_per))


    def increment_food(self):
        for person in self.list_per:
            if person.age >8:
                self.food.available_food += 5
    
    def consume_food(self):
        for person in self.list_per:
            self.food.available_food -= 1

    def harvest(self):
        self.increment_food()
        self.consume_food()
        count_able = 0
        for person in self.list_per:
            if person.age > 8:
                count_able+=1
        
        print(str(count_able) + " persons can produce food")
        


    def remove_dead(self):
        self.list_per = list(filter(lambda person: not person.die,
                                self.list_per))

        
    def runYear(self):
        self.beginSim()
        # update this value to 100000 later

        self.years = 0
        while len(self.list_per)>0 and len(self.list_per)<=100000:
            #Infant Mortality
            #self.chance_of_infant_mortality()

            #Disaster chance is 10%
            # chance = random.randint(1, 101)
            # if chance <=10:
            #     self.disaster = True
            #     self.chance_of_natural_disaster()
            # else:
            #     self.disaster = False

            self.check_dead()
            self.remove_dead()
            for person in self.list_per:
                person.age += 1
            self.reproduce()
            self.harvest()
            self.years+=1
            self.print_log.append(list([len(self.list_per), self.food.available_food, self.years, self.disaster]))
            print("Total Population :", len(self.list_per), "Total years: ", self.years)
            print("food availability: ", self.food.available_food)
            if self.disaster:
                print("Disaster year: ", self.years)
        
        df = pd.DataFrame(self.print_log, columns = ['Total Population', 'Food available', 'Current Year', 'Disaster year'])
        #df.to_csv('E:\population_simulator\Whole_log.csv', index = False)
        df.to_csv('Whole_log.csv', index = False)
        return 


s = Simulation()
s.runYear()
