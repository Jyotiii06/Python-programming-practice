def quiz_game():
    questions = {
        "Who created Python?": "guido",
        "What is the capital of India?": "delhi",
        "2 + 2 = ?": "4",
        "Does the sun rise in the east? (yes/no)": "yes"
        "Python is programming language? (yes/no)": "yes"
        "Is HTML is markup language? (yes/no)": "yes"
        "Why CSS is used in webpages?": "to style the webpage"
        "4 + 4 = ?": "8"
        
    }

    score = 0

    for question, answer in questions.items():
        user_answer = input(question + " ").lower()

        if user_answer == answer:
            print("Correct ✅")
            score += 1
        else:
            print("Wrong ❌")

    print("\nFinal Score:", score, "/", len(questions))

quiz_game()
