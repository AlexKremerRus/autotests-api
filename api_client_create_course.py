from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCoursesRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthentificationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email= get_random_email(),
    password= "str",
    last_name= "str",
    first_name= "str",
    middle_name= "str",
)

create_user_response = public_users_client.create_user(create_user_request)

authentification_user = AuthentificationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(authentification_user)
courses_client = get_courses_client(authentification_user)

create_file_request = CreateFileRequestSchema(
    filename='image.png',
    directory='courses',
    upload_file='./testdata/files/image.png'
)

create_file_response = files_client.create_file(
    create_file_request
)
print(create_file_response)

create_course_request = CreateCoursesRequestSchema(
    title='Python',
    maxScore=100,
    minScore=10,
    description="PS",
    estimatedTime="2 week",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)

create_course_response = courses_client.create_course(create_course_request)
print(create_course_response)



