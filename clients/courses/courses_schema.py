

from pydantic import BaseModel, Field, ConfigDict


from clients.users.users_schema import UserSchema
from clients.files.files_schema import FileSchema


class CourseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: str
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    description: str
    preview_file: FileSchema = Field(alias='previewFile')
    estimated_time: str = Field(alias='estimatedTime')
    created_by_user: UserSchema = Field(alias='createdByUser')

class CreateResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    course: CourseSchema

class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias='userId')

class CreateCoursesRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    description: str
    estimated_time: str | None = Field(alias='estimatedTime')
    preview_file: str = Field(alias='previewFileId')
    created_by_user: str = Field(alias='createdByUserId')

class UpdateCoursesRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    description: str | None
    estimated_time: str | None = Field(alias='estimatedTime')
