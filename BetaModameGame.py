"""
Main Game
With other files intertwined together

Read LICENSE.txt
"""

#IMPORTS

##FILES##
from DatabaseHandling import *
from REDACTED import *
from Testing import *
##FILES##

##NEEDED IMPORTS##
import random, time, hashlib, string
from os import system
from getpass import getpass
##NEEDED IMPORTS#

#IMPORTS

#LOCAL DATABASE
User_money = {'hellom38' : 100, 'TEST' : 300,'soldadoborjarex' : 200}
Pmoney = {'hellom38' : 0, 'TEST' : 20, 'soldadoborjarex' : 100}
bonuses = {'hellom38' : 12,'TEST' : 1,'soldadoborjarex' : 2}
Printable_strings = string.printable
Printable_strings.strip(' ')
#LOCAL DATABASE

#TOOLS
def SearchUser(User0):
    User2 = input("User:")
    User3 = Get_DB(MainDB,User2,"",Main_cur,"MainTable","User","","Maybe")
    if User3 == []:
        print("no such user")
    else:
        User4 = User3[0]
        print("Name:",User4[0])
        print("MoneyP:",User4[1])
        print("MoneyB:",User4[2])
        print("Multipliers:",User4[3])
        if User0 == "hellom38":
            print("Position: Creator")
        else:
            print("Position: Beta Tester")
        input()
    ToolTransportation(User0)

def Leaderboard(User0):
    print("1. hellom38, 347 $, 6 multipliers")
    print("under dev")
    ToolTransportation(User0)
    """Users = Get_DB(MainDB,"","",Main_cur,"MainTable","","","Maybe")
    LeaderboardOrder = []
    UserOrder = []

    for i in Users:
        money = int(i[1]) + int(i[2])
        LeaderboardOrder.append(int(money))

        UserOrder.append(i[0])
        print(LeaderboardOrder)
    LeaderboardOrder = LeaderboardOrder.sort()
    while True:
        i=0
        print(str(UserOrder[i]),":",str(LeaderboardOrder[i]))
        i =+ 1


    print(User2)
    input()
    ToolTransportation(User0)
    """
#TOOLS

#BANK
def Gift_money(UserL,UserM):
    user = input('what user would you like to give money to? ')
    if Get_DB(LoginDB,user,"",Login_Cur,"LoginDetails","User","",False) == False:
        amount = input('how much?')
        if CheckValue(amount):
            if int(amount) <= int(UserM[1]):
                User = Get_DB(LoginDB,user,"",Login_Cur,"LoginDetails","User","","Maybe")
                Alter_DB(MainDB,(int(User[1]) + int(amount)),Main_cur,"MainTable","MoneyP","User",user)
                Alter_DB(MainDB,(int(UserM[1]) - int(amount)),Main_cur,"MainTable","MoneyP","User",UserL[0])
                print('successfully given the money to:',user)
            else:
                print('you haven\'t got enough money')
        else:
            print('not number value')
    else:
        print('something went wrong')
    system("cls")
    transportationZone(UserL[0])

def put_inMoney(UserL,UserM):
    put_inAmount = input('how much would you like to put in? numbers please ')
    if CheckValue(put_inAmount) == True:
        if int(put_inAmount) <= int(UserM[1]):
            Alter_DB(MainDB,(int(UserM[2]) - int(put_inAmount)),Main_cur,"MainTable","MoneyB","User",UserM[0])
            Alter_DB(MainDB,(int(UserM[1]) + int(put_inAmount)),Main_cur,"MainTable","MoneyP","User",UserM[0])
            print('sucesfully transferred')
            input()
            system("cls")
            transportationZone(UserL[0])
        else:
            print('you can\'t because you have got less than what you put')
            system("cls")
            transportationZone(UserL[0])
    else:
        print('try again')
        system("cls")
        TransportationZone(UserL[0])

