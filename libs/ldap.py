from config import server_config
from libs.logger import logger
from ldap3 import Connection
class LDAP():
    def __init__(self):
        self.LDAP_SERVER = server_config.LDAP_SERVER
        self.LDAP_PORT = server_config.LDAP_PORT
        self.LDAP_USER = server_config.LDAP_USER
        self.LDAP_PASS = server_config.LDAP_PASS
        self.LDAP_TLS = server_config.LDAP_TLS
        self.connect = None
        self.__create_connection()
    
    def __create_connection(self):
        try:
            self.connect = Connection(self.LDAP_SERVER, user='cn={user},dc=mservice,dc=org'.format(user=self.LDAP_USER), password=self.LDAP_PASS)
        except Exception as e:
            logger.error(f"LDAP Error {e}")
    
    def authen(self, username, password):
        try:
            self.connect = Connection(self.LDAP_SERVER, user='cn={user},dc=mservice,dc=org'.format(user=username), password=password)
            if self.connect:
                return True
            else:
                return False
        except Exception as e:
            logger.error(f"LDAP Error {e}")
            return False