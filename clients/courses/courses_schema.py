from pydantic import BaseModel, Field, ConfigDict

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class CourseSchema(BaseModel):
    """
    Схема курса, возвращаемая API
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")

class ParamsSchema(BaseModel):
    """
    Параметры фильтрации курсов при запросе списка
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")

class CreateCourseRequestSchema(BaseModel):
    """
    Схема тела запроса для создания нового курса
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")

class CreateCourseResponseSchema(BaseModel):
    """
    Схема ответа при успешном создании курса
    """
    course: CourseSchema

class UpdateCourseRequestSchema(BaseModel):
    """
    Схема тела запроса для обновления (PATCH) данных курса
    """
    model_config = ConfigDict(populate_by_name=True)
    # для патч актуально опционально
    title: str | None
    maxScore: int | None = Field(alias="maxScore")
    minScore: int | None = Field(alias="minScore")
    description: str | None
    estimatedTime: str | None = Field(alias="estimatedTime")