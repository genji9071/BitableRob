from typing import List

from pydantic import BaseModel

from vo.lark.LarkBitableRecordItem import LarkBitableRecordItem


class LarkBitableGetRecordsResponse(BaseModel):
    items: List[LarkBitableRecordItem]
    page_token: str
    has_more: bool
    total: int
