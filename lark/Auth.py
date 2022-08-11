import json
from typing import Optional

from lark import base_url, url_get_tenant_access_token
from utils.RestfulUtils import do_post
from vo.lark.LarkAuthTenantAccessTokenResponse import LarkAuthTenantAccessTokenResponse


class Auth:
    __instance__ = None
    __tenant_access_token__: Optional[str] = None
    __app_id__: Optional[str] = None
    __app_secret__: Optional[str] = None

    def __new__(cls, *args, **kwargs):
        if not Auth.__instance__:
            Auth.__instance__ = object.__new__(cls)
        return Auth.__instance__

    def get_tenant_access_token(self, refresh=False):
        if not Auth.__tenant_access_token__ or refresh:
            Auth.__app_id__, Auth.__app_secret__ = self.__loadProps__()
            Auth.__tenant_access_token__ = self.__get_tenant_access_token__(Auth.__app_id__,
                                                                            Auth.__app_secret__).tenant_access_token
        return Auth.__tenant_access_token__

    def __get_tenant_access_token__(self, app_id: str, app_secret: str) -> LarkAuthTenantAccessTokenResponse:
        return LarkAuthTenantAccessTokenResponse(
            **do_post(base_url + url_get_tenant_access_token, {"app_id": app_id, "app_secret": app_secret}))

    def __loadProps__(self):
        with open("config.json", 'r') as load_f:
            result = json.load(load_f)
            return result['app_id'], result['app_secret']
