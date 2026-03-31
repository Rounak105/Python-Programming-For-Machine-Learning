class father:
    def skill1(self):
        print("father love driving")
class mother:
    def skill2(self):
        print("mother love teaching")
class child(father,mother):
    def skill3(father):
        print("child love dancing")
    
c1=child()
c1.skill3()
c1.skill2()
c1.skill1()
