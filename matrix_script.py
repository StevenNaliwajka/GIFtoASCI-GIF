import random
import os
import time

def matrix_stream(width=80, height=20, speed=0.05):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#$%^&*()"
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        for _ in range(height):
            row = "".join(random.choice(chars) if random.random() > 0.5 else " " for _ in range(width))
            print(row)
        time.sleep(speed)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        matrix_stream(width=80, height=25, speed=0.1)
    except KeyboardInterrupt:
        print("\\nMatrix stream stopped.")