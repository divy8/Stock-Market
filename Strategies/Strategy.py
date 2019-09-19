import time
from Manager import Manager
from Strategies.DemoStrategy import DemoStrategy


class Strategy:

    def __init__(self, manager):
        self.running_strategy = []
        self.manager = manager
        pass
        # self.Stock = stock

    def create_new_strategy(self, s_id, stock):
        if s_id == 1:
            return DemoStrategy(stock, self.manager)
        pass

