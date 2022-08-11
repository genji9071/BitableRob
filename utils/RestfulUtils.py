from typing import Dict, Any

import requests
from pydantic import BaseModel

from lark.Auth import get_tenant_access_token
from utils.ErrorUtils import build_error


def do_post(url: str, body: Dict[str, Any] = None, header: Dict[str, Any] = None) -> Dict[str, Any]:
    response = requests.post(url, data=body, headers=header)
    if response.status_code != 200:
        raise build_error("do_post failed!", url=url, status_code=response.status_code, result=response.json())
    return response.json()


def do_get(url: str, params: Dict[str, Any] = None, header: Dict[str, Any] = None) -> Dict[str, Any]:
    response = requests.get(url, params=params, headers={"Authorization":get_tenant_access_token(), **header})
    if response.status_code != 200:
        raise build_error("do_get failed!", url=url, status_code=response.status_code, result=response.json())
    return response.json()
