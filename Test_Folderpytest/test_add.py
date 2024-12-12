import pytest
import allure
from add import add
# Parametrize with one simple test case
@pytest.mark.parametrize(
    "a, b, expected",  # Parameters that will be passed to the test function
    [(2, 3, 5)]         # Single test case: (a=2, b=3) -> expected=5
)
@allure.feature("Addition Test")
@allure.story("Simple addition test")
@allure.title("Test adding two numbers")
def test_add(a, b, expected):
   # result = a + b  # Perform addition
    result = a + b  # Perform addition
    print(f"Adding {a} + {b} = {result}, Expected: {expected}")
