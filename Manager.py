class Manager:

    # list of all open positions
    def __init__(self):
        self.open_positions = []
        pass

    def get_open_positions(self):
        return self.open_positions
        pass

    def insert(self, strategy):
        self.open_positions.append(strategy)

    def exit(self):
        pass
