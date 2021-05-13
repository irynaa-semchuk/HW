import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_0 = Employee('Ira', 'Stan', 1109)
        self.emp_1 = Employee('Saral', 'Gyaan', 1111)
        self.emp_2 = Employee('Udit', 'Vashisht', 1200)

    def test_email(self):
        self.assertEqual(self.emp_0.email, 'Ira.Stan@email.com')

        self.assertEqual(self.emp_1.email, 'Saral.Gyaan@email.com')
        self.assertEqual(self.emp_2.email, 'Udit.Vashisht@email.com')

        self.emp_1.first = "Sara"
        self.emp_2.first = "Solomiay"

        self.assertEqual(self.emp_1.email, 'Sara.Gyaan@email.com')
        self.assertEqual(self.emp_2.email, 'Solomiay.Vashisht@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_0.fullname, 'Jane Smith')

        self.assertEqual(self.emp_1.fullname, 'Saral Gyaan')
        self.assertEqual(self.emp_2.fullname, 'Udit Vashisht')

        self.emp_1.first = "Sara"
        self.emp_2.first = "Solomiay"

        self.assertEqual(self.emp_1.fullname, 'Sara Gyaan')
        self.assertEqual(self.emp_2.fullname, 'Solomiay Vashisht')

    def test_apply_raise(self):
        self.emp_0.apply_raise()
        self.assertEqual(self.emp_0.pay, 1164)

        self.emp_1.apply_raise()
        self.assertEqual(self.emp_1.pay, 1166)

        self.emp_2.apply_raise()
        self.assertEqual(self.emp_2.pay, 1224)

    @patch('employee.requests.get')
    def test_monthly_schedule(self, mock_get):
        mock_get.return_value.ok = True
        mock_get.return_value.text = 'ok'
        response = self.emp_0.monthly_schedule('ira')
        print(response)
        self.assertEqual(response, 'ok')
        mock_get.return_value.ok = False
        response = self.emp_0.monthly_schedule('ira')
        print(response)
        self.assertEqual(response, 'Bad Response!')


if __name__ == "__main__":
    unittest.main()

