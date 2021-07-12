def vatCal(totalprice):
    result = totalprice+(totalprice*7/100)
    return result
X = int(input("Price :"))
print ("คุณจะต้องจ่าย",vatCal(X))