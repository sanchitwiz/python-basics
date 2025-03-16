class Car:
    total_car = 0

    def __init__(self, model, brand):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand + " !"
    
    @staticmethod
    def general_description():
        return "Cars are good"

class ElectricCar(Car):
    def __init__(self, model, brand, battery_size):
        super().__init__(model, brand)
        self.battery_size = battery_size

def main():
    new_car = Car("Toyota", "Defender")
    print(new_car.model)
    print(new_car.full_name())
    new_electric_car = ElectricCar("Nexon-EV","Tata", "2200Ah")
    print(new_electric_car.battery_size)
    print(new_electric_car.full_name())
    print(new_car.get_brand())
    try: 
        print(new_car.__brand)
    except Exception as error:
        print("Cannot Access Private attribute,", error)
    print(Car.total_car)
    print(Car.general_description())

if __name__ == "__main__":
    main()