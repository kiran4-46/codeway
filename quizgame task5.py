#writing a python program to create a quiz game
def main():
    score = 0
    number_of_questions = 0
    print("Welcome to quiz game");
    print("Note:\n 1. If should enter the answer accurately avoid spelling mistakes");
    print("2. No negative marks for wrong answers")

    user_response = input("Do you want to play this game ? ").lower();

    if(user_response == "yes"):
        # question 1 
        number_of_questions += 1 
        print(f"{number_of_questions}. What is the full form of API ? ")
        print("a. Application Programming Interface")
        print("b. Application Program Interface")
        print("c. App Programming Interface")
        print("d. Application Programming Intermission")
        question = input("Enter your answer ")
        if(question == "Application Programming Interface"):
            print("Correct Answer")
            score += 1
        else:
            print("wrong answer")
            print("Correct Answer is ---->  Application Programming Interface")
        # question 2
        number_of_questions += 1 
        print(f"{number_of_questions}. Who developed python programming language ? ")
        print("a. Guido Rosam")
        print("b. Guido Van Rossum")
        print("c. Rasmos")
        print("d. Niene storm")
        question = input("Enter your answer ")
        if(question == "Guido Van Rossum"):
            print("Correct Answer")
            score += 1
        else:
            print("wrong answer")
            print("Correct Answer is ---->  Guido Van Rossum")
        # question 3
        number_of_questions += 1 
        print(f"{number_of_questions}. Which type of programming does python support ? ")
        print("a. Object-oriented programming")
        print("b. Structured programming")
        print("c. Functional programming")
        print("d. All of the above")
        question = input("Enter your answer ")
        if(question == "All of the above"):
            print("Correct Answer")
            score += 1
        else:
            print("wrong answer")
            print("Correct Answer is ---->  All of the above")
        # question 4
        number_of_questions += 1 
        print(f"{number_of_questions}. Is Python case sensitive while dealing with identifiers?")
        print("a. No")
        print("b. Yes")
        print("c. Machine mode")
        print("d. None of the options")
        question = input("Enter your answer ")
        if(question == "None of the options"):
            print("Correct Answer")
            score += 1
        else:
            print("wrong answer")
            print("Correct Answer is ---->  None of the options")
        # question 5?
        number_of_questions += 1 
        print(f"{number_of_questions}. Which of the followin is the correct extention of a python file ?")
        print("a. .py")
        print("b. .pi")
        print("c. .pl")
        print("d. .p")
        question = input("Enter your answer ")
        if(question == ".py"):
            print("Correct Answer")
            score += 1
        else:
            print("wrong answer")
            print("Correct Answer is ---->  .py")
        # question 6
        number_of_questions += 1 
        print(f"{number_of_questions}. Which of the following keyword is used to defining a function in python programming language ? ")
        print("a. def")
        print("b. define")
        print("c. function")
        print("d. Define")
        question = input("Enter your answer ")
        if(question == "def"):
            print("Correct Answer")
            score += 1
        else:
            print("wrong answer")
            print("Correct Answer is ---->  def")
    else:
        print("Thank you for existing in the quiz game, try again !")
    
    try:
        avgScore = (score * 100)/number_of_questions
        print(f'{avgScore} % of the score');
    except ZeroDivisionError:
        print("0% of the score")
            
            
if __name__ == "__main__":
    main()
__name__ == "__main__"
    