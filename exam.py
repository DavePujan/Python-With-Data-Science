# exam.py - Python Operators Quiz

def ask_question(qno, question, options, correct_option):
    print(f"\nQ{qno}: {question}")
    for key, value in options.items():
        print(f"  {key}) {value}")
    
    user_input = input("Your answer: ").lower()
    while user_input not in options:
        user_input = input("Invalid option. Choose again (a/b/c/d): ").lower()
    
    if user_input == correct_option:
        print("✅ Correct!")
        return 1
    else:
        print(f"❌ Wrong! Correct answer is: {correct_option}) {options[correct_option]}")
        return 0


def main():
    print("🎯 Python Operators Quiz")
    print("-" * 30)

    score = 0
    total = 6

    # Q1: Arithmetic
    score += ask_question(
        1,
        "What is the result of 2 ** 3?",
        {'a': '6', 'b': '8', 'c': '9', 'd': '7'},
        'b'
    )

    # Q2: Assignment
    score += ask_question(
        2,
        "If x = 5 and then x += 3, what is the value of x?",
        {'a': '8', 'b': '5', 'c': '3', 'd': '7'},
        'a'
    )

    # Q3: Comparison
    score += ask_question(
        3,
        "Which operator checks if two values are not equal?",
        {'a': '==', 'b': '<>', 'c': '!=', 'd': '>='},
        'c'
    )

    # Q4: Logical
    score += ask_question(
        4,
        "What is the result of True and False?",
        {'a': 'True', 'b': 'False', 'c': 'None', 'd': 'Error'},
        'b'
    )

    # Q5: Identity
    score += ask_question(
        5,
        "If x = y = [1, 2], what is the result of x is y?",
        {'a': 'True', 'b': 'False', 'c': 'Error', 'd': 'None'},
        'a'
    )

    # Q6: Membership
    score += ask_question(
        6,
        "'a' in ['a', 'b', 'c'] returns?",
        {'a': 'False', 'b': 'Error', 'c': 'True', 'd': 'None'},
        'c'
    )

    # Final Score
    print("\n✅ Quiz Completed!")
    print(f"Your Score: {score}/{total}")

    if score == total:
        print("🎉 Perfect! You're an operator pro!")
    elif score >= 4:
        print("👍 Good job! Keep practicing.")
    else:
        print("📝 Review the operators and try again.")

if __name__ == "__main__":
    main()
