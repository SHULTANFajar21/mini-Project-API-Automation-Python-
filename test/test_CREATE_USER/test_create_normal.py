import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user
from faker import Faker
fake = Faker()

@pytest.mark.QaseIO(7)
def test():
    random_name = fake.name()
    random_email = fake.email()
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer c5c6e5d0d9f9c7d5535858c1840d4507f9a79801b315cb312cb32a7f10e7ccb4",
    }
    payload = {
         "name": random_name,
         "email": random_email,
         "gender": "male",
         "status": "active"
    }
    req = requests.post(api_user, headers=head, json=payload)



    # VALIDATION
    status_code = req.status_code
    resp_name = req.json().get("name")
    resp_email = req.json().get("email")


    # ASSERT
    assert_that(status_code).is_equal_to(201)
    assert_that(resp_name).is_equal_to(random_name)
    assert_that(resp_email).is_equal_to(random_email)