from pydantic import BaseModel, Extra


class PuttingPayloadRequestSchema(BaseModel, extra=Extra.allow):
    """
    Contract doesn't exist yet
    """


class PuttingPayloadResponseSchema(BaseModel):
    key: str
