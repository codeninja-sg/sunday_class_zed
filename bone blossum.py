class Plant:
    def __init__(self, name, water_needed, growth_rate):
        self.name = name
        self.water_level = 0
        self.growth_progress = 0
        self.water_needed = water_needed
        self.growth_rate = growth_rate
        self.is_harvestable = False

    def water(self, amount):
        self.water_level += amount
        print(f"{self.name} watered. Water level: {self.water_level}")

    def grow(self):
        if self.water_level >= self.water_needed:
            self.growth_progress += self.growth_rate
            self.water_level -= self.water_needed  # Simulate water consumption
            print(f"{self.name} is growing. Growth progress: {self.growth_progress}")
            if self.growth_progress >= 100:  # Example threshold for harvest
                self.is_harvestable = True
                print(f"{self.name} is ready for harvest!")
        else:
            print(f"{self.name} needs more water to grow.")

    def harvest(self):
        if self.is_harvestable:
            print(f"Harvested {self.name}!")
            self.growth_progress = 0  # Reset for potential re-growth
            self.is_harvestable = False
        else:
            print(f"{self.name} is not yet ready to be harvested.")

class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"{plant.name} added to the {self.name} garden.")

    def simulate_day(self):
        print(f"\n--- Simulating a day in {self.name} garden ---")
        for plant in self.plants:
            plant.grow()

# Example Usage
my_garden = Garden("My Backyard Oasis")

carrot = Plant("Carrot", water_needed=10, growth_rate=15)
tomato = Plant("Tomato", water_needed=20, growth_rate=10)

my_garden.add_plant(carrot)
my_garden.add_plant(tomato)

# Simulate a few days of growth and care
for day in range(1, 6):
    print(f"\nDay {day}:")
    carrot.water(15)
    tomato.water(25)
    my_garden.simulate_day()

# Check harvestability and harvest
carrot.harvest()
tomato.harvest()