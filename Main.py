from Stock import Stock
class Main:

    def __init__(self):
        pass

if __name__ == '__main__':
    instrument_token = input("Instrument token>>>")
    Stock(instrument_token).insert()

