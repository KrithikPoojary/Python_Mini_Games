from physics import physics_questions
from chemistry import chemistry_questions
from maths import maths_questions
from biology import biology_questions
import random

print("**********************************************")
print("Welcome to Quiz_game!!")
print("**********************************************")
print("Here we have Following types of quiz:\n1-Maths Quiz\n2-Physics Quiz\n3-Chemistry quiz\n4-Biology quiz\n5-Physics + Chemistry Quiz\n6-Physics + Maths Quiz\n7-Physics + Biology Quiz\n8-Chemistry + Biology Quiz\n9-Chemistry + Maths Quiz\n10-Maths + Biology Quiz\n11-PCM Quiz\n12-PCB Quiz\n13-PCMB Quiz")
print("------------------------------------------------------------------")

def math_quiz():
    selected_question = random.sample(maths_questions, 10)
    score = 0
    of_score = 0
    sr_no = 1
    while True:
        for q in selected_question:
            print("")
            print(f"{sr_no}. {q['question']}")
            print("")
            for option in q["options"]:
                print(option)
            print("")
            while True:
                user = input("----->Enter your choice: ").strip().upper()
                if user == "A" or user == "B" or user == "C" or user == "D":
                    break
                else:
                    print("choose among choices(A,B,C,D)")
            # of_score += 1
            if user == q["answer"]:
                of_score += 1
                print("Bravo! correct choice")
                score += 1
                print(f"Your score is [{score}/{of_score}]")
            else:
                of_score += 1
                print(f"Wrong choice the correct option is {q['answer']}")
                print(f"Your score is [{score}/{of_score}]")
            sr_no += 1
            print("------------------------------------------------------------------")
        print('')
        final_score = score
        percentage = (final_score / 10) * 100
        print(f"You got {percentage}% in This Maths Quiz")
        if percentage < 10:
            print("Very Poor! You need a lot of practice.")
        elif percentage < 20:
            print("Poor! Keep learning.")
        elif percentage < 30:
            print("Below Average! Practice more.")
        elif percentage < 40:
            print("Average! You can do better.")
        elif percentage < 50:
            print("Fair! Keep improving.")
        elif percentage < 60:
            print("Good Job!")
        elif percentage < 70:
            print("Very Good!")
        elif percentage < 80:
            print("Great Work!")
        elif percentage < 90:
            print("Excellent!")
        elif percentage < 100:
            print("Outstanding!")
        else:
            print("Perfect Score! Genius!")
        break

def physics_quiz():
    selected_question = random.sample(physics_questions, 10)
    score = 0
    of_score = 0
    sr_no = 1
    while True:
        for q in selected_question:
            print("")
            print(f"{sr_no}. {q['question']}")
            print("")
            for option in q["options"]:
                print(option)
            print("")
            while True:
                user = input("----->Enter your choice: ").strip().upper()
                if user == "A" or user == "B" or user == "C" or user == "D":
                    break
                else:
                    print("choose among choices(A,B,C,D)")
            # of_score += 1
            if user == q["answer"]:
                of_score += 1
                print("Bravo! correct choice")
                score += 1
                print(f"Your score is [{score}/{of_score}]")
            else:
                of_score += 1
                print(f"Wrong choice the correct option is {q['answer']}")
                print(f"Your score is [{score}/{of_score}]")
            sr_no += 1
            print("------------------------------------------------------------------")
        print('')
        final_score = score
        percentage = (final_score / 10) * 100
        print(f"You got {percentage}% in This Physics Quiz")
        if percentage < 10:
            print("Very Poor! You need a lot of practice.")
        elif percentage < 20:
            print("Poor! Keep learning.")
        elif percentage < 30:
            print("Below Average! Practice more.")
        elif percentage < 40:
            print("Average! You can do better.")
        elif percentage < 50:
            print("Fair! Keep improving.")
        elif percentage < 60:
            print("Good Job!")
        elif percentage < 70:
            print("Very Good!")
        elif percentage < 80:
            print("Great Work!")
        elif percentage < 90:
            print("Excellent!")
        elif percentage < 100:
            print("Outstanding!")
        else:
            print("Perfect Score! Genius!")
        break

