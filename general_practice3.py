## using all basics practice 3##
#Simple Quiz Game

questions = [
"How many days are in a week?",
"What's 2 + 2?",
"Are you a good coder?"
]

user_answers = []

quiz_answers = [
"7",
"4",
'no'
]

#asks questions and collects data
def ask_questions():
    for question in questions:
        print(question)
        answer = input().lower()
        user_answers.append(answer)

ask_questions()

#compares user and quiz answers lists
def check_answers():
    score = 0
    for i in range(len(user_answers)):
        if user_answers[i] == quiz_answers[i]:
            score += 1
    return score
    

print(f"You have scored {check_answers()}/{len(questions)}")

