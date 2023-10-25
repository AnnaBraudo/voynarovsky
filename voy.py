# written by Anna Braudo
# TODO: randomize alternatives, instead of sort
# TODO: don't print result per question, store a counter of correct answers
# TODO: catch invalid user input with a message
# TODO: use letters as answer identifiers

import random
from string import ascii_lowercase
# putting all 30 statements from the test and correct answers into a dict
# always putting the correct answer first
QUESTIONS_RUS = {
    "1. Шмурдик боится как мышей, так и тараканов.": [
        "шмурдик боится мышей",
        "шмурдик не боится тараканов",
        "шмурдик боится мышей больше, чем тараканов, но и тараканов боится тоже"],
    "2. Известно, что грымзик обязательно или полосат, или рогат, или то и другое вместе.": [
        "грымзик не может быть однотонным и безрогим одновременно",
        "грымзик не может быть безрогим",
        "грымзик не может быть полосатым и безрогим одновременно"],
    "3. Если запырку отравить, то она сразу начнет пускать пузыри.": [
        "если запырка не пускает пузыри, то она не отравлена",
        "если запырку не отравить, то она не будет пускать пузыри",
        "если запырка пускает пузыри, то она была отравлена"],
        }

total_correct = 0 
for question, alternatives in QUESTIONS_RUS.items():
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    print(question)
    for label, alternative in enumerate(sorted_alternatives):
        print(f"  {label+1}) {alternative}")
    answer_label = int(input("Answer: "))-1
    answer = sorted_alternatives[answer_label]
    if answer == correct_answer:
        print("Correct!")
        total_correct = total_correct + 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"Total correct answers: {total_correct!r}.")