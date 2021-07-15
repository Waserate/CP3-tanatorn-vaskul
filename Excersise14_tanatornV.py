def login():
    username = input("Username : ")
    Password = input("Password : ")
    if username == "waserate" and Password == "363638" :
        return True
    else:
        return False

def showMenu():
    print ("---------------------------")
    print ("Hello Welcome Back !")
    print ("1. Vat Calculator")
    print ("2. Price Calculator")

def menuSelect():
    selecet = int(input(">>"))
    return selecet 

def vatcal(totalPrice):
    vat = 7 
    result = totalPrice + (totalPrice * vat / 100)
    return result
  
def pricecal():
    price1 = int(input("ราคาของชิ้นที่ 1 :"))
    price2 = int(input("ราคาของชื้นที่ 2 :"))
    return vatcal (price1 + price2)


if login():
 print (showMenu())
 Chosse = menuSelect()
 if Chosse == 1:
     totalPrice = int(input("ราคาของ :"))
     print(vatcal(totalPrice)) 
 elif Chosse == 2:
     print(pricecal())
else:
    print("try again")
     