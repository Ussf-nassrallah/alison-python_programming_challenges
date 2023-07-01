import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def test_email(self):
        print("test_email")

        emp_1 = Employee("Youssef", "Nasrallah", 100000)
        emp_2 = Employee("Yahya", "Elhamdie", 50000)
        self.assertEquals(emp_1.email, "Youssef.Nasrallah@gmail.com")
        self.assertEquals(emp_2.email, "Yahya.Elhamdie@gmail.com")

        emp_1.first = "Iliass"
        emp_1.last = "Fokhar"
        emp_2.first = "Hamza"
        emp_2.last = "Nait"
        self.assertEquals(emp_1.email, "Iliass.Fokhar@gmail.com")
        self.assertEquals(emp_2.email, "Hamza.Nait@gmail.com")

    def test_fullname(self):
        print("test_fullname")

        emp_1 = Employee("Abderhman", "Elkhomssi", 12000)
        emp_2 = Employee("Walid", "Amin", 24000)
        self.assertEquals(emp_1.fullname, "Abderhman Elkhomssi")
        self.assertEquals(emp_2.fullname, "Walid Amin")

        emp_1.first = "Yassin"
        emp_1.last = "Nasrallah"
        emp_2.first = "Nissrin"
        emp_2.last = "Elidrissi"
        self.assertEquals(emp_1.fullname, "Yassin Nasrallah")
        self.assertEquals(emp_2.fullname, "Nissrin Elidrissi")

    def test_apply_raise(self):
        print("test_apply_raise")

        emp_1 = Employee("Youssef", "Nasrallah", 100000)
        emp_2 = Employee("Yahya", "Elhamdie", 50000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEquals(emp_1.pay, 150000)
        self.assertEquals(emp_2.pay, 75000)


if __name__ == "__main__":
    unittest.main()