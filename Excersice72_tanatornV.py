menuList = []
def showBill():
    print("--------My Food-------")
    totalprice = 0
    for number in range(len(menuList)):
     print (number+1,menuList[number][0], ":",menuList[number][1])
     totalprice += int(menuList[number][1])
    print ("มูลค่ารวมทั้งหมดคือ :" , totalprice)

while True:
    menuFood = input("ใส่ชื่ออาหาร :")
    if menuFood.lower() == "exit":
        break
    else:
        menuPrice = input("ราคาเท่าไหร่ :")
        menuList.append([menuFood,menuPrice])
showBill()

