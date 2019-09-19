from Strategies.Strategy import Strategy


class Stock:
    stocks_list = []

    def __init__(self, instrument_token):
        self.instrument_token = instrument_token
        self.stock_price = [10, 20, 30, 40, 50, 60, 10, 20, 10]

    def insert(self):
        pass
