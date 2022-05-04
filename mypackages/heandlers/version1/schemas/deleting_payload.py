from pydantic import BaseModel, Extra

# The response schema doesn't necessary because we sent only a status


class DeletingPayloadRequestSchema(BaseModel, extra=Extra.allow):
    key: str
