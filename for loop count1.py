import random

def roll_die():
    """Simulate rolling a six-sided die."""
    return random.randint(1, 6)

def simulate_rolls(num_rolls):
    """Simulate rolling a die `num_rolls` times and print statistics."""
    rolls = []
    count_6 = 0
    count_1 = 0
    count_two_6s_in_a_row = 0
    for _ in range(num_rolls):
        roll = roll_die()
        rolls.append(roll)
    for i in range(len(rolls)):
        if rolls[i] == 6:
            count_6 += 1
        if rolls[i] == 1:
            count_1 += 1
        if i > 0 and rolls[i] == 6 and rolls[i - 1] == 6:
            count_two_6s_in_a_row += 1
    print(f"Total rolls: {num_rolls}")
    print(f"Number of times you rolled a 6: {count_6}")
    print(f"Number of times you rolled a 1: {count_1}")
    print(f"Number of times you rolled two 6s in a row: {count_two_6s_in_a_row}")
simulate_rolls(20)
