from config import server_config 
from libs.logger import logger
import MySQLdb
from MySQLdb import Error

class MySQL():
    def __init__(self):
        self.DB_HOST = server_config.DB_HOST
        self.DB_PORT = server_config.DB_PORT
        self.DB_USER = server_config.DB_USER
        self.DB_PASS = server_config.DB_PASS
        self.DB_DATABASE = server_config.DB_DATABASE
        self.connection = None

    def __create_connection(self):
        dbconfig = {
            
        }
        try:
            cnx = MySQLdb.connect(
                host=self.DB_HOST,
                db= self.DB_DATABASE,
                user=     self.DB_USER,
                passwd= self.DB_PASS
            )
            if cnx:
                self.connection = cnx
        except Exception as e:
            logger.error(f"{e}")
        except Error as e:
            logger.error(f"MySQL Error: {e}")
    
    def select_data(self, query_string, params, fetch):
        
        if self.connection is None:
            self.__create_connection()
        
        try:
            cursor = self.connection.cursor()
            if fetch == 'one':
                cursor.execute(query_string, params)
                return cursor.fetchone()
            elif fetch == 'many':
                cursor.execute(query_string, params)
                return cursor.fetchone()
            elif fetch == 'all':
                cursor.execute(query_string, params)
                return cursor.fetchall()
                
        except Exception as e:
            logger.error(f"{e}")
        except Error as e:
            logger.error(f"MySQL Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if self.connection:
                self.connection.close()
