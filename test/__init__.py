import unittest2
import dot_prop
from functools import partial

testObject = {
  'foo': 'bar',
  'biz': 'booz',
  'nested': {
    'value': 'indeed'
  }
}

class DotPropsTest(unittest2.TestCase):
  def test_get(self):
    self.assertEqual(dot_prop.get(testObject, 'foo'), 'bar')
    self.assertEqual(dot_prop.get(testObject, 'nested.value'), 'indeed')

if __name__ == '__main__':
  unittest2.main()
