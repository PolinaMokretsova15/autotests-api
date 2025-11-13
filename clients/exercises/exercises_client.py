from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.exercises.exercises_schema import CourseIdParamsSchema, CreateExercisesRequestSchema, UpdateExercisesRequestSchema, GetExerciseResponseSchema, GetExercisesResponseSchema

class ExercisesClient(APIClient):
    """
    Клиент для работы с ресурсом /api/v1/exercises
    """
    def get_exercises_api(self, query: CourseIdParamsSchema)-> Response:
        """
        GET /api/v1/exercises — получение списка заданий для определенного курса.

        Args:
          Query: Словарь с query-параметрами. Обязательное поле: courseId.

          Returns:
                Response: HTTP-ответ сервера (список заданий в теле ответа).
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str)-> Response:
        """
        GET /api/v1/exercises/{exercise_id} — получение информации о задании.

        Args:
            exercise_id: Идентификатор задания.

        Returns:
            Response: HTTP-ответ сервера (данные задания в теле ответа).
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExercisesRequestSchema)-> Response:
        """
        POST /api/v1/exercises — создание задания.

        Args:
            request: Тело запроса для создания задания.

        Returns:
            Response: HTTP-ответ сервера (созданное задание в теле ответа).
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, request: UpdateExercisesRequestSchema, exercise_id: str)-> Response:
        """
        PATCH /api/v1/exercises/{exercise_id} — частичное обновление задания.

        Args:
            exercise_id: Идентификатор задания.
            request: Тело запроса с изменяемыми полями (любые из допустимых).

        Returns:
            Response: HTTP-ответ сервера (обновлённое задание в теле ответа).
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str)-> Response:
        """
        DELETE /api/v1/exercises/{exercise_id} — удаление задания.

        Args:
            exercise_id: Идентификатор задания.

        Returns:
            Response: HTTP-ответ сервера (обычно без тела или с минимальной служебной информацией).
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema :
        """
        Возвращает одно задание по идентификатору.
        """
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query: CourseIdParamsSchema) -> GetExercisesResponseSchema:
        """
        Возвращает список заданий для указанного курса.
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExercisesRequestSchema) -> GetExerciseResponseSchema:
        """
        Создаёт новое задание и возвращает созданный объект.
        """
        response = self.create_exercise_api(request)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, request: UpdateExercisesRequestSchema, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Обновляет задание по идентификатору и возвращает обновлённый объект.
        """
        response = self.update_exercise_api(request, exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient :
    """
    Билдер для ExercisesClient.
    Все методы требуют авторизации.
    """
    return ExercisesClient(client=get_private_http_client(user))