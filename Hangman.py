import random
from hang_art import stages,logo
import time
name=input("Enter your name : ")
print(f" Hello! {name.upper()}...")
time.sleep(1)
print(logo)
time.sleep(1)
print("Welcome to Hangman game....")
time.sleep(1)
print("INSTRUCTIONS TO PLAY THIS GAME...")
time.sleep(1)
print("1.Guess the word that was choosen randomly....")
time.sleep(1)
print("2.You have 6 chances to play...")
time.sleep(1)
print("3.Every wrong guess reduces a chance and your points... ")
time.sleep(1)
print("4.Your chances at end will be your score...")
time.sleep(1)
score=0
play='yes'
while play.lower()=='yes':

    list_of_words=["red","rhino","audi","lenovo","apple"]
    chosen_word=random.choice(list_of_words)
    chosen_word_1=[]
    for char in chosen_word:
        chosen_word_1.append(char)
    st=[]
    for i in range(len(chosen_word)):
        st.append("_")
    chances=6
    chance=""
    while chances>0 :
        user_guess=input("Enter your guess:")
        flag = []
        word_s=""
        print(user_guess)
        for i in range(len(chosen_word_1)):
            if user_guess.lower()==chosen_word_1[i]:
                st[i]=chosen_word_1[i]
                flag.append(True)
            else:
                flag.append(False)
        count=flag.count(True)
        if count>0:
            print(f"You have guessed correctly! you have {chances} chances")
        else:
            chances-=1
            print(stages[chances])
            print(f"You have guessed incorrectly! you have {chances} chances ")
        print(st)
        for char in st:
            word_s+=char
        chance = chances
        if chosen_word.lower()==word_s.lower():
            print(f"You WON ! you have {chances} more")
            score=chances*2
            print(f"Your Score was : {score} POINTS")

            chances=0
    if chance==0:
        print(f'YOU Lost !')
        score=chances
        print(f"Your score was {score} points....")
    play = input("Enter yes if you want to play no if you don't want to play : ")
if play.lower()=='no':
    print(f"Thank you {name} for playing the HANGMAN......")
    print("Hope you liked it pretty WELL....")
    print("You have chosen to exit")
