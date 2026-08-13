class StockSpanner:

    def __init__(self):
        self.stock = []
        

    def next(self, price: int) -> int:
        self.stock.append(price)

        span = 0
        for n in reversed(self.stock):
            if n <= price:
                span += 1
            else:
                break

        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


"""

lowest = 75
distance = 2



"""