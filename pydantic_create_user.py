from pydantic import BaseModel, Field, ConfigDict, EmailStr
from pydantic.alias_generators import to_camel

class UserSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name : str =Field(alias="firstName")
    middle_name : str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    user: UserSchema

