from typing import Optional

from peewee import fn

from mypackages.heandlers.version1.schemas.getting_statistic import GettingStatisticResponseSchema
from mypackages.peewee_models import Payloads
from mypackages.heandlers.version1.abstract_handler import AppHandler


class GettingStatisticHandler(AppHandler):

    async def calculate_duplicates_percent(self, unique: Optional[int], duplicate: Optional[int]) -> float:
        if unique is None or duplicate is None:
            return 0.0
        return 100 * duplicate / unique

    async def get(self):
        sql_sum = fn.SUM(Payloads.duplicate_count)

        duplicate = Payloads.select(sql_sum).scalar()
        unique = Payloads.select().count()

        p = round(await self.calculate_duplicates_percent(unique, duplicate), 2)
        response = GettingStatisticResponseSchema(duplicates_percent=p)
        return self.write(response.json())
