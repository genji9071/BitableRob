from pydantic import BaseModel


class LarkBitableRecordItem(BaseModel):
    id: str
    record_id: str
    fields: dict
