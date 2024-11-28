class Car:
    def __init__(self, o_name, o_make, o_model,o_color):
        self.name = o_name
        self.make = o_make
        self.model = o_model
        self.color=o_color

    def start_engine(self):
        print("Starting a car with the name " + self.name)
        print("Starting a car with the make " + self.make)
        print("Starting a car with the color " + self.color )
        print("Starting a car with the model " + self.model)



lambo = Car("Lambo", "V6", "2022", "Black")
lambo.start_engine()

print(" --- ")

mg_hector = Car("Hector","1.5+ Turbo","2023","White")
mg_hector.start_engine()

print("_________")

bmw=Car("Bmw","Q6","2024","Blue")
bmw.start_engine()