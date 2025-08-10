from faker import Faker

fake = Faker('ru_RU')

print(fake.email())
print(fake.password())

print(fake.name())
print(fake.address() )


