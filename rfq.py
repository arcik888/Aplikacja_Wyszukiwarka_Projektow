class RFQ:
    import datetime
    from login import Logging, cs, cur
    import os

    def __init__(self, customer, name, top_cat, num):
        self.customer = customer
        self.name = name
        self.top_cat = top_cat
    
    def catalogue(self):
        year = datetime.datetime.now().date().year
        rfq_num = "#" + '1'
        cat1 = self.top_cat + '\\' + year
        cat2 = cat1 + rfq_num


customer = input("nazwa klienta: ")
name = input("nazwa zapytania: ")
top_cat = 'C:\\Users\\arcik\\Desktop\\RFQ'

