import stock
class StockReport:
    def __init__(self):
        self.stocks_dict = {}

    def add_stock(self, stock):
        self.stocks_dict[stock.get_symbol()] = stock

    def display_report(self):
        print(f"{'Company':<20}{'Symbol'}")
        print("-" * 30)
        for symbol, stock in self.stocks_dict.items():
            print(f"{stock.get_company_name():<20}{symbol}")