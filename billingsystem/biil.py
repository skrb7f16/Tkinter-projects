from tkinter import *
import math,random


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x700+0+0')
        self.root.title("billing software")
        #========Variables========#
        #======customer details variables========#
        self.cname_value=StringVar()
        self.cphn_value=StringVar()
        self.cbill_value=StringVar()
        x=random.randint(1000,9999)
        self.cbill_value.set(str(x))


        #========Grocery variables========#
        self.grocery=[]
        for i in range(0,6):
            self.grocery.append(IntVar())


        #=======Cold drink variables========#
        self.coldrink=[]
        for i in range(0,6):
            self.coldrink.append(IntVar())
        
        #==========Cosmetic variables==========#
        self.cosmetic=[]
        for i in range(0,6):
            self.cosmetic.append(IntVar())
        

        #======bill menu variables===========#
        self.total_cosmetic=StringVar()
        self.total_grocery=StringVar()
        self.total_colddrink=StringVar()
        self.total_cosmetic_tax=StringVar()
        self.total_grocery_tax=StringVar()
        self.total_colddrink_tax=StringVar()
        



        bg_color = "#074463"
        title = Label(self.root, text="Billing software", font=("times new roman", 30,"bold"), pady=2, bd=12, relief=GROOVE, bg=bg_color, fg="white").pack(fill=X)
        #=============customer details frame
        F1=LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,font="arial 15",textvariable=self.cname_value, bd=7, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphn_lbl=Label(F1,text="Phone no",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,font="arial 15",textvariable=self.cphn_value, bd=7, relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        c_bill_lbl=Label(F1,text="Bill Number",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,font="arial 15",textvariable=self.cbill_value, bd=7, relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)
        bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 15 bold").grid(row=0,column=6,padx=10,pady=5)

        #========Cosmetic Frame

        F2=LabelFrame(self.root,text="Cosmetic", font=("times new roman",15,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE)
        F2.place(x=5,y=180 ,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),textvariable=self.cosmetic[0],bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),textvariable=self.cosmetic[1],bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_wash_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        fash_wash_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),textvariable=self.cosmetic[2],bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_spray_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10 ,sticky="w")
        hair_spray_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),textvariable=self.cosmetic[3],bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hair_gel_lbl=Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10 ,sticky="w")
        hair_gel_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),textvariable=self.cosmetic[4],bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_lotion_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10 ,sticky="w")
        hair_lotion_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),textvariable=self.cosmetic[5],bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #========Groceries

        F3=LabelFrame(self.root,text="Groceries", font=("times new roman",15,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE)
        F3.place(x=340,y=180 ,width=325,height=380)

        rice_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),textvariable=self.grocery[0],bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        food_oil_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        food_oil_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),textvariable=self.grocery[1],bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        daal_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        daal_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),textvariable=self.grocery[2],bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        wheat_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10 ,sticky="w")
        wheat_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),textvariable=self.grocery[3],bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        sugar_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10 ,sticky="w")
        sugar_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),textvariable=self.grocery[4],bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        tea_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10 ,sticky="w")
        tea_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),textvariable=self.grocery[5],bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #========Cold Drink Frame

        F4=LabelFrame(self.root,text="Cold Drink", font=("times new roman",15,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE)
        F4.place(x=670,y=180 ,width=325,height=380)

        maza_lbl=Label(F4,text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        maza_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),textvariable=self.coldrink[0],bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        coke_lbl=Label(F4,text="Coke",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        coke_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),textvariable=self.coldrink[1],bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        frooti_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        frooti_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),textvariable=self.coldrink[2],bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        thumbs_up_lbl=Label(F4,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10 ,sticky="w")
        thumbs_up_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),textvariable=self.coldrink[3],bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        limca_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10 ,sticky="w")
        limca_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),textvariable=self.coldrink[4],bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        sprite_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10 ,sticky="w")
        sprite_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),textvariable=self.coldrink[5],bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #================Bill Area

        F5=Frame(self.root,bd=7,relief=GROOVE)
        F5.place(x=1005,y=180,width=340, height=380)
        bill_title=Label(F5,text="Bill Area",font=("arial",15,"bold"),bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #================Bill Menu

        F6=LabelFrame(self.root,bd=7,relief=GROOVE, bg=bg_color,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold")
        F6.place(x=0,y=560,relwidth=1,height=140)

        total_cosmetic_lbl=Label(F6,text="Total Cosmetic Price",font=("times new roman",14,"bold"),fg="white",bg=bg_color).grid(row=0,column=0,sticky="w" ,padx=10,pady=3)
        total_cosmetic_txt=Label(F6,font=("times new roman",10,"bold"),textvariable=self.total_cosmetic,bd=5,relief=SUNKEN,width=18).grid(row=0,column=1,padx=10,pady=3)

        totat_grocery_lbl=Label(F6,text="Total Grocery Price",font=("times new roman",15,"bold"),fg="white",bg=bg_color).grid(row=1,column=0,sticky="w" ,padx=10,pady=3)
        totat_grocery_txt=Label(F6,font=("times new roman",10,"bold"),textvariable=self.total_grocery,bd=5,relief=SUNKEN,width=18).grid(row=1,column=1,padx=10,pady=3)

        total_cold_drink_lbl=Label(F6,text="Total Cold Drink Price",font=("times new roman",14,"bold"),fg="white",bg=bg_color).grid(row=2,column=0,sticky="w" ,padx=10,pady=3)
        total_cold_drink_txt=Label(F6,font=("times new roman",10,"bold"),textvariable=self.total_colddrink,bd=5,relief=SUNKEN,width=18).grid(row=2,column=1,padx=10,pady=3)

        tax_cosmetic_lbl=Label(F6,text="Cosmetic Tax",font=("times new roman",14,"bold"),fg="white",bg=bg_color).grid(row=0,column=3,sticky="w" ,padx=10,pady=3)
        tax_cosmetic_txt=Label(F6,font=("times new roman",10,"bold"),textvariable=self.total_cosmetic_tax,bd=5,relief=SUNKEN,width=18).grid(row=0,column=4,padx=10,pady=3)

        tax_grocery_lbl=Label(F6,text="Grocery Tax",font=("times new roman",15,"bold"),fg="white",bg=bg_color).grid(row=1,column=3,sticky="w" ,padx=10,pady=3)
        tax_grocery_txt=Label(F6,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN,width=18,textvariable=self.total_grocery_tax).grid(row=1,column=4,padx=10,pady=3)

        tax_cold_drink_lbl=Label(F6,text="Cold Drink Tax",font=("times new roman",14,"bold"),fg="white",bg=bg_color).grid(row=2,column=3,sticky="w" ,padx=10,pady=3)
        tax_cold_drink_txt=Label(F6,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN,width=18,textvariable=self.total_colddrink_tax).grid(row=2,column=4,padx=10,pady=3)

        btn_f=Frame(F6,bd=7,relief=GROOVE, bg=bg_color)
        btn_f.place(x=740,width=585,height=105)

        total=Button(btn_f,text="Total",command=self.total,bd=7,relief=GROOVE,font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=20)
        generate=Button(btn_f,text="Generate", command=self.billArea,bd=7,relief=GROOVE,font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=1,padx=10,pady=20)
        clear=Button(btn_f,text="Clear",command=self.clearAll,bd=7,relief=GROOVE,font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=10,pady=20)
        exit=Button(btn_f,text="Exit",bd=7,relief=GROOVE,font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=33,padx=10,pady=20)
        self.bill_welcome()

        #==========prices==========#
        self.cosmetic_prices={
            "Bath Soup":40,
            "Face cream":120,
            "face wash":140,
            "hair spray":180,
            "hair gel":60,
            "body lotion":240
        }
        self.grocery_prices={
            "Rice":50,
            "Food oil":180,
            "daal":60,
            "wheat":300,
            "sugar":34,
            "tea":150
        }
        self.coldrink_prices={
            "maza":40,
            "coke":40,
            "frooti":35,
            "thumbs up":45,
            "limca":30,
            "sprite":80
        }
    def total(self):
        self.total_grocery_price=float(0)
        self.total_cold_drink_price=float(0)
        self.total_cosmetic_price=float(0)
        for i in range(0,6):
            self.total_cosmetic_price+=float(self.cosmetic[i].get()*list(self.cosmetic_prices.values())[i])
            self.total_grocery_price+=float(self.grocery[i].get()*list(self.grocery_prices.values())[i])
            self.total_cold_drink_price+=float(self.coldrink[i].get()*list(self.coldrink_prices.values())[i])
        self.total_cosmetic.set(str(self.total_cosmetic_price))
        self.total_grocery.set(str(self.total_grocery_price))
        self.total_colddrink.set(str(self.total_cold_drink_price))
        self.total_cosmetic_tax.set(str(self.total_cosmetic_price/100))
        self.total_grocery_tax.set(str(self.total_grocery_price/100))
        self.total_colddrink_tax.set(str(self.total_cold_drink_price/100))

    def bill_welcome(self):
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END,"\tWelcome to Shanku Retailer")
        self.txtarea.insert(END,f"\nBill no.  : {self.cbill_value.get()}")
        self.txtarea.insert(END,f"\nName : {self.cname_value.get()}")
        self.txtarea.insert(END,f"\nPhone no. : {self.cphn_value.get()} ")
        self.txtarea.insert(END,"\n======================================")
        self.txtarea.insert(END,"Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END,"\n======================================")
    
    
    def billArea(self):
        self.bill_welcome()
        for i in range(0,6):
            if self.cosmetic[i].get()!=0:
                self.txtarea.insert(END,f"\n{list(self.cosmetic_prices.keys())[i]}\t\t{self.cosmetic[i].get()}\t\t{list(self.cosmetic_prices.values())[i]*self.cosmetic[i].get()}")
            if self.grocery[i].get()!=0:
                self.txtarea.insert(END,f"\n{list(self.grocery_prices.keys())[i]}\t\t{self.grocery[i].get()}\t\t{list(self.grocery_prices.values())[i]*self.grocery[i].get()}")
            if self.coldrink[i].get()!=0:
                self.txtarea.insert(END,f"\n{list(self.coldrink_prices.keys())[i]}\t\t{self.coldrink[i].get()}\t\t{list(self.coldrink_prices.values())[i]*self.coldrink[i].get()}")
        self.grand_total=float(self.total_cosmetic_tax.get())+float(self.total_grocery_tax.get())+float(self.total_colddrink_tax.get())+self.total_cosmetic_price+self.total_grocery_price+self.total_cold_drink_price
        self.txtarea.insert(END,f"\n======================================")
        self.txtarea.insert(END,f"\nTotal\t\t\t\t{self.total_cosmetic_price+self.total_grocery_price+self.total_cold_drink_price}")
        self.txtarea.insert(END,f"\nTotal Tax\t\t\t\t{float(self.total_cosmetic_tax.get())+float(self.total_grocery_tax.get())+float(self.total_colddrink_tax.get())}")
        self.txtarea.insert(END,f"\n======================================")
        self.txtarea.insert(END,f"\nGrand Total\t\t\t\t{self.grand_total}")
    
    def clearAll(self):
        self.bill_welcome()
        for i in range(0,6):
            self.cosmetic[i].set(0)
            self.grocery[i].set(0)
            self.coldrink[i].set(0)



        


root = Tk()

obj = Bill_App(root)

root.mainloop()
