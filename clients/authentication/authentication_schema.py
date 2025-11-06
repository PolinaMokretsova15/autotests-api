from pydantic import BaseModel, Field
from pydantic.alias_generators import to_camel

class TokenSchema(BaseModel):
    """
    Описание структуры аутентификационных токенов.
    """
    token_type: str = Field(alias="tokenType")
    access_token: str =Field(alias="accessToken")
    refresh_token: str =Field(alias="refreshToken")


class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str

class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа аутентификации.
    """
    token: TokenSchema

class RefreshTokenSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str =Field(alias="refreshToken")

