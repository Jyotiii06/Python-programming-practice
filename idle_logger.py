import time
from datetime import datetime

def log_message():
    with open("log.txt", "a") as file:
        file.write(f"Log entry at {datetime.now()}\n")
    print("Logged at", datetime.now())

def main():
    print("Idle-based script started. Press Ctrl+C to stop.")
    try:
        while True:
            log_message()
            time.sleep(10)  # wait for 10 seconds (idle time)
    except KeyboardInterrupt:
        print("\nScript stopped by user.")

if __name__ == "__main__":
    main()
