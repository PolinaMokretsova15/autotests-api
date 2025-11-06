from pydantic import BaseModel, Field, ConfigDict

class ExerciseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """
    Описывает структуру объекта задания (exercise)
    """
    id: str
    title: str
    courseId: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class CourseIdParamsSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """
    Query-параметр для получения списка заданий по курсу
    """
    course_id: str = Field(alias="courseId")

class CreateExercisesRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """
    Тело запроса для создания задания POST /api/v1/exercises
    """
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    course_id: str = Field(alias="courseId")

class GetExercisesResponseSchema(BaseModel):
    """
    Ответ от GET /api/v1/exercises
    """
    exercises: list[ExerciseSchema]

class GetExerciseResponseSchema(BaseModel):
    """
    Ответ от GET /api/v1/exercises/{exercise_id}
    и POST /api/v1/exercises
    """
    exercise : ExerciseSchema

class UpdateExercisesRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """
    Тело запроса для обновления задания PATCH /api/v1/exercises/{exercise_id}
    """
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")