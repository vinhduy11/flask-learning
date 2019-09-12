from config import server_config
from libs.logger import logger
from ldap3 import Connection, Server, SUBTREE
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
            logger.error('[{}][{}]{}'.format(LDAP.__name__, self.__create_connection.__name__, e))
    
    def authen(self, username, password):
        try:
            user_dn = "cn={},dc=mservice,dc=org".format(username)
            base_dn = "dc=mservice,dc=org"
            server = Server(self.LDAP_SERVER, port=self.LDAP_PORT, use_ssl=False)
            self.connect = Connection(server, user='{}@mservice.org'.format(username), password=password, authentication='SIMPLE')
            logger.debug('[{}][{}]{}'.format(LDAP.__name__, self.authen.__name__, self.connect.bind()))
            if self.connect.bind():
                logger.debug('[{}][{}]{}'.format(LDAP.__name__, self.authen.__name__, 'Connection Bind Complete!'))
                return True
            else:
                logger.debug('[{}][{}]{}'.format(LDAP.__name__, self.authen.__name__, self.connect.result))
                return False
        except Exception as e:
            logger.error('[{}][{}]{}'.format(LDAP.__name__, self.authen.__name__, e))