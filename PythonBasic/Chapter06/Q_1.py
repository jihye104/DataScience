class FourCal:
    first = second = 0

    def __init__(self,first,second):
        self.first = first
        self.second = second

    def setdata(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        return self.first+self.second

    def mul(self):
        return self.first*self.second

    def sub(self):
        return self.first-self.second

    def div(self):
        return self.first//self.second

a = FourCal(4,2)
a.setdata(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

b = FourCal(3,8)
b.setdata(3,8)
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())