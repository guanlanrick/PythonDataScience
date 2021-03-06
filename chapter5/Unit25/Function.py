import numpy as np


sap = np.array(["MMM", "ABT", "ABBV", "ACN", "ACE", "ATVI", "ADBE", "ADT"])
stocks = np.array(list([140.49, 0.97, 40.68, 41.53, 55.7, 57.21, 98.2, 99.19,
                        109.96, 111.47, 35.71, 36.27, 87.85, 89.11, 30.22, 30.91]))

stocks = stocks.reshape(8, 2).T

fall = np.greater(stocks[0], stocks[1])

stocks[1, 0] = np.nan
# print(np.isnan(stocks))

stocks[np.isnan(stocks)] = 0

print(stocks)