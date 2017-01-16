import random
def hfrwa_next(current, dt, rate):
    if random.random() < 0.5:
        return current + rate * dt
    else:
        return current - rate * dt

def hfrwm_next(current, dt, rate):
    if random.random < 0.5:
        return current * (1.0 + rate * dt)
    else:
        return current / (1.0 + rate * dt)

def hfrwa(seed, dt, rate, time):
    steps = int(float(time) / dt)
    t = [0]
    y = [seed]
    for _ in range(steps):
        t.append(t[-1] + dt)
        y.append(hfrwa_next(y[-1], dt, rate))
    return t, y

def simulate(trader, all_prices):
    ts, prices = all_prices
    profits = [0]
    for i in range(1,len(ts)):
        t = ts[:i]
        price = prices[:i]
        buy = trader.buy(t, price)
        sell = trader.sell(t, price)

        trader.stock = buy - sell
        trader.profit -= (buy - sell) * price[-1]

        trader.step(t, price)
    return trader

class AllOrNothing:
    def __init__(self, time_interval=1):
        self.profit = 0
        self.stock = 0
        self.time_interval = time_interval
        self.next_t = time_interval

        self.profits=[0]

    def buy(self, t, price):
        if t[-1] >= self.next_t:
            self.next_t += self.time_interval
            if price[-1] > price[-2]:
                return 1
        return 0
    
    def sell(self, t, price):
        if t[-1] >= self.next_t:
            self.next_t += self.time_interval
            if price[-1] < price[-2]:
                return self.stock
        return 0

    def step(self, t, price):
        self.profits.append(self.profit)

all_prices = hfrwa(0, 0.1, 1, 1000.0)
trader = AllOrNothing()

simulate(trader, all_prices)

t,y = all_prices

import matplotlib.pyplot as plt
plt.show()
plt.plot(t, y, 'b-')
plt.plot(t, trader.profits, 'r-')
plt.axis([t[0], t[-1], min(y), max(y)])
plt.show()