def chemistry_quiz():
    selected_question = random.sample(chemistry_questions, 10)
    score = 0
    of_score = 0
    sr_no = 1
    while True:
        for q in selected_question:
            print("")
            print(f"{sr_no}. {q['question']}")
            print("")
            for option in q["options"]:
                print(option)
            print("")
            while True:
                user = input("----->Enter your choice: ").strip().upper()
                if user == "A" or user == "B" or user == "C" or user == "D":
                    break
                else:
                    print("choose among choices(A,B,C,D)")
            # of_score += 1
            if user == q["answer"]:
                of_score += 1
                print("Bravo! correct choice")
                score += 1
                print(f"Your score is [{score}/{of_score}]")
            else:
                of_score += 1
                print(f"Wrong choice the correct option is {q['answer']}")
                print(f"Your score is [{score}/{of_score}]")
            sr_no += 1
            print("------------------------------------------------------------------")
        print('')
        final_score = score
        percentage = (final_score / 10) * 100
        print(f"You got {percentage}% in This Chemistry Quiz")
        if percentage < 10:
            print("Very Poor! You need a lot of practice.")
        elif percentage < 20:
            print("Poor! Keep learning.")
        elif percentage < 30:
            print("Below Average! Practice more.")
        elif percentage < 40:
            print("Average! You can do better.")
        elif percentage < 50:
            print("Fair! Keep improving.")
        elif percentage < 60:
            print("Good Job!")
        elif percentage < 70:
            print("Very Good!")
        elif percentage < 80:
            print("Great Work!")
        elif percentage < 90:
            print("Excellent!")
        elif percentage < 100:
            print("Outstanding!")
        else:
            print("Perfect Score! Genius!")
        break

def biology_quiz():
    selected_question = random.sample(biology_questions, 10)
    score = 0
    of_score = 0
    sr_no = 1
    while True:
        for q in selected_question:
            print("")
            print(f"{sr_no}. {q['question']}")
            print("")
            for option in q["options"]:
                print(option)
            print("")
            while True:
                user = input("----->Enter your choice: ").strip().upper()
                if user == "A" or user == "B" or user == "C" or user == "D":
                    break
                else:
                    print("choose among choices(A,B,C,D)")
            # of_score += 1
            if user == q["answer"]:
                of_score += 1
                print("Bravo! correct choice")
                score += 1
                print(f"Your score is [{score}/{of_score}]")
            else:
                of_score += 1
                print(f"Wrong choice the correct option is {q['answer']}")
                print(f"Your score is [{score}/{of_score}]")
            sr_no += 1
            print("------------------------------------------------------------------")
        print('')
        final_score = score
        percentage = (final_score / 10) * 100
        print(f"You got {percentage}% in This Biology Quiz")
        if percentage < 10:
            print("Very Poor! You need a lot of practice.")
        elif percentage < 20:
            print("Poor! Keep learning.")
        elif percentage < 30:
            print("Below Average! Practice more.")
        elif percentage < 40:
            print("Average! You can do better.")
        elif percentage < 50:
            print("Fair! Keep improving.")
        elif percentage < 60:
            print("Good Job!")
        elif percentage < 70:
            print("Very Good!")
        elif percentage < 80:
            print("Great Work!")
        elif percentage < 90:
            print("Excellent!")
        elif percentage < 100:
            print("Outstanding!")
        else:
            print("Perfect Score! Genius!")
        break

def pc_quiz():
    selected_question = random.sample(physics_questions, 5)+random.sample(chemistry_questions ,5)
    random.shuffle(selected_question)
    score = 0
    of_score = 0
    sr_no = 1
    while True:
        for q in selected_question:
            print("")
            print(f"{sr_no}. {q['question']}")
            print("")
            for option in q["options"]:
                print(option)
            print("")
            while True:
                user = input("----->Enter your choice: ").strip().upper()
                if user == "A" or user == "B" or user == "C" or user == "D":
                    break
                else:
                    print("choose among choices(A,B,C,D)")
            # of_score += 1
            if user == q["answer"]:
                of_score += 1
                print("Bravo! correct choice")
                score += 1
                print(f"Your score is [{score}/{of_score}]")
            else:
                of_score += 1
                print(f"Wrong choice the correct option is {q['answer']}")
                print(f"Your score is [{score}/{of_score}]")
            sr_no += 1
            print("------------------------------------------------------------------")
        print('')
        final_score = score
        percentage = (final_score / 10) * 100
        print(f"You got {percentage}% in This Physics and Chemistry Quiz")
        if percentage < 10:
            print("Very Poor! You need a lot of practice.")
        elif percentage < 20:
            print("Poor! Keep learning.")
        elif percentage < 30:
            print("Below Average! Practice more.")
        elif percentage < 40:
            print("Average! You can do better.")
        elif percentage < 50:
            print("Fair! Keep improving.")
        elif percentage < 60:
            print("Good Job!")
        elif percentage < 70:
            print("Very Good!")
        elif percentage < 80:
            print("Great Work!")
        elif percentage < 90:
            print("Excellent!")
        elif percentage < 100:
            print("Outstanding!")
        else:
            print("Perfect Score! Genius!")
        break

