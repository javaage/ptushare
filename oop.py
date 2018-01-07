class Stock(object):
    """docstring for Hotel"""
    def __init__(self, code,open,current,high,low,date,clmn=0):
        self.code = code
        self.open = open
        self.current = current
        self.high = high
        self.low = low
        self.clmn = clmn
        self.date = date
a = Stock(1,2,3,4,5,6)

print a.code
print a.clmn