import allure

from clients.courses.courses_schema import CourseSchema, UpdateCoursesRequestSchema, UpdateCourseResponseSchema, \
    GetCoursesResponseSchema, CreateResponseSchema, CreateCoursesRequestSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user
from tools.logger import get_logger  # Импортируем функцию для создания логгера

logger = get_logger("COURSES_ASSERTIONS")

@allure.step("Проверка ответа обновления курса")
def assert_update_course_response(
        request: UpdateCoursesRequestSchema,
        response: UpdateCourseResponseSchema):
    logger.info("Проверка ответа обновления курса")
    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")

@allure.step("Проверка курса")
def assert_course(actual: CourseSchema, expected: CourseSchema):
    logger.info("Проверка курса")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)

@allure.step("Проверка ответа на получения курса")
def assert_get_courses_response(
        get_course_response: GetCoursesResponseSchema,
        create_course_response: list[CreateResponseSchema]
):
    logger.info("Проверка ответа на получения курса")

    assert_length(get_course_response.courses, create_course_response, "courses")

    for index, create_course_response in enumerate(create_course_response):
        assert_course(get_course_response.courses[index], create_course_response.course)

@allure.step("Проверка ответа на создание курса")
def assert_create_course_response(
        request: CreateCoursesRequestSchema,
        response: CreateResponseSchema
):
    logger.info("Проверка ответа на создание курса")

    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")

    assert_equal(response.course.preview_file.id, request.preview_file, "preview_file_id")
    assert_equal(response.course.created_by_user.id, request.created_by_user, "created_by_user_id")