def pm_quiz():
    selected_question = random.sample(physics_questions, 5)+random.sample(maths_questions ,5)
    random.shuffle(selected_question)
    score = 0
    of_score = 0
    sr_no = 1
    while True:
        for q in selected_question:
            print("")
            print(f"{sr_no}. {q['question']}")
            print("")
            for option in q["options"]:
                print(option)
            print("")
            while True:
                user = input("----->Enter your choice: ").strip().upper()
                if user == "A" or user == "B" or user == "C" or user == "D":
                    break
                else:
                    print("choose among choices(A,B,C,D)")
            # of_score += 1
            if user == q["answer"]:
                of_score += 1
                print("Bravo! correct choice")
                score += 1
                print(f"Your score is [{score}/{of_score}]")
            else:
                of_score += 1
                print(f"Wrong choice the correct option is {q['answer']}")
                print(f"Your score is [{score}/{of_score}]")
            sr_no += 1
            print("------------------------------------------------------------------")
        print('')
        final_score = score
        percentage = (final_score / 10) * 100
        print(f"You got {percentage}% in This Physics and Maths Quiz")
        if percentage < 10:
            print("Very Poor! You need a lot of practice.")
        elif percentage < 20:
            print("Poor! Keep learning.")
        elif percentage < 30:
            print("Below Average! Practice more.")
        elif percentage < 40:
            print("Average! You can do better.")
        elif percentage < 50:
            print("Fair! Keep improving.")
        elif percentage < 60:
            print("Good Job!")
        elif percentage < 70:
            print("Very Good!")
        elif percentage < 80:
            print("Great Work!")
        elif percentage < 90:
            print("Excellent!")
        elif percentage < 100:
            print("Outstanding!")
        else:
            print("Perfect Score! Genius!")
        break

def pb_quiz():
    selected_question = random.sample(physics_questions, 5)+random.sample(biology_questions ,5)
    random.shuffle(selected_question)
    score = 0
    of_score = 0
    sr_no = 1
    while True:
        for q in selected_question:
            print("")
            print(f"{sr_no}. {q['question']}")
            print("")
            for option in q["options"]:
                print(option)
            print("")
            while True:
                user = input("----->Enter your choice: ").strip().upper()
                if user == "A" or user == "B" or user == "C" or user == "D":
                    break
                else:
                    print("choose among choices(A,B,C,D)")
            # of_score += 1
            if user == q["answer"]:
                of_score += 1
                print("Bravo! correct choice")
                score += 1
                print(f"Your score is [{score}/{of_score}]")
            else:
                of_score += 1
                print(f"Wrong choice the correct option is {q['answer']}")
                print(f"Your score is [{score}/{of_score}]")
            sr_no += 1
            print("------------------------------------------------------------------")
        print('')
        final_score = score
        percentage = (final_score / 10) * 100
        print(f"You got {percentage}% in This Physics and Biology Quiz")
        if percentage < 10:
            print("Very Poor! You need a lot of practice.")
        elif percentage < 20:
            print("Poor! Keep learning.")
        elif percentage < 30:
            print("Below Average! Practice more.")
        elif percentage < 40:
            print("Average! You can do better.")
        elif percentage < 50:
            print("Fair! Keep improving.")
        elif percentage < 60:
            print("Good Job!")
        elif percentage < 70:
            print("Very Good!")
        elif percentage < 80:
            print("Great Work!")
        elif percentage < 90:
            print("Excellent!")
        elif percentage < 100:
            print("Outstanding!")
        else:
            print("Perfect Score! Genius!")
        break

