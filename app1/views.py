class Vehicle:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        self.__fuel = 100

    def refuel(self, liters):
        self.__fuel += liters
        print(f"Refueled {liters} liters. Current fuel level: {self.__fuel}")

    def check_fuel(self):
        print(f"Current fuel level: {self.__fuel}")

    def make_sound(self):
        print("Beep! Beep!")

    def accelerate(self, speed):
        print(f"Accelerating to {speed} km/h.")

    def brake(self):
        print("Braking!")

    def get_brand_model(self):
        return f"Brand: {self.__brand}, Model: {self.__model}"

    def move(self):
        raise NotImplementedError("Move method must be implemented in the derived class.")


class Car(Vehicle):
    def drift(self):
        print("Car is drifting!")

    def play_music(self, song):
        print(f"Playing {song} in the car!")

    def move(self):
        print("Car is moving!")


class Truck(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.cargo_capacity = 0

    def load_cargo(self, weight):
        self.cargo_capacity += weight
        print(f"Cargo loaded. Current cargo capacity: {self.cargo_capacity} kg.")

    def unload_cargo(self, weight):
        if self.cargo_capacity >= weight:
            self.cargo_capacity -= weight
            print(f"Cargo unloaded. Current cargo capacity: {self.cargo_capacity} kg.")

        else:
            print("Not enough cargo to unload.")

    def check_cargo_capacity(self):
        print(f"Current cargo capacity: {self.cargo_capacity} kg.")

    def move(self):
        print("Truck is moving!")


class Boat(Vehicle):
    def anchor(self):
        print("Boat is anchoring!")

    def turn_on_lights(self):
        print("Boat lights are turned on!")

    def move(self):
        print("Boat is sailing!")


class Plane(Vehicle):
    def autopilot(self):
        print("Plane is on autopilot!")

    def deploy_flaps(self):
        print("Flaps are deployed for landing!")

    def move(self):
        print("Plane is flying!")

    def greeting(self):
        print("hello to all!")


car1 = Car("Honda", "Civic")
boat1 = Boat("Sunny", "Sailor")
plane1 = Plane("Skyline", "Jetstar")
truck1 = Truck("Swift", "Transporter")

vehicles = [car1, boat1, plane1, truck1]

for vehicle in vehicles:
    print(vehicle.get_brand_model())
    vehicle.move()
    print()
