import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user
from faker import Faker
fake = Faker()

@pytest.mark.QaseIO(4)
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
         "status": ""
    }
    req = requests.post(api_user, headers=head, json=payload)



    # VALIDATION
    status_code = req.status_code
    res_field = req.json()[0]["field"]
    res_msg = req.json()[0]["message"]


    # ASSERT
    assert_that(status_code).is_equal_to(422)
    assert_that(res_field).is_equal_to("status")
    assert_that(res_msg).is_equal_to("can't be blank")
