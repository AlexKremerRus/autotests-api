
from pydantic import BaseModel, Field, ConfigDict

class GetExercisesQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias='courseId')

class ExerciseSchema(BaseModel):
    """
    Описание структуры.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    courseId: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int | None = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания.
    """
    model_config = ConfigDict(populate_by_name=True)

    exercise: ExerciseSchema

class GetExercisesResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    exercises: list[ExerciseSchema]

class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение задания..
    """
    model_config = ConfigDict(populate_by_name=True)

    exercise: ExerciseSchema

class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    exercise: ExerciseSchema

class CreateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int | None = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')

class UpdateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int | None = Field(alias='orderIndex')
    description: str | None
    estimated_time: str | None = Field(alias='estimatedTime')