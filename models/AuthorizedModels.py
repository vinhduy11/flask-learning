from libs.ldap import LDAP
from libs.mysql import MySQL
from libs.logger import logger
class AuthorizedModels():
    def __init__(self):
        self.params = {}
        self.user_info = {
            "username": None,
            "fullname": None,
            "last_logged_in": None,
            "roles": None,
            "modules_permit_access": None
        }
        self.result = {
            "status": False,
            "code": -1,
            "msg": None
        }

    def user_authen_process(self, params):
        self.params = params
        result = self.__login_by_ldap()
        if result is True:
            res = {"status": True, "code": 0, "msg": ""}
        else:
            res = {"status": False, "code": -1, "msg": ""}
        
        self.result.update(res)
        return self.result

    def __login_by_ldap(self):
        try:
            result = LDAP().authen(self.params['username'], self.params['password'])
            if result is True:
                self.user_info.update({'username': self.params['username']})
                return True
        except Exception as e:
            logger.error(f'Authen Error {e}')
            return False
    
    def __get_roles(self):
        pass

    def __get_modules_permit_access(self):
        pass
