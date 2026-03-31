class Number:
    def __init__(self,value):
        self.value=value
    def __sub__(self,other):
        return Number(self.value-other.value)
    def display(self):
        print("Difference: ",self.value)
n1=Number(90)
n2=Number(10)
n3=n1-n2
n3.display() 