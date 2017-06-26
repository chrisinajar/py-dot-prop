import unittest2
from dot_props import dotProps
from functools import partial

testObject = {
  'foo': 'bar',
  'biz': 'booz',
  'nested': {
    'value': 'indeed'
  }
}

class DotPropsTest(unittest2.TestCase):
  def test_basic(self):
    self.assertEqual(dotProps(testObject, 'foo'), 'bar')
    self.assertEqual(dotProps(testObject, 'nested.value'), 'indeed')

if __name__ == '__main__':
  unittest2.main()
