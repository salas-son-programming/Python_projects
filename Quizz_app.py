#Quiz App
#o Asks multiple-choice questions.
#o Tracks correct answers and shows final score.
#Focus: Dictionaries, loops, scoring logic
#Tip: Store questions and answers in a dictionary or list of dicts

questions = [
    {"question": "what is the capital of cameroon?",
     "options": ["A. YAOUNDE", "B. DOUALA", "C. BUEA"],
     "answer": "A"},
    {"question": "where is cameroon located?",
     "options": ["A. AMERICA", "B. AFRICA", "C. ASIA"],
     "answer": "B"},
    {"question": "what is the capital of FRANCE?",
     "options": ["A. LYON", "B. MARSEILLE", "C. PARIS"],
     "answer": "C"}
]
points=0
for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)
    user_answer = input("enter your answer: ")
    if user_answer.upper() == q["answer"]:
        points+=1
print(f"you have obtained {points}/3")




