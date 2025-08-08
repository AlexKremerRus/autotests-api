from clients.courses.courses_client import get_courses_client, CreateCoursesRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExercisesRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthentificationUserSchema
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email= get_random_email(),
    password= "str",
    lastName= "str",
    firstName= "str",
    middleName= "str",
)

create_user_response = public_users_client.create_user(create_user_request)

authentification_user = AuthentificationUserSchema(
    email=create_user_request['email'],
    password=create_user_request['password']
)


files_client = get_files_client(authentification_user)
courses_client = get_courses_client(authentification_user)

create_file_request = CreateFileRequestDict(
    filename='image.png',
    directory='courses',
    upload_file='./testdata/files/image.png'
)

create_file_response = files_client.create_file(
    create_file_request
)
print(create_file_response)

create_course_request = CreateCoursesRequestDict(
    title='Python',
    maxScore=100,
    minScore=10,
    description="PS",
    estimatedTime="2 week",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)

create_course_response = courses_client.create_course(create_course_request)
print("---------")
print("---------")

print(create_course_response)

print("---------")

exercises_client = get_exercises_client(authentification_user)
exercises_client_request = CreateExercisesRequestDict(
    title= "test",
    courseId= create_course_response['course']['id'],
    maxScore=100,
    minScore=10,
    orderIndex=12,
    description="test test test",
    estimatedTime="1 week"
)


exercises_client_response = exercises_client.create_exercise(exercises_client_request)
print('%%%%%%%')
print(exercises_client_response)
