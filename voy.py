# written by Anna Braudo

#putting all 30 statements from the test and correct answers into a list
QUESTIONS = {
    "Шмурдик боится как мышей, так и тараканов.": ["b","a","c"],
    "Известно, что грымзик обязательно или полосат, или рогат, или то и другое вместе.": ["b","a","c"],
    "Если запырку отравить, то она сразу начнет пускать пузыри.": ["c","a","b"],
            }

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    for label, alternative in enumerate(sorted_alternatives):
        print(f"  {label}) {alternative}")

    answer_label = int(input(f"{question}? "))
    answer = sorted_alternatives[answer_label]
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")