def cb_quiz():
    selected_question = random.sample(biology_questions, 5)+random.sample(chemistry_questions ,5)
    random.shuffle(selected_question)
    score = 0
    of_score = 0
    sr_no = 1
    while True:
        for q in selected_question:
            print("")
            print(f"{sr_no}. {q['question']}")
            print("")
            for option in q["options"]:
                print(option)
            print("")
            while True:
                user = input("----->Enter your choice: ").strip().upper()
                if user == "A" or user == "B" or user == "C" or user == "D":
                    break
                else:
                    print("choose among choices(A,B,C,D)")
            # of_score += 1
            if user == q["answer"]:
                of_score += 1
                print("Bravo! correct choice")
                score += 1
                print(f"Your score is [{score}/{of_score}]")
            else:
                of_score += 1
                print(f"Wrong choice the correct option is {q['answer']}")
                print(f"Your score is [{score}/{of_score}]")
            sr_no += 1
            print("------------------------------------------------------------------")
        print('')
        final_score = score
        percentage = (final_score / 10) * 100
        print(f"You got {percentage}% in This Chemistry and Biology Quiz")
        if percentage < 10:
            print("Very Poor! You need a lot of practice.")
        elif percentage < 20:
            print("Poor! Keep learning.")
        elif percentage < 30:
            print("Below Average! Practice more.")
        elif percentage < 40:
            print("Average! You can do better.")
        elif percentage < 50:
            print("Fair! Keep improving.")
        elif percentage < 60:
            print("Good Job!")
        elif percentage < 70:
            print("Very Good!")
        elif percentage < 80:
            print("Great Work!")
        elif percentage < 90:
            print("Excellent!")
        elif percentage < 100:
            print("Outstanding!")
        else:
            print("Perfect Score! Genius!")
        break

def cm_quiz():
    selected_question = random.sample(maths_questions, 5)+random.sample(chemistry_questions ,5)
    random.shuffle(selected_question)
    score = 0
    of_score = 0
    sr_no = 1
    while True:
        for q in selected_question:
            print("")
            print(f"{sr_no}. {q['question']}")
            print("")
            for option in q["options"]:
                print(option)
            print("")
            while True:
                user = input("----->Enter your choice: ").strip().upper()
                if user == "A" or user == "B" or user == "C" or user == "D":
                    break
                else:
                    print("choose among choices(A,B,C,D)")
            # of_score += 1
            if user == q["answer"]:
                of_score += 1
                print("Bravo! correct choice")
                score += 1
                print(f"Your score is [{score}/{of_score}]")
            else:
                of_score += 1
                print(f"Wrong choice the correct option is {q['answer']}")
                print(f"Your score is [{score}/{of_score}]")
            sr_no += 1
            print("------------------------------------------------------------------")
        print('')
        final_score = score
        percentage = (final_score / 10) * 100
        print(f"You got {percentage}% in This Chemistry and Maths Quiz")
        if percentage < 10:
            print("Very Poor! You need a lot of practice.")
        elif percentage < 20:
            print("Poor! Keep learning.")
        elif percentage < 30:
            print("Below Average! Practice more.")
        elif percentage < 40:
            print("Average! You can do better.")
        elif percentage < 50:
            print("Fair! Keep improving.")
        elif percentage < 60:
            print("Good Job!")
        elif percentage < 70:
            print("Very Good!")
        elif percentage < 80:
            print("Great Work!")
        elif percentage < 90:
            print("Excellent!")
        elif percentage < 100:
            print("Outstanding!")
        else:
            print("Perfect Score! Genius!")
        break

