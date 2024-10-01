
def ask_question(question, options, correct_answer):
    print("\n" + question)
    for option in options:
        print(option)
    
    
    answer = input("Enter your answer (A, B, C, or D): ").upper()
    while answer not in ['A', 'B', 'C', 'D']:
        answer = input("Invalid input. Please enter A, B, C, or D: ").upper()

    
    if answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Wrong! The correct answer was {correct_answer}.")
        return False


def run_quiz():
    
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Paris", "C. Madrid", "D. Rome"],
            "correct_answer": "B"
        },
        {
            "question": "Which language is used for web development?",
            "options": ["A. Python", "B. HTML", "C. Java", "D. C++"],
            "correct_answer": "B"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A. Charles Dickens", "B. J.K. Rowling", "C. William Shakespeare", "D. Mark Twain"],
            "correct_answer": "C"
        }
    ]

    score = 0
    total_questions = len(questions)

    # Loop through each question
    for question_data in questions:
        is_correct = ask_question(
            question_data["question"], 
            question_data["options"], 
            question_data["correct_answer"]
        )
        if is_correct:
            score += 1

    
    print("\nQuiz Over!")
    print(f"Your final score is: {score}/{total_questions}")


if __name__ == "__main__":
    run_quiz()
