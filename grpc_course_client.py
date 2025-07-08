import grpc

import course_service_pb2
import course_service_pb2_grpc

# Устанавливаем соединение с сервером
channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)

# Отправляем запрос
response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id="12"))
print(response.course_id)
print(f"Course name: {response.title}")
print(f"Description: {response.description}")