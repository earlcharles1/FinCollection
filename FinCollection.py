import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

class Info_Calc:
	def __init__(self):
		self.ticker = yf.Ticker('FREE RICK KKR VXX')
		self.data = yf.download(tickers=('FREE RICK KKR VXX'), 
			period = 'ytd', 
			interval = '1h',
			group_by ='ticker', 
			auto_adjust = True, 
			prepost = False)
		self.df = pd.DataFrame(self.data)
		self.returns = np.log(self.df['FREE','Close'] / self.df['FREE','Close'].shift(1))
		self.returns1 = np.log(self.df['VXX','Close'] / self.df['VXX','Close'].shift(1))
		# self.returns2 = np.log(self.df['KKR','Close'] / self.df['KKR','Close'].shift(1))
		# self.returns3 = np.log(self.df['VXX','Close'] / self.df['VXX','Close'].shift(1))
		# self.Return_Deviation = np.std(self.returns)
		self.Price_Deviation = np.std(self.df['FREE','Close'])

	def histo(self):

		plt.hist(self.returns)
		plt.title('Histogram of Daily Returns')
		plt.show()
	def return_plot(self):
		self.cumu = np.cumsum(self.returns)
		self.cumu1 = np.cumsum(self.returns1)
	def bad_code(self):
		return self.cumu
	def bad_code2(self):
		return self.cumu1		



IC = Info_Calc()
dataman = IC.df
IC.return_plot()
plt.plot(IC.bad_code())
plt.plot(IC.bad_code2())
plt.show()

# plt.plot(dataman['FREE', 'Close'].pct_change(),color ='r', label = 'Whole Earth Brands')
# plt.plot(dataman['RICK', 'Close'].pct_change(),color = 'g',label = 'RCI Hospitality')
# plt.plot(dataman['KKR', 'Close'].pct_change())
# plt.plot(dataman['TIP', 'Close'].pct_change())
# plt.plot(dataman['VXX', 'Close'].pct_change())
# plt.legend()
# plt.show()
