class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"Device initialized: {self.brand} {self.model}")

    def device_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class MobilePhone(Device):
    def __init__(self, brand, model, phone_number):
        super().__init__(brand, model)
        self.phone_number = phone_number
        self.battery_level = 100
        print(f"MobilePhone initialized with number: {self.phone_number}")

    def make_call(self, number):
        if self.battery_level <= 0:
            print("Battery is dead. Please charge your phone.")
        else:
            print(f"Calling {number}...")
            self.battery_level -= 10

    def check_battery(self):
        print(f"Battery level: {self.battery_level}%")

phone = MobilePhone("Apple", "iPhone 14", "123-456-7890")
phone.device_info()
phone.make_call("987-654-3210")
phone.check_battery()
