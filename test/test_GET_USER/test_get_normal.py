import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user

@pytest.mark.QaseIO(10)
def test():
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer c5c6e5d0d9f9c7d5535858c1840d4507f9a79801b315cb312cb32a7f10e7ccb4",
    }

    req = requests.get(api_user, headers=head)


    # VALIDATION
    status_code = req.status_code
    resp_id = req.json()[0]["id"]
    resp_name = req.json()[0]["name"]
    resp_email = req.json()[0]["email"]
    resp_gender = req.json()[0]["gender"]
    resp_status = req.json()[0]["status"]

    # ASSERT
    assert_that(status_code).is_equal_to(200)
    assert_that(resp_id).is_not_none()
    assert_that(resp_name).is_not_none()
    assert_that(resp_email).is_not_none()
    assert_that(resp_gender).is_not_none()
    assert_that(resp_status).is_not_none()
    assert_that(resp_id).is_type_of(int)
    assert_that(resp_email).contains("@")
    assert_that(resp_gender).is_in("male", "female")
    assert_that(resp_status).is_in("active", "inactive")