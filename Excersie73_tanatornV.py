system = {"ข้าวมันไก่":50,"ข้าวหน้าเป็ด":47,"ข้าวขาหมู":45}
menuList = []
def showBill():
    totalPrice = 0
    print("--------My Food-------")
    for number in range(len(menuList)):
     print (number+1,menuList[number][0], ":",menuList[number][1])
     totalPrice += menuList[number][1]
    print ("ราคารวมทั้งหมดคือ :",totalPrice,"บาท") 

def Vat(totalprice):
    totalVat = ()

while True:
    menuFood = input("ใส่ชื่ออาหาร :")
    if menuFood.lower() == "exit":
        break
    else:
       menuList.append([menuFood,system[menuFood]])
showBill()
