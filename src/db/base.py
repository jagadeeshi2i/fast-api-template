from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base


class MixinToJson:
    def to_dict(self):
        """
        Converts the object to a dictionary representation.

        Returns:
            dict: A dictionary representation of the object.
        """
        row_dict = dict(self.__dict__)
        row_dict.pop("_sa_instance_state", None)
        return row_dict


Base = declarative_base(cls=(MixinToJson,))


class Crud:
    @classmethod
    async def create(cls, model, request, session: AsyncSession):
        """
        Creates a new record in the database for the given model.

        Args:
            cls (Type): The class of the model.
            model (Type[BaseModel]): The model to create a record for.
            request (BaseModel): The request object containing the data for the new record.
            session (AsyncSession): The database session.

        Returns:
            Any: The created record.
        """
        stmt = insert(model).values(**request.dict())
        result = await cls.execute(stmt, session)
        return result.scalar_one()

    @classmethod
    async def execute(cls, stmt, session: AsyncSession):
        """
        Executes the given statement using the provided session.

        Args:
            stmt: The statement to execute.
            session: The session to use for execution.

        Returns:
            The result of the execution.
        """
        return await session.execute(stmt)
