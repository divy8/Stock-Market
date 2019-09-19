from Strategy import Strategy
class Stock:
    stock_price = [10,20,30,40,50,60,10,20,10]

    def __init__(self, instrument_token):
        self.instrument_token = instrument_token

    def insert(self):
        Strategy(Stock).analysis(Stock)
        pass
