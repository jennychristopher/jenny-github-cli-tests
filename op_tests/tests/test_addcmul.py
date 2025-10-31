import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../addcmul_math_op/math_ops"))

from addcmul import addcmul


def test_addcmul_basic():
    assert addcmul(1,2,3) == 7

