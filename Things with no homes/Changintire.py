class Car:
    def __init__(self, make, model, year, tire_status, has_jack):
        self.make = make  # Corrected from self.made
        self.model = model
        self.year = year
        self.tire_status = tire_status
        self.has_jack = has_jack

    def check_tires(self):
        print("Tire Status:")
        for position, status in self.tire_status.items():  # Fixed .times() to .items()
            print(f"{position}: {status}")

    def change_tire(self, tire_position):
        try:
            if not self.has_jack:
                raise Exception("Error: No jack available to change the tire.")

            # Check if the tire position is valid
            if tire_position not in self.tire_status:
                raise ValueError(f"Error: {tire_position} is not a valid tire position.")

            # Check if the tire is already "good"
            if self.tire_status[tire_position] == "good":
                raise Exception(f"Error: The {tire_position} tire is already in good condition.")

            # Change the tire status
            self.tire_status[tire_position] = "good"
            print(f"The {tire_position} tire has been changed successfully!")

        except Exception as e:
            print(e)

def main():

    # Initial tire status (with two flat tires)
    tire_status = {
        "front_left": "flat",
        "front_right": "good",
        "rear_left": "good",
        "rear_right": "flat"
    }

    # Create a Car object
    my_car = Car("Toyota", "Corolla", 2020, tire_status, has_jack=True)

    # Check tire status
    my_car.check_tires()

    # Simulate changing tires
    while True:
        tire_to_change = input("Enter the tire to change (e.g., front_left, rear_right) or 'exit' to quit: ")
    
        if tire_to_change.lower() == 'exit':
            break
    
        my_car.change_tire(tire_to_change)
        my_car.check_tires()

# This should be outside the main function
if __name__ == "__main__":
    main()
