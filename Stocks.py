from Stock import Stock


class Stocks:
    stocks_list = {}

    def __init__(self):
        pass

    def get_stock(self, instrument_token):
        if instrument_token in self.stocks_list:
            return self.stocks_list[instrument_token]
        else:
            ss = Stock(instrument_token)
            self.stocks_list[instrument_token] = ss
            return ss
