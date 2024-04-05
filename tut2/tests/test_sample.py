import pytest
from myapp.sample import validate_age 

def test_validate_age_exception():
  with pytest.raises(ValueError,match='Age cannot be less than 0'):
    validate_age(-2)

def test_validate_age():
  assert validate_age(12)==12