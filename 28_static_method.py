"""
Static Method:

Requirement:
    - add method to compute average salary
    - In simple terms, if we pass 2 numbers then
    it should return avg of 2 numbers

"""

print("Static Method")
print("-"*20)
# -------------------


class Employee:
    def add_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

    # Here we don't need to pass 'self' i.e instance object to function
    # We are no where using instance object inside function, it is waste
    # def get_avg_salary(self, sal1, sal2):
    #     return (sal1+sal2)/2

    # Here we don't need to pass 'cls' i.e class object to function
    # We are no where using class object inside function, it is waste
    # @classmethod
    # def get_avg_salary(cls, sal1, sal2):
    #     return (sal1+sal2)/2

    @staticmethod # cls/self will NOT be passed in 1t argument
    def compute_avg_salary(sal1, sal2):
        return (sal1+sal2)/2

e1 = Employee()
e2 = Employee()

e1.add_salary(20000)
e2.add_salary(30000)

s1 = e1.get_salary()
s2 = e2.get_salary()

# avg = Employee.compute_avg_salary(s1,s2)
# OR
avg = e1.compute_avg_salary(s1,s2)
print("Avg Sal:", avg)

print("#"*40, end="\n\n")
###########################################