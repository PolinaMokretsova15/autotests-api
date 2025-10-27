from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise(TypedDict):
    """
    Описывает структуру объекта задания (exercise)
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class CourseIdParams(TypedDict):
    """
    Query-параметр для получения списка заданий по курсу
    """
    courseId: str

class CreateExercisesRequestDict(TypedDict):
    """
    Тело запроса для создания задания POST /api/v1/exercises
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesResponseDict(TypedDict):
    """
    Ответ от GET /api/v1/exercises
    """
    exercises: list[Exercise]

class GetExerciseResponseDict(TypedDict):
    """
    Ответ от GET /api/v1/exercises/{exercise_id}
    и POST /api/v1/exercises
    """
    exercise : Exercise

class UpdateExercisesRequestDict(TypedDict):
    """
    Тело запроса для обновления задания PATCH /api/v1/exercises/{exercise_id}
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с ресурсом /api/v1/exercises
    """
    def get_exercises_api(self, query: CourseIdParams)-> Response:
        """
        GET /api/v1/exercises — получение списка заданий для определенного курса.

        Args:
          Query: Словарь с query-параметрами. Обязательное поле: courseId.

          Returns:
                Response: HTTP-ответ сервера (список заданий в теле ответа).
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str)-> Response:
        """
        GET /api/v1/exercises/{exercise_id} — получение информации о задании.

        Args:
            exercise_id: Идентификатор задания.

        Returns:
            Response: HTTP-ответ сервера (данные задания в теле ответа).
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExercisesRequestDict)-> Response:
        """
        POST /api/v1/exercises — создание задания.

        Args:
            request: Тело запроса для создания задания.

        Returns:
            Response: HTTP-ответ сервера (созданное задание в теле ответа).
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, request: UpdateExercisesRequestDict, exercise_id: str)-> Response:
        """
        PATCH /api/v1/exercises/{exercise_id} — частичное обновление задания.

        Args:
            exercise_id: Идентификатор задания.
            request: Тело запроса с изменяемыми полями (любые из допустимых).

        Returns:
            Response: HTTP-ответ сервера (обновлённое задание в теле ответа).
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str)-> Response:
        """
        DELETE /api/v1/exercises/{exercise_id} — удаление задания.

        Args:
            exercise_id: Идентификатор задания.

        Returns:
            Response: HTTP-ответ сервера (обычно без тела или с минимальной служебной информацией).
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict :
        """
        Возвращает одно задание по идентификатору.
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query: CourseIdParams) -> GetExercisesResponseDict:
        """
        Возвращает список заданий для указанного курса.
        """
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(self, request: CreateExercisesRequestDict) -> GetExerciseResponseDict:
        """
        Создаёт новое задание и возвращает созданный объект.
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, request: UpdateExercisesRequestDict, exercise_id: str) -> GetExerciseResponseDict:
        """
        Обновляет задание по идентификатору и возвращает обновлённый объект.
        """
        response = self.update_exercise_api(request, exercise_id)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient :
    """
    Билдер для ExercisesClient.
    Все методы требуют авторизации.
    """
    return ExercisesClient(client=get_private_http_client(user))