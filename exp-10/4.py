class a1:
    def aa(n):
        n=10
class a2(a1):
    def aaa(n1):
        n1=18
    def __add__(n,n1):
        sum=n+n1
    def display(sum):
        print(sum)
c1=a2()
c1.display()

