# =========================================== HOST ===========================================
import os

host_gorest = "https://gorest.co.in/public/v2"
host_qase_io = "https://api.qase.io/v1"

# =========================================== ENDPOINT ===========================================
api_user = host_gorest + "/users"
api_user_wrong = host_gorest + "/usersss"
api_result_qase_io = host_qase_io + "/result"
# =========================================== CONFIG ===========================================
TOKEN_QASE_IO = os.environ.get('QASE_IO_TOKEN')
PROJECT_CODE_QASE_IO = "MPAAP"
TEST_RUN_QASE_IO = "1"
# =========================================== SLACK ===========================================
WEBHOOK = os.environ.get('WEBHOOOK_SLACK')