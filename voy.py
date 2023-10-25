# written by Anna Braudo
# TODO: randomize alternatives, instead of sort
# TODO: don't print result per question, store a counter of correct answers
# TODO: catch invalid user input with a message
# TODO: use letters as answer identifiers
# TODO: improve results summary, to improve readability and maybe to store texts in variables

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


if total_correct <= 2:
    print("У вас отлично развито логическое мышление. Если вы и делаете ошибки в рассуждениях, то в основном по случайности или от усталости, но не из-за неумения. Тем не менее, помните, что все хорошее всегда можно улучшить. В данном случае вы решили отвечать на вопросы намеренно неправильно.")
elif total_correct > 2 and total_correct < 6:
    print("Вы не захотели проходить тест.")
elif total_correct > 6 and total_correct < 14:
    print('Вариант 1: Вы проходили тест, тыкая в пункты наугад. Вариант 2: У вас логическое мышление отсутствует вообще. Тот результат, который получили вы, можно получить простым тыканьем наугад. Не стоит пытаться "рассуждать логически", особенно прилюдно.')
elif total_correct > 14 and total_correct < 20:
    print("Вариант 1: У вас не хватило терпения пройти весь тест, вы сделали его только отчасти, а оставшиеся пункты выбрали наугад. Вариант 2: Ваше логическое мышление неразвито. Если вы попытаетесь публично рассуждать, то, вполне возможно, вас будут высмеивать. Вам придется обратиться к другим сильным сторонам вашей личности, если вы хотите кого-то в чем-то убедить или что-то узнать. Однако может быть, вы не совсем безнадежны, если попробуете подучиться.")
elif total_correct > 20 and total_correct < 26:
    print("У вас хорошо развито логическое мышление. Однако вы можете делать ошибки в нестандартных или запутанных случаях. Получив какой-нибудь вывод в результате рассуждения, не торопитесь принимать его за истину. Возьмите за правило перепроверять свои выводы, искать в них ошибки и просто слабые места. Не удивляйтесь, не возмущайтесь, если вас поправляют: возможно, за дело.")
elif total_correct > 26 and total_correct < 31:
    print("У вас отлично развито логическое мышление. Если вы и делаете ошибки в рассуждениях, то в основном по случайности или от усталости, но не из-за неумения. Тем не менее, помните, что все хорошее всегда можно улучшить.")
