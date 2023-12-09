
import sqlite3

class database:
    def __init__(self):
        self.DBname = 'TokaFitness.db'

    def connect (self):
        conn = None
        try:
            conn = sqlite3.connect(self.DBname)
        except Exception as e:
            print(e)
        return conn

    def queryDB(self,command, params=[]):
        conn = self.connect()
        cur = conn.cursor() #creates new cursor object by executing SQL treatments
        cur.execute(command,params) #executes the update based on provided parameters

        #fetchall()- it fetches all the rows on a result set. If some rows have already been extracted 
        # form the result set, then it retrieves the remaining rows from the result set
        result = cur.fetchall()
        self.disconnect(conn)
        return result

    def updateDB(self,command, params=[]):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(command,params)


        conn.commit()
        result = cur.fetchall() # commits the transaction
        self.disconnect(conn) # gets all the results 
        return result 
    

    def toggle_tod_complete(self, Book_ID):
        conn = self.connect()
        cur = conn.cursor()

        cur.execute("SELECT complete FROM Book_tbl WHERE book_ID = ?", (book_ID))
        row = cur.fetchone()

        if row is not None:
            current_complete_status = row[0]
            new_complete_status = not current_complete_status

            cur.execute("UPDATE Books SET complete = ? WHERE book_ID = ?", (new_complete_status, Book_ID))
            conn.commit()
            
        def get_table_structure(self, table_name):
            conn = self.connect()
            cur = conn.cursor()
            cur.execute(f"PRAGMA table_info({table_name})"
            table_info = cur.fetchall()
            field_names = [info[1] for info in table_info]
            self.disconnect()
            return field_names
#################################################
#This closes the database
    def disconnect(self,conn):
        conn.close()
