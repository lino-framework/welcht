from lino.utils.pythontest import TestCase


class TestCase(TestCase):

    def test_mathieu(self):
        self.run_django_manage_test('lino_welcht/demo')
