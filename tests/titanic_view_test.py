import unittest

from lecture.titanic import views

class TitanicViewTest(unittest.TestCase):
    mock = views()

    def test_modeling(self):
        self.mock.modeling()

if __name__ == '__main__':
    unittest.main()