from faker import Faker
import json
fake = Faker()
fake_user = {}

def create_users():
	for i in range(10):
		fake_user[i] = [fake.email(), fake.name(), fake.password()]
	return fake_user


print create_users()