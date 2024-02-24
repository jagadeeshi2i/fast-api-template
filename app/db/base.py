from sqlalchemy import and_, delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base


class MixinToJson:
    def to_dict(self):
        row_dict = dict(self.__dict__)
        row_dict.pop('_sa_instance_state', None)
        return row_dict


Base = declarative_base(cls=(MixinToJson,))


class Crud:
    @classmethod
    async def create(cls, model, request, session: AsyncSession):
        stmt = insert(model).values(**request.dict())
        result = await cls.execute(stmt, session)
        return result.scalar_one()

    @classmethod
    async def execute(cls, stmt, session: AsyncSession):
        return await session.execute(stmt)
 