import pytest
import time
from TestCases.test_login import TestLogin
from TestCases.test_invest import TestInvest
from Common.global_path import report_path

now = time.strftime('%Y-%m-%d_%H_%M_%S')
filePath = report_path + "Result" + now + ".html"

pytest.main(['-m','smoke','--html',filePath])