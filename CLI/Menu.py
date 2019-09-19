from threading import Thread

from Stocks import Stocks


class Menu(Thread):

    def __init__(self, manager, strategy):
        Thread.__init__(self)
        self.daemon = True
        self.manager = manager
        self.strategy = strategy

    def run(self):
        while True:
            command = int(input("Enter Command"))
            if command == 1:
                instrument_token = input("instrument_token")
                stock = Stocks().get_stock(instrument_token)
                s_id = int(input("Strategy Id"))
                strategy = self.strategy.create_new_strategy(s_id, stock)
                self.manager.insert(strategy)
                # add new stock to watch list
                pass
            elif command == 2:
                for open in self.manager.get_open_positions():
                    print(open)
                # show list of stocks under Manager
                pass
            else:
                pass
            pass
