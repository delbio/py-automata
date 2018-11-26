import unittest

from automaton.core.Action import Action

class TestActionMethods(unittest.TestCase):

    def test_constructor_nullOriginState_throwError(self):
        with self.assertRaises(ValueError):
            action = Action(None)

if __name__ == '__main__':
    unittest.main()