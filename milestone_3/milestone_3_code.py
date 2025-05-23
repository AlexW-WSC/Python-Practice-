print("Welcome to the quiz!!!! 3 questions, dont lose or you're stupid.")
print("")


# If you would like to edit this script, you can simply place each question and correct answer into their respective list variables. Please ensure that each question is 'paired' with an answer (question 1 in the questions list should would be answer 1 in the answers list, etc.), and that both lists contain the same number of items.

questions = ["What colour are baby pandas?", "How is 'else if' written in Python?", "What is the meaning of the life?"]
correctanswers = ["pink", "elif", "42"]

if len(questions) != len(correctanswers):   
    print("There is not the same amount of questions as there is answers.")
    quit()

playing = True 
score = 0


while playing == True:
    score = 0
    for i in range(len(questions)):
        
        if playing == True:
            answer = None
            answer = input("Question {}: ".format(i + 1) + questions[i]).strip().lower()
    
            if answer == correctanswers[i]:
                print("{} was correct, great job.".format(correctanswers[i]))
                score += 1
            else:
                print("{} was incorrect, better luck next time!".format(answer))
            answer = None
    if score == len(questions):
        print("Your score was {}/{}. You got them all correct!".format(score, len(questions)))
    elif score >= (len(questions) / 2):
        print("Your score was {}/{}. Not bad.".format(score, len(questions)))
    elif score <= (len(questions) / 2) and score != 0:
        print("Your score was {}/{}. A good effort.".format(score, len(questions)))
    elif score == 0:
        print("Your score was {}/{}. You got them all wrong. Better luck next time!".format(score, len(questions)))
    
    playing_status = input("Would you like to try again?").strip().lower()
    if playing_status == "no":
        playing = False
        
print("Thanks for playing!")
quit()


        
    
