from http import HTTPStatus

import allure
import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCoursesRequestSchema, UpdateCourseResponseSchema, \
    GetCoursesQuerySchema, GetCoursesResponseSchema, CreateCoursesRequestSchema, CreateResponseSchema
from fixtures.courses import CourseFixture
from fixtures.file import FileFixture
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_get_courses_response, \
    assert_create_course_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    @allure.title("Создание курса ")
    def test_create_course(self,
                           courses_client: CoursesClient,
                           function_file: FileFixture,
                           function_user: UserFixture
                           ):
        request = CreateCoursesRequestSchema(
            previewFileId=function_file.response.file.id,
            createdByUserId=function_user.response.user.id
        )
        response = courses_client.create_courses_api(request)
        response_data = CreateResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_course_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Получение курса")
    def test_get_courses(self,
                         courses_client: CoursesClient,
                         function_user: UserFixture,
                         function_course: CourseFixture):
        query= GetCoursesQuerySchema(user_id=function_user.response.user.id)
        response = courses_client.get_courses_api(query)

        response_data = GetCoursesResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_course.response])
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Обновление курса")
    def test_update_course(self,
                           courses_client: CoursesClient,
                           function_course: CourseFixture):
        request = UpdateCoursesRequestSchema()
        response = courses_client.update_course_api(function_course.response.course.id, request)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
