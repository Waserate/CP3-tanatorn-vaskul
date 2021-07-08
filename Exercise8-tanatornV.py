'''
ในการเข้าใช้งานโปรแกรมให้ผู้ล็อคอินโดยใช้ Username และ Password(ผู้เรียนกำหนดเอง)
หากสำเร็จ โปรแกรมจะขึ้นหน้าต้อนรับและแสดงรายการสินค้าพร้อมราคา (ผู้เรียนกำหนดเอง)
เมื่อเลือกสินค้าที่ต้องการเรียบร้อยแล้ว โปรแกรมจะถามจำนวนที่ต้องการซื้อ
หลังจากผู้ซื้อเลือกเรียบร้อยแล้ว โปรแกรมจะทำการแสดงสรุปราคารวมของรายการสั่งซื้อทั้งหมด
'''
username = input("Username : ")
Password = input("Password : ")
if username == "waserate" and Password == "363638" :
    print ("---------------------------")
    print ("Hello Welcome Back !")
    print ("1. Cookie : 10 Bath")
    print ("2. Cake   : 20 Bath")
    print ("3. water  : 5.5 Bath")
    Chosse1 = input("Pls Choose Menu (1,2,3):")
    if Chosse1 == "1":
        Chosse1a = int(input("ต้องการซื้อจำนวนเท่าไหร่ :"))
        print ("จำนวนเงินที่คุณต้องจ่ายคือ :",Chosse1a*10 )
    elif Chosse1 == "2":
         Chosse1b = int(input("ต้องการซื้อจำนวนเท่าไหร่ :"))
         print ("จำนวนเงินที่คุณต้องจ่ายคือ :",Chosse1b*20 )
    elif Chosse1 == "3":
         Chosse1c = int(input("ต้องการซื้อจำนวนเท่าไหร่ :"))
         print ("จำนวนเงินที่คุณต้องจ่ายคือ :",Chosse1c*5.5 )
else:
 print ("try Again")