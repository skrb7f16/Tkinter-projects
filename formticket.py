from tkinter import *

root = Tk()
#widthxheight
root.geometry("400x300")
root.minsize(200,100)
root.maxsize(1200,800)

def getvals():
    print("submitting form")
    foodser='No'
    if foodservice.get()==1:
        foodser='Yes'
    rec=[namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get()]
    rec.append(foodser)
    print(rec)
    cols=['Name','Phone no',"Gender",'Emergency','Payement mode', 'Meals Services']
    with open('record.txt', 'a') as f:
        f.write('\n')
        for i in range(0,len(rec)):
            f.write(f"{cols[i]}:- {rec[i]}\n")
    Label(root,text='Submitted! Thank you', pady=20).grid(row=8,column=3)
    nameentry.delete(0,'end')
    phoneentry.delete(0,'end')
    genderentry.delete(0,'end')
    emergencyentry.delete(0,'end')
    paymentmodeentry.delete(0,'end')



Label(root,text="Welcome to My travel Agency", font="arial 13 bold", pady=20).grid(row=0,column=3)

# creating the text
name=Label(root, text="Name")
phone=Label(root, text="Phone")
gender=Label(root, text="Gender")
emergency=Label(root, text="Emergency Contact")
paymentmode=Label(root, text="Payement")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservice=IntVar()

# creating entry widgets

nameentry=Entry(root, textvariable=namevalue)
phoneentry=Entry(root, textvariable=phonevalue)
genderentry=Entry(root, textvariable=gendervalue)
emergencyentry=Entry(root, textvariable=emergencyvalue)
paymentmodeentry=Entry(root, textvariable=paymentmodevalue)


nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

# btns
food=Checkbutton(root,text='Want to get meals during travel prebooked', variable=foodservice)
food.grid(row=6,column=3)
Button(text='submit form', command=getvals).grid(row=7,column=3)


root.mainloop()