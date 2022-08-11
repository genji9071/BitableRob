import inspect
from typing import List

from lark import base_url, url_get_records
from lark.Auth import Auth
from utils.RestfulUtils import do_get
from vo.lark.LarkBaseResponse import LarkBaseResponse
from vo.lark.LarkBitableGetRecordsResponse import LarkBitableGetRecordsResponse


def get_records(app_token: str,
                table_id: str,
                view_id: str = None,
                filter: str = None,
                sort: List[str] = None,
                field_names: List[str] = None,
                text_field_as_array: str = None,
                page_token: str = None,
                page_size: str = None,
                user_id_type: str = None
                ) -> LarkBaseResponse[LarkBitableGetRecordsResponse]:
    frame = inspect.currentframe()
    args, _, _, values = inspect.getargvalues(frame)
    kwargs = {}
    for i in args:
        if values[i] is not None:
            kwargs[i] = values[i]
    return __get_records__(**kwargs)


def __get_records__(app_token: str,
                    table_id: str,
                    **kwargs
                    ) -> LarkBaseResponse[LarkBitableGetRecordsResponse]:
    url = base_url + url_get_records.replace(":app_token", app_token).replace(":table_id", table_id)
    return LarkBaseResponse[LarkBitableGetRecordsResponse](**do_get(url, params=kwargs))

if __name__ == '__main__':
    get_records('1','2', field_names=['a','b'])