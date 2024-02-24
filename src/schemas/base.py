from pydantic import BaseModel, ConfigDict


class PydanticBaseModel(BaseModel):
    model_config: ConfigDict = {"from_attributes": True}