def mb_quiz():
    selected_question = random.sample(maths_questions, 5)+random.sample(biology_questions ,5)
    random.shuffle(selected_question)
    score = 0
    of_score = 0
    sr_no = 1
    while True:
        for q in selected_question:
            print("")
            print(f"{sr_no}. {q['question']}")
            print("")
            for option in q["options"]:
                print(option)
            print("")
            while True:
                user = input("----->Enter your choice: ").strip().upper()
                if user == "A" or user == "B" or user == "C" or user == "D":
                    break
                else:
                    print("choose among choices(A,B,C,D)")
            # of_score += 1
            if user == q["answer"]:
                of_score += 1
                print("Bravo! correct choice")
                score += 1
                print(f"Your score is [{score}/{of_score}]")
            else:
                of_score += 1
                print(f"Wrong choice the correct option is {q['answer']}")
                print(f"Your score is [{score}/{of_score}]")
            sr_no += 1
            print("------------------------------------------------------------------")
        print('')
        final_score = score
        percentage = (final_score / 10) * 100
        print(f"You got {percentage}% in This Maths and Biology Quiz")
        if percentage < 10:
            print("Very Poor! You need a lot of practice.")
        elif percentage < 20:
            print("Poor! Keep learning.")
        elif percentage < 30:
            print("Below Average! Practice more.")
        elif percentage < 40:
            print("Average! You can do better.")
        elif percentage < 50:
            print("Fair! Keep improving.")
        elif percentage < 60:
            print("Good Job!")
        elif percentage < 70:
            print("Very Good!")
        elif percentage < 80:
            print("Great Work!")
        elif percentage < 90:
            print("Excellent!")
        elif percentage < 100:
            print("Outstanding!")
        else:
            print("Perfect Score! Genius!")
        break

def pcm_quiz():
    selected_question = random.sample(maths_questions, 4)+random.sample(chemistry_questions ,3)+random.sample(physics_questions,3)
    random.shuffle(selected_question)
    score = 0
    of_score = 0
    sr_no = 1
    while True:
        for q in selected_question:
            print("")
            print(f"{sr_no}. {q['question']}")
            print("")
            for option in q["options"]:
                print(option)
            print("")
            while True:
                user = input("----->Enter your choice: ").strip().upper()
                if user == "A" or user == "B" or user == "C" or user == "D":
                    break
                else:
                    print("choose among choices(A,B,C,D)")
            # of_score += 1
            if user == q["answer"]:
                of_score += 1
                print("Bravo! correct choice")
                score += 1
                print(f"Your score is [{score}/{of_score}]")
            else:
                of_score += 1
                print(f"Wrong choice the correct option is {q['answer']}")
                print(f"Your score is [{score}/{of_score}]")
            sr_no += 1
            print("------------------------------------------------------------------")
        print('')
        final_score = score
        percentage = (final_score / 10) * 100
        print(f"You got {percentage}% in This Physics, Chemistry and Maths Quiz")
        if percentage < 10:
            print("Very Poor! You need a lot of practice.")
        elif percentage < 20:
            print("Poor! Keep learning.")
        elif percentage < 30:
            print("Below Average! Practice more.")
        elif percentage < 40:
            print("Average! You can do better.")
        elif percentage < 50:
            print("Fair! Keep improving.")
        elif percentage < 60:
            print("Good Job!")
        elif percentage < 70:
            print("Very Good!")
        elif percentage < 80:
            print("Great Work!")
        elif percentage < 90:
            print("Excellent!")
        elif percentage < 100:
            print("Outstanding!")
        else:
            print("Perfect Score! Genius!")
        break

def pcb_quiz():
    selected_question = random.sample(biology_questions, 4)+random.sample(chemistry_questions ,3)+random.sample(physics_questions,3)
    random.shuffle(selected_question)
    score = 0
    of_score = 0
    sr_no = 1
    while True:
        for q in selected_question:
            print("")
            print(f"{sr_no}. {q['question']}")
            print("")
            for option in q["options"]:
                print(option)
            print("")
            while True:
                user = input("----->Enter your choice: ").strip().upper()
                if user == "A" or user == "B" or user == "C" or user == "D":
                    break
                else:
                    print("choose among choices(A,B,C,D)")
            # of_score += 1
            if user == q["answer"]:
                of_score += 1
                print("Bravo! correct choice")
                score += 1
                print(f"Your score is [{score}/{of_score}]")
            else:
                of_score += 1
                print(f"Wrong choice the correct option is {q['answer']}")
                print(f"Your score is [{score}/{of_score}]")
            sr_no += 1
            print("------------------------------------------------------------------")
        print('')
        final_score = score
        percentage = (final_score / 10) * 100
        print(f"You got {percentage}% in This Physics, Chemistry and Biology Quiz")
        if percentage < 10:
            print("Very Poor! You need a lot of practice.")
        elif percentage < 20:
            print("Poor! Keep learning.")
        elif percentage < 30:
            print("Below Average! Practice more.")
        elif percentage < 40:
            print("Average! You can do better.")
        elif percentage < 50:
            print("Fair! Keep improving.")
        elif percentage < 60:
            print("Good Job!")
        elif percentage < 70:
            print("Very Good!")
        elif percentage < 80:
            print("Great Work!")
        elif percentage < 90:
            print("Excellent!")
        elif percentage < 100:
            print("Outstanding!")
        else:
            print("Perfect Score! Genius!")
        break

