class vehicle():
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    def vehicletype(self):
        print(f"Vehicle Details:{self.make} {self.model} {self.year}")
class Car(vehicle):
    def __init__(self,fuel_type, make, model, year):
        super().__init__(make, model, year)
        self.fuel_type=fuel_type
    def mileageCalc(self, distance,fuelUsed):
        mileage=distance/fuelUsed
        return mileage
class Truck(vehicle):
    def __init__(self,cargoCapacity, make, model, year):
        super().__init__(make,model,year)
        self.cargoCapacity=cargoCapacity
    def calculateWeightCapacity(self, cargoCapacity):
        weightCapacity=cargoCapacity
        return weightCapacity
class ElectricCar(vehicle):
    def __init__(self,batteryCapacity, make, model, year):
        super().__init__(make,model,year)
        self.batteryCapacity=batteryCapacity
    def calculateRange(self,batteryCapacity):
        range=batteryCapacity*5
        return range


if __name__ == "__main__":
    car=Car("Petrol","Toyota","Corolla",2011)
    car.vehicletype()
    print(car.mileageCalc(500,25))
    eCar=ElectricCar(10,"Tesla","X",2020)
    eCar.vehicletype()
    print(eCar.calculateRange(10))
    truck=Truck(50,"Ford","Truck",2023)
    truck.vehicletype()
    print(truck.calculateWeightCapacity(50))
