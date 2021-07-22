class Customer:
    name = ""
    lastName = ""
    age = 0 

    def addCart(self):
        print("Add to Cart" ,self.name,self.lastName)
Customer1 = Customer()
Customer1.name = "tanatorn"
Customer1.lastName = "Vaskul"
Customer1.addCart()

Customer2 = Customer()
Customer2.name = "Sukritta"
Customer2.lastName = "Vaskul"
Customer2.addCart()

Customer3 = Customer()
Customer3.name = "Nunnapath"
Customer3.lastName = "Vaskul"
Customer3.addCart()

Customer4 = Customer()
Customer4.name = "Jane"
Customer4.lastName = "Vaskul"
Customer4.addCart()