class father:
    def skill1(self):
        print("father love driving")

class child(father):
    def skill1(self):
        print("child love dancing")
    
p1=father()
p1.skill1()
c1=child()
c1.skill1()

