class DatePro:
    # (1) 멤버변수
    content = "날짜 처리 클래스"

    # (2) 생성자
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    # (3) 객체 메서드(instance method)
    def display(self):
        print(f"{self.year}-{self.month}-{self.day}")

    # (4) 클래스 메서드(class method)
    @classmethod #함수 장식자
    def date_string(cls,dateStr): #'19951025'
        year = dateStr[:4]
        month = dateStr[4:6]
        day = dateStr[6:]

        print(f"{year}년 {month}월 {day}일")

# (5) 객체 멤버
date = DatePro(1995,10,25) #생성자
print(date.content)
print(date.year)
date.display()

# (6) 클래스 멤버
print(DatePro.content)
DatePro.date_string('20221116')