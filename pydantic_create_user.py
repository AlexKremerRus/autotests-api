from pydantic import BaseModel, Field, ConfigDict, HttpUrl, EmailStr

class UserBasic(BaseModel):
    """
    Основа структуры данных для пользователя
    """
    email: EmailStr
    last_name:str = Field(alias="lastName", default='last')
    first_name: str = Field(alias="firstName", default='first')
    middle_name: str = Field(alias="middleName", default='middle')

class UserSchema(UserBasic):
    """
    Структура данных для пользователя
    """
    id: str


class CreateUserRequestSchema(UserBasic):
    """
    Структура данных для запроса на создание пользователя
    """
    password: str


class CreateUserResponseSchema(BaseModel):
    """
    Структура данных для ответа на создание пользователя
    """
    user: UserSchema

user = UserSchema(id="course_id", email="test@tet.re")

print(user)