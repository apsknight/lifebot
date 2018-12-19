import sqlite3

class Database:

    def __init__(self):
        '''
        Initialize database connection and create table if not exist
        '''
        self.con = sqlite3.connect('apscare.db')
        self.createTable()

    def __del__ (self):
        '''
        Destructor - Close Connections
        '''
        if self.con:
            self.con.close()

    def createTable(self):
        '''
        Create table for storing disease conditions
        '''
        try:
            cur = self.con.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS Treatments(Disease VARCHAR(50) PRIMARY KEY, Details VARCHAR(500),
                Selfcare VARCHAR(200), Medications VARCHAR(200), Specialists VARCHAR(200));
                            ''')

            self.con.commit()

        except Error as e:
            if self.con:
                self.con.rollback()
            
    def insert(self, disease, details, selfcare, medications, specialists):
        '''
        Insert condition row in table.
        '''
        try:
            cur = self.con.cursor()
            cur.execute("INSERT INTO Treatments VALUES(?,?,?,?,?);", (
                    disease, details, selfcare, medications, specialists, ))
            self.con.commit()

        except Error as e:
            if self.con:
                self.con.rollback()
    
    def search(self, disease):
        '''
        Return disease's conditions.
        If not found - return None 
        '''
        cur = self.con.cursor()
        cur.execute("SELECT * FROM Treatments WHERE Disease = ?;", (disease,))
        data = cur.fetchone()
        if not data:
            return None
        result = {
            "disease": data[0],
            "details": data[1],
            "selfcare": data[2],
            "medications": data[3],
            "specialists": data[4]
            }

        return result