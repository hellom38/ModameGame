#databaseHandling.py
"""
Language: Python and SQL
Role: Controlling DB

Databases = [REDACTED].db
            Login$_ModameDatabase.db
            Testing$_ModameDatabase.db
            Main$_ModameDatabase.db

Python Programs:
                [CENSORED].py
                ModameGameMain.py
                ModameGameBeta.py
                Testing.py


Other: index.html
       view.css
       interact.js

FORMAT:
      LoginDB = table: LoginDetails(User,Pass)
      TestingDB = table: TestingTable(Word)
      REDACTED_DB = table: HackingTable(Query)
      MainDB = table: MainTable(User,MoneyP,MoneyB,Multipliers)
"""

#Connection
import sqlite3
REDACTED_DB = sqlite3.connect("Example.db")
LoginDB = sqlite3.connect("Login$_ModameDatabase.db")
TestingDB = sqlite3.connect("Testing$_ModameDatabase.db")
MainDB = sqlite3.connect("Main$_ModameDatabase.db")
#cursor
REDACTED_Cur = REDACTED_DB.cursor()
Login_Cur = LoginDB.cursor()
Testing_cur = TestingDB.cursor()
Main_cur = MainDB.cursor()


def Create_DB(DB,INPUT,INPUT2,INPUT3,INPUT4,CURSOR,TABLE,Column1,Column2,Column3,Column4):
    try:
        if Column2 == "":

            QueryRequest = f""" INSERT INTO "{TABLE}" ("{Column1}") VALUES ("{INPUT}")"""
        elif Column3 == "":
            QueryRequest = f""" INSERT INTO "{TABLE}" ("{Column1}","{Column2}") VALUES ("{INPUT}","{INPUT2}") """
        elif Column4 == "":
            QueryRequest = f""" INSERT INTO "{TABLE}" ("{Column1}","{Column2}","{Column3}") VALUES ("{INPUT}","{INPUT2}","{INPUT3}") """
        else:
            QueryRequest = f""" INSERT INTO "{TABLE}" ("{Column1}","{Column2}","{Column3}","{Column4}") VALUES ("{INPUT}","{INPUT2}","{INPUT3}","{INPUT4}") """
        CURSOR.execute(QueryRequest)
    except sqlite3.Error as e:
        print("Error has happened:",e)
    else:
        print("Worked succesfully")
        DB.commit()

def Get_DB(DB,INPUT,INPUT2,CURSOR,TABLE,Column1,Column2,SHOW):
    try:
        if Column1 != "":
            if Column2 == "":

                QueryRequest = f""" SELECT * FROM "{TABLE}" WHERE "{Column1}" = "{INPUT}" """
            else:

                QueryRequest = f""" SELECT * FROM "{TABLE}" WHERE "{Column1}" = "{INPUT}" AND "{Column2}" = "{INPUT2}" """
        else:
            QueryRequest = f""" SELECT * FROM "{TABLE}" """

        CURSOR.execute(QueryRequest)

    except sqlite3.Error as e:
        print("Error has happened:",e)
    else:
        HOLDER = CURSOR.fetchall()
        if SHOW == True:
            print(HOLDER)
        if SHOW == "Maybe":
            return HOLDER
        else:
            pass
        if HOLDER == []:
            return True
        else:
            return False

def Delete_DB(DB,INPUT,CURSOR,TABLE,Column1):
    try:
        if INPUT != "":
            QueryDelete = f""" DELETE FROM "{TABLE}" WHERE "{Column1}" = "{INPUT}" """
        else:
            QueryDelete = f""" DELETE FROM "{TABLE}" """

        CURSOR.execute(QueryDelete)

    except sqlite3.Error as e:
        print("Error has happened:",e)
    else:
        print("Worked succesfully")
        DB.commit()

def Alter_DB(DB,NEW_INPUT,CURSOR,TABLE,Column1,CONDITION,RESULT):
    try:

        QueryRequest = f""" UPDATE "{TABLE}" SET "{Column1}" = "{NEW_INPUT}" WHERE "{CONDITION}" = "{RESULT}" """

        CURSOR.execute(QueryRequest)
    except sqlite3.Error as e:
        print("Error has happened:",e)
    else:
        print("Worked succesfully")
        DB.commit()
"""
Table creator
-----------
"""
