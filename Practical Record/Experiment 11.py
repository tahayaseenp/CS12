import random
import time


def simulate_dice():
    try:
        print("Press Ctrl+C to stop the dice")
        while True:
            n = random.randint(1, 6)
            print(n, end=' ')  # This statement can be commented out to keep the terminal clean
            time.sleep(0.001)
    except KeyboardInterrupt:
        print("\nDice stopped")
        print("Your number is", n)
        

simulate_dice()