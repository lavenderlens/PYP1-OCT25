from abc import ABC, abstractmethod

class Customer(ABC):
    def __init__(self, name, **address):
        super().__init__()
        self.name = name
        self.address = dict()
    pass

class BusinessCustomer(Customer):
    def __init__(self, name, **address):
        super().__init__(name, **address)
        self.acc_num = 0

class ResidentialCustomer(Customer):
    def __init__(self, name, **address):
        super().__init__(name, **address)

class Staff(ABC):
    def __init__(self, name, years_with_company, **contact_details):
        super().__init__()
        self.name = name
        self.years_with_company = years_with_company
        self.contact_details = dict()
    def file_for_tax(self, tax_rate, gross_income):
        return tax_rate * gross_income / 52
    pass

# make Staff abstract - no such thing as a Staff
# subclass Staff into CallCenterStaff and EngineeringStaff 

class CallCentreStaff(Staff):
    def __init__(self, name, years_with_company, **contact_details):
        super().__init__(name, years_with_company, **contact_details)
        self.operator_id = 0
    @abstractmethod
    def file_for_tax(self, tax_rate, gross_income, sales_bonus):
        return tax_rate * (gross_income + sales_bonus) / 52

    pass

class Engineering(Staff):
    def __init__(self, name, years_with_company, **contact_details):
        super().__init__(name, years_with_company, **contact_details)
        self.location = "London"
    pass



