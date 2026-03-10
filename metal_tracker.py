import yfinance as yf
import matplotlib.pyplot as plt

# Download Aluminium and Copper data
aluminium = yf.download("ALI=F", period="6mo")
copper = yf.download("HG=F", period="6mo")

# Plot the prices
plt.figure()

plt.plot(aluminium["Close"], label="Aluminium Price")
plt.plot(copper["Close"], label="Copper Price")

plt.title("Metal Price Tracker")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()

plt.show()
