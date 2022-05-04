from pydantic import BaseModel, Extra

# The request schema doesn't necessary


class GettingStatisticResponseSchema(BaseModel):
    duplicates_percent: float
