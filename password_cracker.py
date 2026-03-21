import itertools
import string
import time

def crack_password(password):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    start_time = time.time()

    print("\nCracking password...\n")

    for length in range(1, len(password) + 1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)

            if attempts % 500 == 0:
                print(f"Attempts: {attempts}")

            if guess == password:
                end_time = time.time()
                print("\n✅ Password cracked!")
                print(f"Password: {guess}")
                print(f"Attempts: {attempts}")
                print(f"Time taken: {round(end_time - start_time, 2)} seconds")
                return

password = "abc"   # 👈 change this manually

crack_password(password)
