# exam.py - Control Statements Quiz

def ask(qno, question, options, correct):
    print(f"\nQ{qno}. {question}")
    for k, v in options.items():
        print(f"  {k}) {v}")
    ans = input("Your answer: ").lower()
    if ans == correct:
        print("✅ Correct")
        return 1
    else:
        print(f"❌ Wrong. Correct: {correct}) {options[correct]}")
        return 0

def main():
    print("🧪 Python Control Statements Quiz")
    score = 0
    total = 5

    score += ask(1, "Which keyword is used to skip an iteration in a loop?", 
                 {'a': 'break', 'b': 'continue', 'c': 'pass', 'd': 'stop'}, 'b')

    score += ask(2, "Which of the following creates an infinite loop?",
                 {'a': 'for i in range(10)', 'b': 'while True', 'c': 'while i < 5', 'd': 'for i in []'}, 'b')

    score += ask(3, "What does 'pass' do in Python?",
                 {'a': 'Skips the loop', 'b': 'Ends the loop', 'c': 'Does nothing', 'd': 'Raises error'}, 'c')

    score += ask(4, "Which one is correct syntax for if-elif-else?",
                 {'a': 'if-elseif-else', 'b': 'if-elif-else', 'c': 'if-else if-else', 'd': 'if-elif-endif'}, 'b')

    score += ask(5, "What will be output of: if 5 > 3: print('Hi')?",
                 {'a': 'Nothing', 'b': 'Error', 'c': 'Hi', 'd': 'False'}, 'c')

    print(f"\n📊 Final Score: {score}/{total}")
    print("🎉 Excellent!" if score == total else "👍 Keep practicing!")

if __name__ == "__main__":
    main()
