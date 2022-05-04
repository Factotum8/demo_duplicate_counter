from pydantic import BaseModel, Extra


class AddingPayloadRequestSchema(BaseModel, extra=Extra.allow):
    """
    Contract doesn't exist yet
    """


class AddingPayloadResponseSchema(BaseModel):
    key: str
