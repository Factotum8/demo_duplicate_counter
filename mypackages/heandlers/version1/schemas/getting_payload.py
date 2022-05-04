from pydantic import BaseModel, Extra


class GettingPayloadRequestSchema(BaseModel, extra=Extra.allow):
    """
    Contract doesn't exist yet
    """


class AddingPayloadResponseSchema(BaseModel):
    key: str
