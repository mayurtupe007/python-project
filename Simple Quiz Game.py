
questions = {
    " What is the output of print(2 ** 3)?": {
        "options": ["A. 6 ", "B. 8", "C. 9", "D. 5"],
        "answer": "B"
    },
    " Which of the following is a valid variable name in Python?": {
        "options": ["A. 2var", "B. @name ", "C. var_2 t", "D. class "],
        "answer": "C"
    },
    " What is the data type of print(type(3.14))?": {
        "options": ["A. int  ", "B. float ", "C. str ", "D. complexs"],
        "answer": "B"
    },
    " Which keyword is used for a function in Python?": {
        "options": ["A. func", "B. define ", "C. def ", "D. function "],
        "answer": "C"
    },
    " What does the len() function do?": {
        "options": ["A. Returns number of lines in file","B. Returns length of object","C. Returns last element","D. Returns logical expression"],
        "answer": "B"
    },
    " Which operator is used for floor division?": {
        "options": [ "A. /","B. %","C. //","D, **"],
        "answer": "C"
    },
    " What is the output of bool([])?": {
        "options": ["A. True","B. False","C.  None","D. Error" ],
        "answer": "B"
    },
    " How do you start a comment in Python?": {
        "options": ["A.  //","B. <!--","C. #","D. -- "],
        "answer": "C"
    },
    " What is the output of Hello[1]?": {
        "options": ["A. H ","B. e","C. l","D. o"],
        "answer": "B"
    },
    " What is a correct syntax to create a Python dictionary?": {
        "options": ["A. dict = (1: One, 2: Two)","B. dict ={1=> One, 2 => Two }","C .dict = {1, One, 2, Two}","D. dict = {1: 'One', 2: 'Two'}"],
        "answer": "D"
    }
    

}

def run_quiz(quiz):
    score = 0
    print("🧠 Welcome to the Quiz Game!\n")
    for i, (question, q_data) in enumerate(quiz.items(), start=1):
        print(f"Q{i}. {question}")
        for opt in q_data["options"]:
            print(opt)
        user_ans = input("Your answer (A/B/C/D): ").strip().upper()
        
        if user_ans == q_data["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q_data['answer']}\n")
    print(f"🎉 Your final score: {score}/{len(quiz)}")


run_quiz(questions)
