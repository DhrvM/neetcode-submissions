class StockSpanner:

    def __init__(self):
        self.stock = [] # (price, span)
        

    def next(self, price: int) -> int:

        span = 1
        i = len(self.stock) - 1
        while i >= 0 and self.stock[i][0] <= price :
            span += self.stock[i][1]
            self.stock.pop()
            i = len(self.stock) - 1

        self.stock.append([price, span])

        return span

            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


"""

[[], [100], [80], [60], [70], [60], [75], [85]]
[  ,   1,   , 1,   , 1,   2,    1,    4,   6]



"""