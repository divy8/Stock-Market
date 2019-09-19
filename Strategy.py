import time
from  Manager import Manager
class Strategy:

    def __init__(self, Stock):
        self.Stock=Stock
        pass

    def analysis(self, Stock):
        print("processing")
        time.sleep(30)
        x=input("Enter strategy>>")
        count=0

        if x==1:
            print("Processing")
            time.sleep(30)
            for x in Stock.stock_price:
                count = 0
                if x>x+1:
                    count=count+1
                else:
                    count=count-1

        if count>0:
            self.buy_trigger()
        else:
            self.sell_trigger()
        pass

    def buy_trigger(self):
        print("stock bought")
        Manager().exit(1)
        pass

    def sell_trigger(self):
        print("Stock-Market Sold")
        Manager().exit(2)
        pass
