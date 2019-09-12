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
    
    def authen(self, username, password):
        self.connect = None
        try:
            
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
        finally:
            if self.connect.bind():
                self.connect.unbind()