def pcmb_quiz():
    selected_question = random.sample(maths_questions, 3)+random.sample(chemistry_questions ,2)+random.sample(physics_questions,2)+random.sample(biology_questions ,3)
    random.shuffle(selected_question)
    score = 0
    of_score = 0
    sr_no = 1
    while True:
        for q in selected_question:
            print("")
            print(f"{sr_no}. {q['question']}")
            print("")
            for option in q["options"]:
                print(option)
            print("")
            while True:
                user = input("----->Enter your choice: ").strip().upper()
                if user == "A" or user == "B" or user == "C" or user == "D":
                    break
                else:
                    print("choose among choices(A,B,C,D)")
            # of_score += 1
            if user == q["answer"]:
                of_score += 1
                print("Bravo! correct choice")
                score += 1
                print(f"Your score is [{score}/{of_score}]")
            else:
                of_score += 1
                print(f"Wrong choice the correct option is {q['answer']}")
                print(f"Your score is [{score}/{of_score}]")
            sr_no += 1
            print("------------------------------------------------------------------")
        print('')
        final_score = score
        percentage = (final_score / 10) * 100
        print(f"You got {percentage}% in This Physics and Chemistry and Maths and Biology Quiz")
        if percentage < 10:
            print("Very Poor! You need a lot of practice.")
        elif percentage < 20:
            print("Poor! Keep learning.")
        elif percentage < 30:
            print("Below Average! Practice more.")
        elif percentage < 40:
            print("Average! You can do better.")
        elif percentage < 50:
            print("Fair! Keep improving.")
        elif percentage < 60:
            print("Good Job!")
        elif percentage < 70:
            print("Very Good!")
        elif percentage < 80:
            print("Great Work!")
        elif percentage < 90:
            print("Excellent!")
        elif percentage < 100:
            print("Outstanding!")
        else:
            print("Perfect Score! Genius!")
        break

while True:
    user = int(input("Select the respective number among subjects to play Quiz Game: "))
    print("------------------------------------------------------------------")
    if user == 1:
        print("You are in the Maths quiz , All the best buddy!!")
        math_quiz()
    elif user == 2:
        print("You are in the Physics quiz , All the best buddy!!")
        physics_quiz()
    elif user == 3:
        print("You are in the Chemistry quiz , All the best buddy!!")
        chemistry_quiz()
    elif user == 4:
        print("You are in the Biology quiz , All the best buddy!!")
        biology_quiz()
    elif user == 5:
        print("You are in the Physics and Chemistry quiz , All the best buddy!!")
        pc_quiz()
    elif user == 6:
        print("You are in the Physics and Maths quiz , All the best buddy!!")
        pm_quiz()
    elif user == 7:
        print("You are in the Physics and Biology quiz , All the best buddy!!")
        pb_quiz()
    elif user == 8:
        print("You are in the Chemistry and Biology quiz , All the best buddy!!")
        cb_quiz()
    elif user == 9:
        print("You are in the Chemistry and Maths quiz , All the best buddy!!")
        cm_quiz()
    elif user == 10:
        print("You are in the Maths and Biology quiz , All the best buddy!!")
        mb_quiz()
    elif user == 11:
        print("You are in the PCM quiz , All the best buddy!!")
        pcm_quiz()
    elif user == 12:
        print("You are in the PCM quiz , All the best buddy!!")
        pcb_quiz()
    elif user == 13:
        print("You are in the PCMB quiz , All the best buddy!!")
        pcmb_quiz()
    else:
        print("Please Choose between 1-13 only")
    while True:
        print("")
        print("Hope You Enjoyed and Learnt something at the same this.")
        print("")
        a = input("Do you want to play again?[y/n]").strip().lower()
        if a == "y":
            break
        elif a == "n":
            exit()
        else:
            print("Please choose between {y/n} only")
        

