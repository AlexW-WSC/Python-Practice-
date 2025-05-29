import random

# If you would like to edit this script, you can simply place each question and correct answer into their respective list variables. Please ensure that each question is 'paired' with an answer (question 1 in the questions list should would be answer 1 in the answers list, etc.), and that both lists contain the same number of items.



# lists with questions, answers
questions = ["What colour are baby pandas?", "How is 'else if' written in Python?", "What is the meaning of life?",]
correctanswers = ["pink", "elif", "42"]



# aborts the application if the amount of questions is not the same as the amount of answers(the script will not work.)
if len(questions) != len(correctanswers):   
    print("There is not the same amount of questions as there is answers. Stopping script..")
    quit()



print("Welcome to the quiz!!!! This quiz has {} questions. None of your answers are stored.".format(len(questions)))
print("")




# sets essential variables for the loop
playing = True 
score = 0

# main logic loop starts here, first checks for the playing variable (in case of a retry)
while playing == True:
    score = 0

    #randomises question order
    temp_list = list(zip(questions, correctanswers)) # pairs lists
    random.shuffle(temp_list) # shuffles the pair 
    question_list_temp, answer_list_temp = zip(*temp_list) # unzips again

    questions, correctanswers = list(question_list_temp), list(answer_list_temp) # reassign the lists 


    for i in range(len(questions)):
        
        if playing == True:
            answer = None
            # pulls the question from the list and asks for input 
            answer = input("Question {}: ".format(i + 1) + questions[i]).strip().lower()
            
            # increases score if answer is correct 
            if answer == correctanswers[i]:
                print("{} was correct, great job.".format(correctanswers[i]))
                score += 1
            else:
                print("{} was incorrect, better luck next time!".format(answer))
            if answer == None:
                print("0w0 you entered nothing")
            answer = None
    # after the loop, prints scores based on percentage of answers correct(100%, over 50%, under 50%, 0%)
    if score == len(questions):
        print("Your score was {}/{}. You got them all correct!".format(score, len(questions)))
    elif score >= (len(questions) / 2):
        print("Your score was {}/{}. Not bad.".format(score, len(questions)))
    elif score <= (len(questions) / 2) and score != 0:
        print("Your score was {}/{}. A good effort.".format(score, len(questions)))
    elif score == 0:
        print("Your score was {}/{}. You got them all wrong. Better luck next time!".format(score, len(questions)))
    # checks if the loop should run again absed on the 'playing' variable 
    playing_status = input("Would you like to try again?").strip().lower()
    if playing_status == "yes":
        playing = True
    else:
        playing = False
# otherwise, ends the script        
print("Thanks for playing!")
quit()


        
    
