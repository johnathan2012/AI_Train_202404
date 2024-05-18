#class BMI
#attribute -> name,weight,height
#property -> bmi
#instance method -> status
#輸入
#請輸入姓名
#體重
#身高
#輸出
#徐國堂您好,BMI:26.12,體重:過重

class BMI():
    def __init__(self,n:str):
        self.name = n
    
#    def __repr__(self):
#        return f"這是Person的實體,我的名字是{self.name}" #字串插補
    
class Human(BMI):
    def __init__(self,name:str,weight:int,height:int):
        super().__init__(name)
        self.__weight = weight
        self.__height = height
    
    @property
    def weight(self):
        return self.__weight
    
    @property
    def height(self):
        return self.__height
    
    def __repr__(self):
        message = ""
        message += f"Name:{self.name}\n"
        message += f"Weight:{self.weight}\n"
        message += f"Height:{self.height}\n"
        return message
    
    def bmi(self) -> float: #實體的method
        return round(self.weight / ((self.height/100)**2),ndigits=2)
    

s1 = Human("Johnathan",79,158)
#print(type(s1))
print(s1.name)
print(f"BMI:{s1.bmi()}")
print(s1)