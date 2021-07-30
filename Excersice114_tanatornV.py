from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
import datetime
import math

c = CurrencyRates()
b = BtcConverter()   

year = 0
month = 0 
day = 0 
price_in_range = []

def date_obj(year,month,day):
   date_obj = datetime.datetime(year,month,day)
   return date_obj


def loopDay(day,next_day):
    for loop in range(next_day):
        day = day + loop
        bitcoin_last_price = b.get_previous_price('USD',date_obj(year,month,day))
        price_in_range.append(bitcoin_last_price)
        print ("วันที่",loop+1,"ราคา :",bitcoin_last_price)

def mean_calculate(value, max):
    totalSum = math.fsum(value)
    return totalSum/max


def conclusion_price(mean):
     print ("ค่าส่วนต่างเฉลี่ยอยู่ที่ :",(((price_in_range[2]-mean)/mean)*100),"เปอร์เซ็นต์")
     return (((price_in_range[2]-mean)/mean)*100)


def difference_cal(difference):
    if difference >= 100:
        print ('ส่วนต่างเยอะมาก')
    elif difference >= 50:
        print ('ส่วนต่างปานกลาง')
    elif difference >= 25:
        print ('ส่วนต่างน้อย')
    elif difference >= 0:
        print ('ส่วนต่างแทบไม่มี')
    elif difference == 0:
        print ('ไม่มีส่วนต่าง')
    elif difference <= 0:
        print ('ส่วนต่างติดลบไม่ควรเทรด')


year = int(input("กรุณากรอกปี :"))
month = int(input("กรุณากรอกเดือน :"))
day = int(input("กรุณากรอกวัน :"))
next_day = int(input("กรุณากรอกจำนวนวันที่ต้องการจะดู :"))

print ('วันที่เริ่ม',day,'เดือน',month,'ปี',year,'ถึงถัดไปอีก',next_day,'วันข้างหน้า')
loopDay(day,next_day)
mean = mean_calculate(price_in_range, next_day)
print ('ค่าเฉลี่ยของ',next_day,'วันคือ :' ,mean)
difference = conclusion_price(mean)
difference_cal(difference)
