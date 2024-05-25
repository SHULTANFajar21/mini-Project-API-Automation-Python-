import requests

from setting.endpoint import TOKEN_QASE_IO, PROJECT_CODE_QASE_IO, TEST_RUN_QASE_IO, api_result_qase_io


def update_test_result(test_case_id, test_status):
    head = {
        "accept": "application/json",
        "content-type": "application/json",
        "Token": TOKEN_QASE_IO
    }
    payload = {
        "case_id": test_case_id,
        "status": test_status
    }
    req = requests.post(f"{api_result_qase_io}/{PROJECT_CODE_QASE_IO}/{TEST_RUN_QASE_IO}", headers=head, json=payload)