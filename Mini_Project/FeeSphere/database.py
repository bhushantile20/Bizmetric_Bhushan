import mysql.connector
from mysql.connector import Error
from config import connection

class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def connect(self):
        """connect to database"""
        try:
            self.connection = mysql.connector.connect(**connection)
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("mysql connected successfully")
                return True
        except Error as e:
            print(f"mysql error: {e}")
            return False
    
    def create_table(self):
        """create courses table if not exists"""
        try:
            courses = [
                ('HR', True),
                ('FINANCE', True), 
                ('MARKETING', True),
                ('DS', False)
            ]
            
            self.cursor.executemany(
                "insert into  courses (subject, has_analytics) values(%s, %s)",
                courses
            )
            self.connection.commit()
            print("table setup complete!")
        except Error as e:
            print(f"Table Error: {e}")
    
    def get_courses(self):
        """Get all available courses"""
        try:
            self.cursor.execute("select  subject, has_analytics FROM courses")
            return self.cursor.fetchall()
        except Error as e:
            print(f"query Error: {e}")
            return []
    
    def close(self):
        """close database connection"""
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("connection closed ")
