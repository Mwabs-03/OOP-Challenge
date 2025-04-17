# Creating a class Pet and initializing its attributes

class Pet :
    def __init__(self, name):
        #setting the default values as 5 to start the pet in a balanced and neutral state
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []


# Methods        
# eat(): reduces hunger by 3 points (but not below 0), and increases happiness by 1.
    def eat(self):
        if self.hunger > 0:
            self.hunger = max(self.hunger - 3, 0)
            self.happiness += 1
        else:
            print(f"{self.name} is not hungry.")
        return self.hunger, self.happiness
    
# sleep(): increases energy by 5 points (but not above 10).
    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        return self.energy
    

# play(): decreases energy by 2, increases happiness by 2, and increases hunger by 1.
    def play(self):
        # I have used 2 because, incase of any deductions, we  will not have negative energy
        if self.energy >= 2:
            self.energy -= 2
            self.happiness += 2
            self.hunger += 1
        else:
            print(f"{self.name} is too tired to play.")
        return self.energy, self.happiness, self.hunger

# get_status(): prints the current state of the pet.
    def get_status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        # this line prints tricks , separated by a comma. 
        # If there are no tricks, it prints 'None'.
        print(f"Tricks: {', '.join(self.tricks) if self.tricks else 'None'}")