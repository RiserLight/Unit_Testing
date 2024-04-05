import pytest
from my_app.sample import add

def test_add_num():
  assert add(2,3)==5

def test_add_str():
  assert add("ra","hul")=="rahul"

class Test:
  
  def setup_method(self,method):
    print(f'Setup {method}')

  def teardown_method(self,method):
    print(f'teardown {method}')
    
  def test_add_num(self):
    assert add(2,3)==5

  def test_add_str(self):
    assert add("ra","hul")=="rahul"