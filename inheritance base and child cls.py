class MobilePhone:
    def __init__(self, screen_type="Touch Screen", network_type="4G/5G", dual_sim=False,
                 front_camera="5MP", rear_camera="8MP", ram="2GB", storage="16GB"):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def display_specs(self):
        return (f"Screen Type: {self.screen_type}\n"
                f"Network Type: {self.network_type}\n"
                f"Dual SIM: {self.dual_sim}\n"
                f"Front Camera: {self.front_camera}\n"
                f"Rear Camera: {self.rear_camera}\n"
                f"RAM: {self.ram}\n"
                f"Storage: {self.storage}")

class Apple(MobilePhone):
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
    
    def display_specs(self):
        base_specs = super().display_specs()
        return f"{base_specs}\nModel: {self.model}\nBrand: Apple"

class Samsung(MobilePhone):
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
    
    def display_specs(self):
        base_specs = super().display_specs()
        return f"{base_specs}\nModel: {self.model}\nBrand: Samsung"

iphone = Apple(model="iPhone 14", front_camera="12MP", rear_camera="48MP", ram="6GB", storage="128GB", dual_sim=True)
galaxy = Samsung(model="Galaxy S23", front_camera="10MP", rear_camera="50MP", ram="8GB", storage="256GB", dual_sim=True)

print("Apple Phone Specs:")
print(iphone.display_specs())

print("\nSamsung Phone Specs:")
print(galaxy.display_specs())
