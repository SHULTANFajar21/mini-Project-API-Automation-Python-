import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user

@pytest.mark.QaseIO(11)
def test():
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer c5c6e5d0d9f9c7d5535858c1840d4507f9a79801b315cb312cb32a7f10e7ccb4",
    }

    req = requests.post(api_user, headers=head)


    # VALIDATION
    status_code = req.status_code
    description = req.json()[0]["message"]


    # ASSERT
    assert_that(status_code).is_equal_to(422)
    assert_that(description).is_equal_to("can't be blank")
