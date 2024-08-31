import sys


if sys.version_info >= (3, 11):
    from src.stepping311 import get_stepping_variants
else:
    from src.stepping27 import get_stepping_variants
