question_pack = [
    {
        "question": "1+1=?",
        "choices": ["A = 1", "B = 2", "C = 3", "D = 4"],
        "rightchoice": "B",
        "reason": "Based on the elementary math book, 1+1 is 2"
    },
    {
        "question": "2+2=?",
        "choices": ["A = 2", "B = 4", "C = 6", "D = 8"],
        "rightchoice": "B",
        "reason": "Based on the elementary math book, 2+2 is 4"
    },
    {
        "question": "3+3=?",
        "choices": ["A = 3", "B = 6", "C = 9", "D = 12"],
        "rightchoice": "B",
        "reason": "Based on the elementary math book, 4+4 is 8"
    }
]
correct_answer_count = 0
user_choice = []

for q in range(len(question_pack)):
    print(question_pack[q]["question"])
    choices = question_pack[q]["choices"]
    print(*question_pack[q]["choices"], sep="\n")
    print()
    answer = input("Your answer? ").upper()
    user_choice.append(answer)

for q in range(len(question_pack)):
    print(q + 1, ":")
    if user_choice[q] == question_pack[q]["rightchoice"]:
        print("Bingo, the correct answer is {0}".format(user_choice[q]))
        correct_answer_count = correct_answer_count+1
        print()
    else:
        print("Nah, the right answer is {0}, not {1}.".format(question_pack[q]["rightchoice"], user_choice[q]))
        print("Reason: {0}".format(question_pack[q]["reason"]))
        print()

print("Correct answers:", correct_answer_count)

correct_percentage = float(correct_answer_count/len(question_pack)*100)
print("Percent correct:", round(correct_percentage, 2))
