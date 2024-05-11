from Car import Car
from Motorcycle import Motorcycle

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "motorcycle":
            return Motorcycle()
        else:
            return None

# Uso de la clase VehicleFactory
factory = VehicleFactory()

while True:
    vehicle_type = input("Enter vehicle type (car or motorcycle): ").lower()

    vehicle = factory.create_vehicle(vehicle_type)
    if vehicle:
        vehicle.start_engine()
        vehicle.drive()
        vehicle.stop_engine()
        break  # Salir del bucle si se ingresó un tipo de vehículo válido
    else:
        print("Invalid vehicle type entered. Please enter 'car' or 'motorcycle'.")

