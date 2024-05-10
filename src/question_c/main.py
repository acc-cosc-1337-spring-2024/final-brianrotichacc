import stock as s
import stock_report as sr


stock1 = s.Stock("AAPL", "Apple Inc")
stock2 = s.Stock("CAT", "Caterpillar")
stock3 = s.Stock("EK", "Eastman Kodak")
stock4 = s.Stock("GOOG", "Google")
stock5 = s.Stock("MSFT", "Microsoft")

report = sr.StockReport()

report.add_stock(stock1)
report.add_stock(stock2)
report.add_stock(stock3)
report.add_stock(stock4)
report.add_stock(stock5)


report.display_report()