def withdrawMoney(UserL,UserM):
    put_outAmount = input('how much would you like to put out? numbers please ')
    if CheckValue(put_outAmount) == True:
        if int(put_outAmount) <= int(UserM[2]):
            Alter_DB(MainDB,(int(UserM[1]) + int(put_outAmount)),Main_cur,"MainTable","MoneyP","User",UserM[0])
            Alter_DB(MainDB,(int(UserM[2]) - int(put_outAmount)),Main_cur,"MainTable","MoneyB","User",UserM[0])
            print('sucefully transferred')
            input()
            system("cls")
            transportationZone(UserL[0])
        else:
            print('you can\'t because you have got less than what you put')
            system("cls")
            transportationZone(UserL[0])
    else:
        print("did not work")
        transportationZone(UserL[0])
#BANK



#PLAY
def StartPlay(UserL,UserM):
    print('lets start playing')
    print('welcome to 9 lives')
    clue = []
    words = ['shirt', 'otter', 'rocks', 'plane', 'teeth', 'fairy', 'pizza', 'gorilla', 'cheese', 'parrot', 'hippopotamus', 'mississippi', 'giraffe', 'orange']
    secret_word = random.choice(words)
    lives = 0
    difficulty = input('what difficulty\n easy, press \"1\" \n medium, press \"2\" \n difficult, press \"3\"')
    if difficulty == '3':
            lives = 4
    elif difficulty == '2':
            lives = 6
    elif difficulty == '1':
        lives = 9
    else:
        print('Incorrect, Restarting game')


    heart_symbol = u'\u2764'


    index = 0
    while index < len(secret_word):
        clue.append('?')
        index = index + 1


    def check_word(guessed_letter, clue, secret_word):
        index = 0
        while index < len(secret_word):
            if guessed_letter.lower() == secret_word[index].lower():
                clue[index] = guessed_letter
            index = index + 1


    while lives > 0:
        print(clue)
        print('lives left: ' + heart_symbol * lives)
        guess = input("guess the letter or the whole word: ")

        if guess == secret_word:
            print("correct")
            if difficulty == '3':
                Alter_DB(MainDB,(int(UserM[1]) + 20),Main_cur,"MainTable","MoneyP","User",UserL[0])
            elif difficulty == '2':
                Alter_DB(MainDB,(int(UserM[1]) + 13),Main_cur,"MainTable","MoneyP","User",UserL[0])

            elif difficulty == '1':
                Alter_DB(MainDB,(int(UserM[1]) + 8),Main_cur,"MainTable","MoneyP","User",UserL[0])
            transportationZone(UserL[0])


        if guess in secret_word:
            check_word(guess, clue, secret_word)

        else:
            print('Incorrect, you lose a life')
            lives = lives - 1

    if lives == 0:
        print("you lost, the answer was: " + secret_word)
        system("cls")
        transportationZone(UserL[0])

def RobotGame():

    now = time.time()
    future = now + 60
    while time.time() < future:

        max_num = 30

        random_number = random.randint(1, max_num)
        guess = 0
        while guess != random_number :
            guess = int(input(f"Guess the number between 1 & {max_num}: "))
            if guess < random_number:
                print("Wrong! Too low...")
            elif guess > random_number:
                print("Wrong! Too high...")
        print(f"Thats Right! Random number is {random_number}")
    print("time up")
    Start()
#PLAY



#SETTINGS
def ChangePwd_or_User(User):
    select = input('[1] password\n[2] User\n')
    if '1' in select:
        select2 = getpass('(if you would like to exit, press 1)\nnew password: ')
        if len(select2) > 4 and len(select2) < 20:
            if '1' != select2:
                Alter_DB(LoginDB,Hash(select2),Login_Cur,"LoginDetails","Pass","User",User[0])
            else:
                print("cancelled")
                transportationZone(User[0])
        else:
            print("Has to be less than 20 characters and more than 4")
            transportationZone(User[0])
    elif '2' in select:
        select3 = input('(if you would like to exit,press 1)\nnew user: ')
        if Get_DB(LoginDB,select3,"",Login_Cur,"LoginDetails","User","",True) == True:
            if len(select3) > 4 and len(select3) < 20:
                if '1' != select3:
                    Alter_DB(LoginDB,select3,Login_Cur,"LoginDetails","User","User",User)
                else:
                    print("cancelled")
                    transportationZone(User[0])
            else:
                print("Has to be less than 20 characters and more than 4")
                transportationZone(User[0])

        else:
            print("Username already exists")
            transportationZone(User[0])

    else:
        print('did not understand')
        time.sleep( 1 )
    system("cls")
    transportationZone(User[0])
