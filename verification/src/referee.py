from checkio_referee import RefereeCodeGolf
from checkio_referee.covercode import py_2_str

import settings
import settings_env
from tests import TESTS



class Referee(RefereeCodeGolf):
    DEFAULT_LENGTH = 150
    BASE_POINTS = 15
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "golf"
    ENV_COVERCODE = {
        "python_2": py_2_str,
        "python_3": None,
        "javascript": None
    }
