from tabulate import tabulate  # to create table
from math import sqrt  # to generate sqrt formula


class CustomerMembership:
    # benefit of mmembership
    benefit = {
        "Membership": ["Platinum", "Gold", "Silver"],
        "Discount": ["15%", "10%", "8%"],
        "Another Benefit": ["Benefit Silver + Gold +Vacation Voucher+ cashback max 30%", "Benefit Silver + Online Transport Voucher", "Food Voucher"]
    }

    # requirement to be in the membership
    requirement = {
        "Membership": ["Platinum", "Gold", "Silver"],
        "Monthly Expense (mio)": [8, 6, 5],
        "Monthly Income (mio)": [15, 10, 7]
    }

    def __init__(self, username, membership=None):
        """ 
        Initialize the User object with parameters : username
        input: username
        """
        self.username = username
        self.membership = membership

    def show_benefit(self):
        """
        Display all membership benefit
        input : none
        """
        print("PacCommerce Membership Benefit\n")
        print(tabulate(self.benefit, headers="keys",
              tablefmt="grid", stralign="center"))

    def show_requirement(self):
        """
        Display all membership requirement
        input: None
        """
        print("PacCommerce Membership Requirement\n")
        print(tabulate(self.requirement, headers="keys",
              tablefmt="grid", stralign="center"))

    def predict_membership(self, monthly_expense, monthly_income):
        """
        Predict user membership using euclidean formula
        input: monthly_expense, monthly_income
        output : display predictted membership
        """
        min_distance = float('inf')  # closest distance to membership level
        predicted_membership = None

        for level in range(len(self.requirement["Membership"])):
            requirement_expense = self.requirement["Monthly Expense (mio)"][level]
            requirement_income = self.requirement["Monthly Income (mio)"][level]

            # calculate user current distance to membership requirement
            distance = sqrt((monthly_expense-requirement_expense)
                            ** 2 + (monthly_income-requirement_income)**2)

            if distance < min_distance:
                min_distance = distance
                predicted_membership = self.requirement["Membership"][level]

        print(f"{self.username}'s predicted membership is {
              predicted_membership}")
        return predicted_membership

    def calculate_price(self, membership, pricelist):
        """ 
        Calculate total price after membership's benefit applied
        input : membership (str), pricelist (list of float)
        output : display total price after discount
        """
        membership_discount = {
            "Platinum": 0.15,
            "Gold": 0.10,
            "Silver": 0.08
        }  # discount list
        if membership not in membership_discount:
            print("invalid membership")

        total_price = sum(pricelist)
        discount = membership_discount[membership]
        # calculate total price after applying discount
        discounted_price = total_price - (total_price*discount)

        print(f"Total price for {membership} after discount : IDR {
              discounted_price:.2f}")
        return discounted_price


# testing
cust1 = CustomerMembership("kai")
print(f'username : {cust1.username}')
cust1.show_benefit()
cust1.show_requirement()
cust2 = CustomerMembership("Beomgyu")
cust2.predict_membership(10, 15)
cust1.predict_membership(5, 7)
cust1.calculate_price("Silver", [100000, 200000, 50000, 150000])
