class Samsung:
    def __init__(self, model, screen_size, storage, battery_capacity, color):
        self.model = model
        self.screen_size = screen_size
        self.storage = storage
        self.battery_capacity = battery_capacity
        self.color = color

    def __str__(self):
        return (f"Samsung(model={self.model}, screen_size={self.screen_size} inches, "
                f"storage={self.storage}GB, battery={self.battery_capacity}mAh, color={self.color})")


# Creating objects of Samsung class with different properties
samsung1 = Samsung(model="Galaxy S21", screen_size=6.2, storage=128, battery_capacity=4000, color="Phantom Gray")
samsung2 = Samsung(model="Galaxy Note 20", screen_size=6.7, storage=256, battery_capacity=4300, color="Mystic Bronze")
samsung3 = Samsung(model="Galaxy Z Fold 3", screen_size=7.6, storage=512, battery_capacity=4400, color="Phantom Black")
samsung4 = Samsung(model="Galaxy A52", screen_size=6.5, storage=128, battery_capacity=4500, color="Awesome Blue")

# Printing the properties of each Samsung object
print(samsung1)
print(samsung2)
print(samsung3)
print(samsung4)
