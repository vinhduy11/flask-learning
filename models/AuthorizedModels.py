from flask import session
from libs.ldap import LDAP
from libs.mysql import MySQL
from libs.logger import logger
import time
class AuthorizedModels():
    def __init__(self):
        self.params = {}
        
        self.result = {
            "status": False,
            "code": -1,
            "msg": None
        }

    def user_authen_process(self, params):
        self.params = params
        
        user_result = self.__check_existed()
        if user_result:
            ldap_result = self.__login_by_ldap()
            if ldap_result:
                res = {"status": True, "code": 0, "msg": ""}
                user = {
                    "username": user_result[0],
                    "fullname": user_result[1],
                    "last_logged_in": int(time.time()),
                    "roles": user_result[2],
                    "modules_permit_access": None
                }
                for (key, val) in user.items():
                    session[key] = val
                
            else:
                res = {"status": False, "code": -1, "msg": "Login error! Please check Username and password."}
        else:
            res = {"status": False, "code": -1, "msg": "No user found!"}
        
        self.result.update(res)
        return self.result

    def __check_existed(self):
        try:
            query_string =  "select pua.username, pua.fullname, purm.role_id "\
                            "from per_user_account pua " \
                            "join per_user_role_map purm on pua.username = purm.username " \
                            "where pua.username = '{param1}' and account_status = 1 ".format(param1 = self.params['username'])
            res = MySQL().select(query_string=query_string, fetch='one')
            logger.debug('[{}][{}]{}'.format(AuthorizedModels.__name__, self.__check_existed.__name__, res))
            if res:
                return res
        except Exception as e:
            logger.error('[{}][{}]{}'.format(AuthorizedModels.__name__, self.__check_existed.__name__, e))
            return False

    def __login_by_ldap(self):
        try:
            result = LDAP().authen(self.params['username'], self.params['password'])
            logger.debug('[{}][{}]{}'.format(AuthorizedModels.__name__, self.__login_by_ldap.__name__, result))
            if result:
                return True
        except Exception as e:
            logger.error('[{}][{}]{}'.format(AuthorizedModels.__name__, self.__login_by_ldap.__name__, e))
            return False