#SETTINGS


#TRANSPORTATIONS
def ToolTransportation(User):
    Tool = input("[1] Search User\n[2] Leaderboard\n[3] exit\n")
    if "1" in Tool:
        SearchUser(User)
    elif "2" in Tool:
        Leaderboard(User)
    elif "3" in Tool:
        transportationZone(User)
    else:
        print("did not understand")
        system("cls")
        ToolTransportation(User)

def AdminTransportation(User):
    transportationA = input("[1] Delete\n[2] Add\n[3] Get\n[4] Execute\n[5] Exit\n")
    if "1" in transportationA:
        Ask = input("User:")
        Delete_DB(LoginDB,Ask,Login_Cur,"LoginDetails","User")
        AdminTransportation(User)
    elif "2" in transportationA:
        Ask1 = input("INPUT:")
        Ask2 = input("INPUT2:")
        Ask4 = input("COLUMN1:")
        Ask5 = input("COLUMN2:")
        Ask6 = input("TABLE:")


        Create_DB(LoginDB,Ask1,Ask2,"","",Login_Cur,Ask6,Ask4,Ask5,"","")
        AdminTransportation(User)
    elif "3" in transportationA:
        Ask1 = input("INPUT:")
        Ask2 = input("INPUT2:")
        Ask4 = input("COLUMN1:")
        Ask5 = input("COLUMN2:")
        Ask6 = input("TABLE:")


        Get_DB(LoginDB,Ask1,Ask2,Login_Cur,Ask6,Ask4,Ask5,True)

        AdminTransportation(User)
    elif "4" in transportationA:
        executer = input("CODE:")
        try:
            exec(executer)
        except Exception as e:
            print("Error:",e)
        finally:
            AdminTransportation(User)
    elif "5" in transportationA:
        transportationZone(User)
    else:
        print("did not understand")
        AdminTransportation(User)

def transportationBank(UserL,UserM):
    print('Hello',UserL[0])
    print('Welcome the bank')
    transportation1 = input('[1] Withdraw\n[2] Balance\n[3] Put in\n[4] Give money\n[5] exit\n')
    if '2' in transportation1:
        print('your bank balance is:',UserM[2], 'and your player money is:', UserM[1])
        transportationZone(UserL[0])
    elif '1' in transportation1:
        system("cls")
        withdrawMoney(UserL,UserM)
    elif '3' in transportation1:
        system("cls")
        put_inMoney(UserL,UserM)
    elif '4' in transportation1:
        system("cls")
        Gift_money(UserL,UserM)
    elif '5' in transportation1:
        system("cls")
        transportationZone("LOL")
    else:
        print('did not understand')
        system("cls")
        transportationBank(UserL,UserM)

def transportationZone(User):
    transportation0 = input('[1] play\n[2] bank\n[3] settings\n[4] Tools\n[5] log out\n')
    Money = Get_DB(MainDB,User,"",Main_cur,"MainTable","User","","Maybe")
    Login = Get_DB(LoginDB,User,"",Login_Cur,"LoginDetails","User","","Maybe")
    Login3 = Login[0]
    Money1 = Money[0]
    if '2' in transportation0:
        system("cls")
        transportationBank(Login3,Money1)
    elif '1' in transportation0:
        system("cls")
        StartPlay(Login3,Money1)
    elif 'hack' in transportation0:
        system("cls")
        REDACTEDTransportation(User)
    elif 'secret' in transportation0:
        system("cls")
        print("LOL")
        transportationZone(User)
    elif '3' in transportation0:
        system("cls")
        ChangePwd_or_User(Login3)
    elif 'Admin' in transportation0:
        system("cls")
        if User == "hellom38":
            AdminTransportation(User)


    elif '4' in transportation0:
        ToolTransportation(User)

    elif '5' in transportation0:
        system("cls")
        Start()

    else:
        print('try again')
        system("cls")
        transportationZone(User)
