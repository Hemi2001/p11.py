class Time:
    def __init__ (self,h,m,s):
        self.h = h
        self.m = m
        self.s = s
        
    def sum(self,t) :
        h=self.h + t.h
        m=self.m +t.m
        s=self.s + t.s
        if s >= 60 :
            s-=60
            m+=1
        if m >= 60 :
            m-+60
            h+=1
        result = Time(h,m,s)
        return result
    def sub(self) :
        ...
    def show(self):
        print(f"{self.h} :{self.m} :{self.s} ")
        
t1 = Time(8,50,23)
t1.show()
t2 = Time(15,21,36)
t2.show()

s= t1.sum(t2)
s.show()
        