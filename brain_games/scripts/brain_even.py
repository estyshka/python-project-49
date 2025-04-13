
from brain_games.scripts.main import greet
from random import randint
import prompt
#отвечают Биллу, надо исправить


def main():
    greet()
    welcome_user()
    rule()
    ask()
    answer()

def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)


def rule():
    print('Answer "yes" if the number is even, otherwise answer "no".')




number = randint(0, 100)


def ask():
    print('Question: ' + str(number))




def answer():


    if number % 2 == 0:
        flag = True
    else:
        flag = False
    answ = prompt.string('Your answer: ')
    if answ == 'yes' and flag == True or answ == 'no' and flag == False:
        print('Correct!')
        def answer1():
            number = randint(0, 100)
            if number % 2 == 0:
                flag = True
            else:
                flag = False
            print('Question: ' + str(number))
            answ = prompt.string('Your answer: ')
            if answ == 'yes' and flag == True or answ == 'no' and flag == False:
                print('Correct!')


                number = randint(0, 100)
                if number % 2 == 0:
                    flag = True
                else:
                    flag = False
                print('Question: ' + str(number))
                answ = prompt.string('Your answer: ')
                if answ == 'yes' and flag == True or answ == 'no' and flag == False:
                    print('Correct!')
                
                elif answ == 'yes' and flag == False:

                    print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, " + name + '!')
                elif answ == 'no' and flag == True:

                    print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, " + name + '!')
                elif flag == True:

                    print(f"'{answ}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
                elif flag == False:

                    print(f"'{answ}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")



            elif answ == 'yes' and flag == False:

                print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, " + name + '!')
            elif answ == 'no' and flag == True:

                print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, " + name + '!')
            elif flag == True:

                print(f"'{answ}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            elif flag == False:

                print(f"'{answ}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
        answer1()
    
            
                

    elif answ == 'yes' and flag == False:

        print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, " + name + '!')
    elif answ == 'no' and flag == True:

        print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, " + name + '!')
    elif flag == True:

        print(f"'{answ}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
    elif flag == False:

        print(f"'{answ}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")


