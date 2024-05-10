import stock as s
def stock_purchase_history():
    stock1 = s.Stock("AAPL", "Apple Inc")
    stock2 = s.Stock("CAT", "Caterpillar")
    stock3 = s.Stock("EK", "Eastman Kodak")
    stock4 = s.Stock("GOOG", "Google")
    stock5 = s.Stock("MSFT", "Microsoft")

    stocks_dict = {
    stock1.get_symbol(): stock1,
    stock2.get_symbol(): stock2,
    stock3.get_symbol(): stock3,
    stock4.get_symbol(): stock4,
    stock5.get_symbol(): stock5
    }

    print(f"{'Symbol':<10}{'Company Name'}")
    print("---------------------------------")

    for symbol, stock in stocks_dict.items():
        print(f"{symbol:<10}{stock.get_company_name()}")