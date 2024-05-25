import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user_wrong

@pytest.mark.QaseIO(9)
def test():
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer c5c6e5d0d9f9c7d5535858c1840d4507f9a79801b315cb312cb32a7f10e7ccb4",
    }

    req = requests.get(api_user_wrong, headers=head)


    # VALIDATION
    status_code = req.status_code


    # ASSERT
    assert_that(status_code).is_equal_to(404)
