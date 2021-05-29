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
        
    def test_email_negative_case(self):
        self.assertNotEqual(self.emp_0.email,'ira.stan@email.com' )
        self.assertNotEqual(self.emp_1.email, 'saral.gyaan@email.com')
        self.assertNotEqual(self.emp_2.email, 'udit.vashisht@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Saral Gyaan')
        self.assertEqual(self.emp_2.fullname, 'Udit Vashisht')

        self.emp_1.first = "Sara"
        self.emp_2.first = "Solomiay"

        self.assertEqual(self.emp_1.fullname, 'Sara Gyaan')
        self.assertEqual(self.emp_2.fullname, 'Solomiay Vashisht')

    def test_fullname_negative_case(self):
        self.assertNotEqual(self.emp_0.fullname,'ira stan' )
        self.assertNotEqual(self.emp_1.fullname, 'saral gyaan')
        self.assertNotEqual(self.emp_2.fullname, 'udit vashisht')

    def test_apply_raise(self):
        self.emp_0.apply_raise()
        self.assertEqual(self.emp_0.pay, 1164)

        self.emp_1.apply_raise()
        self.assertEqual(self.emp_1.pay, 1166)

        self.emp_2.apply_raise()
        self.assertEqual(self.emp_2.pay, 1260)
      
    def test_apply_raise_negative_case(self):
    	with self.assertRaises(TypeError):
            self.emp_0.apply_raise(1111)
            self.emp_1.apply_raise(1167)
            self.emp_2.apply_raise(2222)
    
    @patch('employee.requests.get')
    def test_monthly_schedule(self, mock_get):
        mock_get.return_value.ok = True
        mock_get.return_value.text = 'ok'
        res = self.emp_0.monthly_schedule('may')
        print(res)
        self.assertEqual(res, 'ok')
        mock_get.return_value.ok = False
        res = self.emp_0.monthly_schedule('may')
        print(res)
        self.assertEqual(res, 'Bad Response!')

if __name__ == "__main__":
    unittest.main()

