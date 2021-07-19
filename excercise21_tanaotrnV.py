from tkinter import *

def leftClickButton(event):
   BMI = (float(textboxweight.get())/((float(textboxHeight.get())/100)**2))
   if BMI > 30:
        A = "อ้วนมาก"
   elif BMI <= 29.99:
        A = "อ้วน"
   elif BMI <= 24.99:
        A = "น้ำหนักเกิน"        
   elif BMI <= 22.99:
        A = "ปกติเหมาะสม"
   elif BMI <= 18.5:
        A = "ผอมเกินไป"      
    
   labelCal.configure(text=A)


main = Tk()
labelHeight = Label(main, text = "ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textboxHeight = Entry(main)
textboxHeight.grid(row=0,column=1)
labelweight = Label(main, text = "น้ำหนัก (kg.)")
labelweight.grid(row=1,column=0)
textboxweight = Entry(main)
textboxweight.grid(row=1,column=1)
Calculatebutton = Button(main, text = "คำนวนค่า BMI")
Calculatebutton.grid(row=2,column=0)
Calculatebutton.bind('<Button-1>',leftClickButton)
labelCal = Label(main, text = "ผลลัพธ์")
labelCal.grid(row=2,column=1)
main.mainloop()