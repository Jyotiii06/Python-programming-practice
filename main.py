import random
import time

sentences = [
    "Python is a powerful programming language.",
    "Practice typing every day to improve speed.",
    "Consistency is the key to success.",
    "Artificial intelligence is changing the world.",
    "GitHub projects improve developer skills."
]

print("=" * 50)
print("       PYTHON TYPING SPEED TESTER")
print("=" * 50)

sentence = random.choice(sentences)

print("\nType the following sentence:\n")
print(sentence)

input("\nPress Enter when ready...")

start_time = time.time()

typed_text = input("\nStart typing:\n")

end_time = time.time()

time_taken = end_time - start_time

original_words = sentence.split()
typed_words = typed_text.split()

correct_words = 0

for i in range(min(len(original_words), len(typed_words))):
    if original_words[i] == typed_words[i]:
        correct_words += 1

accuracy = (correct_words / len(original_words)) * 100

word_count = len(typed_text.split())

wpm = (word_count / time_taken) * 60

print("\n" + "=" * 50)
print("RESULT")
print("=" * 50)

print(f"Time Taken : {round(time_taken, 2)} seconds")
print(f"Typing Speed : {round(wpm, 2)} WPM")
print(f"Accuracy : {round(accuracy, 2)}%")

if wpm >= 60:
    print("Excellent typing speed!")
elif wpm >= 40:
    print("Good job!")
else:
    print("Keep practicing!")
print("=" * 50)
