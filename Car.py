# Name: Taylor Brent and Megahn McClaskey       Date Assigned: 11.14.17
#
# Course: CSE 1284 Sec 7                        Date Due: 11.14.17
#
# Program Description: The program is a class that assists in the larger program of
# determining the winner of a demolition derby. The class gets the names of driver,
# the model, number of hits, and adds hits. 

class Car:
        def __init__(self, name = "unknown", model = "unknown"):
                self.hits = 0
                self.name = name
                self.model = model

        def __str__(self):
                return str(self.name) + '\t' + str(self.model)

        def get_driver(self):
                return str(self.name)

        def get_model(self):
                return str(self.model)

        def get_hits(self):
                return str(self.hits)

        def add_hit(self):
                self.hits += 1
