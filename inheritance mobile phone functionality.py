class MobilePhone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.battery_level = 100
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print(f"Added {name} with number {number} to contacts.")

    def make_call(self, number):
        if self.battery_level <= 0:
            print("Battery is dead. Please charge your phone.")
        else:
            print(f"Calling {number}...")
            self.battery_level -= 10

    def receive_call(self, number):
        print(f"Incoming call from {number}...")
        print(f"Call connected with {number}.")

    def send_text(self, number, message):
        if self.battery_level <= 0:
            print("Battery is dead. Please charge your phone.")
        else:
            print(f"Sending text to {number}: {message}")
            self.battery_level -= 5

    def take_a_picture(self):
        if self.battery_level <= 0:
            print("Battery is dead. Please charge your phone.")
        else:
            print("Taking a picture...")
            self.battery_level -= 15

    def charge_phone(self):
        self.battery_level = 100
        print("Phone is fully charged.")

    def check_battery(self):
        print(f"Battery level: {self.battery_level}%")

    def show_contacts(self):
        if not self.contacts:
            print("No contacts saved.")
        else:
            print("Contacts:")
            for name, number in self.contacts.items():
                print(f"{name}: {number}")

# Example usage
phone = MobilePhone("123-456-7890")
phone.add_contact("Alice", "987-654-3210")
phone.make_call("987-654-3210")
phone.receive_call("555-555-5555")
phone.send_text("987-654-3210", "Hello, Alice!")
phone.take_a_picture()
phone.check_battery()
phone.charge_phone()
phone.check_battery()
phone.show_contacts()
