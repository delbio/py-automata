import unittest

from fsm.core import action as _act

class TestActionMethods(unittest.TestCase):

    def test_constructor_nullOriginState_throwError(self):
        with self.assertRaises(ValueError):
            action = _act.Action(None)

if __name__ == '__main__':
    unittest.main()
