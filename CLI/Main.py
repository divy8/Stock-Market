from Manager import Manager
from CLI.Menu import Menu
from Strategies.Strategy import Strategy

if __name__ == '__main__':
    manager = Manager()
    strategy = Strategy(manager)
    m = Menu(manager, strategy)
    # hello .
    m.start()

    m.join()
    # instrument_token = input("Instrument token>>>")
    # Stock(instrument_token).insert()
