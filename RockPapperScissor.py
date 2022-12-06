"Welcome to Mauseem's Rock paper Scissor.."
import pyttsx3
import random
import time

engine = pyttsx3.init()
# engine.say("I will speak this text")

Name = input("Enter your name : ")
time.sleep(1)
engine.say(f"Hello {Name}")
Greet = print(f"Hello {Name}")
engine.runAndWait()

time.sleep(1)

engine.say("The Game is about to begin.")
Begin = print("The Game is about to begin.")
engine.runAndWait()

time.sleep(1)

engine.say('Lets Go!!!')
print('Lets Go!!!')
engine.runAndWait()

# Option =  ("Rock","Paper","Scissor")
def RockPaperScissor():
    Option =  ("Rock","Paper","Scissor")
    Choice = input("Enter your choice. Rock,Paper or Scissor : ")
    engine.say(f"You chose {Choice}")
    # engine.runAndWait()
    
    AIChoice = random.choice(Option)

    if Choice == "Paper" and AIChoice == "Rock":
       Outcome = f"Computer chose {AIChoice} you won"
    elif Choice == "Rock" and AIChoice == "Paper":
        Outcome = f"Computer chose {AIChoice} you lose"
    elif Choice == "Scissor" and AIChoice == "Paper":
        Outcome = f"Computer chose {AIChoice} you won"
    elif Choice == "Paper" and AIChoice == "Scissor":
        Outcome  = f"Computer chose {AIChoice} you lose"
    elif Choice == "Rock" and AIChoice == "Scissor":
        Outcome = f"Computer chose {AIChoice} you won"
    elif Choice == "Scissor" and AIChoice == "Rock":
        Outcome = f"Computer chose {AIChoice} you lose"
    else:
        Outcome = "Darn Computer Chose the same Word"
    engine.say(Outcome)
    

RockPaperScissor()
engine.runAndWait()
