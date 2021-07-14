menuList = []
priceList = []
def showBill():
    print("--------My Food-------")
    totalprice = 0
    for number in range(len(menuList)):
     print (number+1,menuList[number] ,":",priceList[number])
     totalprice += int(priceList[number])
     print ("มูลค่าทั้งหมดคือ :" , totalprice)

while True:
    menuFood = input("ใส่ชื่ออาหาร :")
    if menuFood.lower() == "exit":
        break
    else:
        menuPrice = input("ราคาเท่าไหร่ :")
        menuList.append(menuFood)
        priceList.append(menuPrice)
showBill()

