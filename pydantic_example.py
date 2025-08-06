from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    # address:Address
    is_active: bool=Field(alias='isActive')

user_data = {
    'id':'3',
    'name':'Penis',
    'email':'test@tets.test',
    'isActive':True
}

# user = User(id=1,name='tet', email='fff', address={"city":"Moscow", "zip_code":"123456"}, isActive=True)

# user2 = User(id=2,name='test', email='dddd', address=Address(city="LA", zip_code="123321"), isActive=False)

user3 = User(**user_data)

print(user3)

