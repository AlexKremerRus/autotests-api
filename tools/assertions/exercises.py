import allure

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExercisesRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, ExerciseSchema, UpdateExercisesRequestSchema, UpdateExerciseResponseSchema, \
    GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response

from tools.logger import get_logger  # Импортируем функцию для создания логгера

logger = get_logger("EXERCISES_ASSERTIONS")


@allure.step("Проверка ответа на создания задания")
def assert_create_exercise_response(
        request:CreateExercisesRequestSchema  ,
        response:CreateExerciseResponseSchema
):
    logger.info("Проверка ответа на создания задания")

    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")

    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")

@allure.step("Проверка задания")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные задания соответствуют ожидаемым.

    :param actual: Фактические данные задания.
    :param expected: Ожидаемые данные задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Проверка задания")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

@allure.step("Проверка ответа на получения задания")
def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema
):
    logger.info("Проверка ответа на получения задания")

    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)

@allure.step("Проверка ответа на обновления задания")
def assert_update_exercise_response(
        request: UpdateExercisesRequestSchema,
        response: UpdateExerciseResponseSchema
):
    logger.info("Проверка ответа на обновления задания")

    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")

@allure.step("Проверка ответа на не найденное задания")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    logger.info("Проверка ответа на не найденное задания")

    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)

@allure.step("Проверка ответа на получения заданий")
def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercise_responses: list[CreateExerciseResponseSchema]
):
    """
    Проверяет, что ответ на получение списка заданий соответствует ответам на их создание.

    :param get_exercises_response: Ответ API при запросе списка заданий.
    :param create_exercise_responses: Список API ответов при создании заданий.
    :raises AssertionError: Если данные заданий не совпадают.
    """
    logger.info("Проверка ответа на получения заданий")

    assert_length(get_exercises_response.exercises, create_exercise_responses, "exercises")

    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response.exercise)






