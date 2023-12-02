class summation():
    x1=0
    x2=0
    y1=0
    y2=0
    # ایجاد متغییرهای عمومی در کلاس 
    def __init__ (self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        # جمع دو کسر
    def plus (self):
        print((self.x1*self.y2)+(self.x2*self.y1),(self.y1*self.y2))
         # تفریق دو کسر
    def minus (self):
        print((self.x1*self.y2)-(self.x2*self.y1),(self.y1*self.y2))
         # ضرب دو کسر
    def multiplication (self):
        if self.y1 or self.y2 == 0:        #اگر مخرج کسر 0 باشد 
            print('Error :/')
        else:
            print((self.x1*self.x2) , (self.y1*self.y2))
         # تقسیم دو کسر
    def division (self):
        if self.y1 or self.y2 == 0:        #اگر مخرج کسر 0 باشد 
            print('Error :/')
        else:
            print((self.x1*self.y2),(self.y1*self.x2))
        # نمایش خروجی
def main (): 
    x1 , y1 ,x2 , y2 = map(int , input().split())  # دریافت اعداد از کاربر 
    n1 =summation(x1,y1,x2,y2)                          # ایجاد نمونه از کلاس
    print(n1.plus())
    print(n1.minus())
    print(n1.multiplication())
    print(n1.division())
if __name__ == "__main__":             
    main()