#TRANSPORTATIONS


#START
def Login2(Logins):


    while Logins < 6:

        login_username = input('User: ')
        login_password = getpass('password: ')
        Finder = Get_DB(LoginDB,login_username,Hash(login_password),Login_Cur,"LoginDetails","User","Pass",False)
        if Finder != True:

            print('Welcome back', login_username)
            system("cls")
            transportationZone(login_username)

        else:
            print('Password or/and user does not match')
            Logins += 1
            print(Logins)
            system("cls")
            Login2(Logins)




    else:
        forgot_password = input('did you forget your username or Password?')
        if 'yes' in forgot_password:
            try:
                print('checking if you have got the Password_ModameGame file..')
                FindFile = open('Password_ModameGame.txt', 'r')
            except IOError:
                print('failed to get file')
                system("cls")
                CheckIfRobot()
            else:
                Info = FindFile.readlines()
                print('here is your information:', Info)
                FindFile.close()
                Login2(0)

        else:
            system("cls")
            CheckIfRobot()

def RegisterUser():
    print('register!!')
    create_username = input('New User: ')
    create_password = getpass('New password: ')
    if Get_DB(LoginDB,create_username,"",Login_Cur,"LoginDetails","User","",False) == True:
        if len(create_username) and len(create_password) > 4:

            print('sucefully registered')
            print('saving password in file \'Password_ModameGame\'')
            try:
                PasswordFile = open('Password_ModameGame.txt', 'w')
                PasswordFile.write('User:')
                PasswordFile.write(create_username)
                PasswordFile.write('\nPassword:')
                PasswordFile.write(create_password)
                PasswordFile.close()
                Create_DB(LoginDB,create_username,Hash(create_password),"","",Login_Cur,"LoginDetails","User","Pass","","")
                Create_DB(MainDB,create_username,0,100,"",Main_cur,"MainTable","User","MoneyP","MoneyB","Multipliers")

            except IOError:
                print ("Error: can\'t find file or read data")
                system("cls")
                Start()

            else:
                print("Written content in the file successfully")
                PasswordFile.close()
                system("cls")
                transportationZone(create_username)
        else:
            print('has to be more than 4 characters!')
            system("cls")
            Start()

    else:
        print('username already exists!!')
        system("cls")
        Start()

def Start():
    Login1 = ''
    print('Welcome player to the modame game!! v1.2')
    Login1 = input('[1] Sign up\n[2] Log in\n')
    if '2' in  Login1:
        print('Welcome back!!')
        system("cls")
        Login2(0)
    elif '1' in Login1:
        system("cls")
        RegisterUser()
    else:
        print('program did not work, restarting.')
        system("cls")
        Start()
#START


#OTHER
def CheckIfRobot():
            Robotlist = ['hello','Robot', 'cat', 'dog','golf']
            RobotWord = random.choice(Robotlist)
            RobotNumber = random.randint(1,100000)
            RobotText = ('write this number plus the  text for ex: 10 and hello = 15:',RobotWord, 'and:',str(RobotNumber))
            RobotTest = input(RobotText)
            if CheckValue(RobotTest):
                if int(RobotTest) == (len(RobotWord) + RobotNumber):
                    print('you are going to have to wait 1 minute until trying again')
                    print('if we did something wrong, in this part, \nit is because in the if you forgot the password, you had to say yes')
                    RobotGame()

                else:
                    print('try again')
                    system("cls")
                    CheckIfRobot()
            else:
                print('try again')
                system("cls")
                CheckIfRobot()

def Hash(Word):

    Word = hashlib.sha256(str.encode(Word)).hexdigest()
    return Word

def CheckValue(type_word):
    try:
        int(type_word)
        return True
    except:
        return False
#OTHER


if __name__ == '__main__':
    '''print("Beta DatastoreOther")
    BetaWork()'''

    print("v1.2(Bug update and other)\nDatastore in next update :D")
    time.sleep( 2 )
    system("cls")
    Start()
