"""Classes for melon orders."""

import random




class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    shipped = False

    def __init__(self, species, qty, country_code='US'):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.country_code = country_code


    def get_base_price(self):

        self.base_price = random.randint(5, 9)

    def get_total(self):
        # base_price = 5
        base_price = self.get_base_price()
        total = (1 + self.tax) * self.qty * base_price

        # check christmas melon first
        # check international:
            #check if quantity is less than 10

        if self.species == "Christmas Melon": 
            base_price *= 1.5

        if self.country_code != "US" and self.qty < 10:
            total = ((1 + self.tax) * self.qty * base_price) + 3
            total = (round(total, 2))

        return total # get_base_price


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True


    def get_country_code(self):
        """Return the country code."""
        return self.country_code

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08

    # if country_code IS default (US), then this class is instantiated

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17
    country_code = ''

class GovernmentMelonOrder(AbstractMelonOrder):

    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        if passed: 
            self.passed_inspection = True # self.attribute