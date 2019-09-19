import time


class DemoStrategy():

    def __init__(self, stock, manager):
        self.stock = stock
        self.manager = manager
        pass

    def analysis(self):
        print("processing ... ")
        time.sleep(5)
        print("Got Buy Trigger ... ")
        self.trigger()

    def trigger(self):
        self.manager.insert(self)

    def __str__(self):
        return "Demo Strategy"
