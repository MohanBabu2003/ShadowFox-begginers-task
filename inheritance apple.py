class Apple:
    def __init__(self, color, size, variety, weight):
        self.color = color
        self.size = size
        self.variety = variety
        self.weight = weight

    def __str__(self):
        return f"Apple(variety={self.variety}, color={self.color}, size={self.size}, weight={self.weight}g)"
apple1 = Apple(color="Red", size="Medium", variety="Fuji", weight=150)
apple2 = Apple(color="Green", size="Large", variety="Granny Smith", weight=180)
apple3 = Apple(color="Yellow", size="Small", variety="Golden Delicious", weight=130)
apple4 = Apple(color="Red", size="Large", variety="Red Delicious", weight=160)
print(apple1)
print(apple2)
print(apple3)
print(apple4)
