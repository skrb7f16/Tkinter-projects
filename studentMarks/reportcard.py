from tkinter import *
import math

root=Tk()

root.title("Student Management")
root.geometry("1500x800+0+0")


#=========variables==========#
bg_color="blue"
sname=StringVar()
admission=StringVar()
year=StringVar()

#===========subjects variables=========#
sub=[]
cred=[]
for i in range(0,5):
    sub.append(StringVar())
    cred.append(StringVar())

#=========marks varibales=============#
marksVar=[]
for i in range(0,6):
    marksVar.append([StringVar() for i in range(0,5)])

total_exam_wise=[]
for i in range(0,7):
    total_exam_wise.append(StringVar())

total_subwise=[]
for i in range(0,5):
    total_subwise.append(StringVar())

#==============result variable================#
cgpa=StringVar()
percent=StringVar()
status=StringVar()


lbl=Label(root,text="Nmit Student Marks Report", font=("times new roman",30,"bold"),bg="blue",fg="white",bd=7,relief=GROOVE,pady=2).pack(fill=X)


#===========students details===============================#

F1=LabelFrame(root,text="Students Details",font=("arial",15,"bold"),fg="gold",bg="blue",bd=7,relief=GROOVE)
F1.place(x=0,y=65,relwidth=1)

sname_lbl=Label(F1,text="Student Name",font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=0,column=0,pady=5,padx=20)
sname_txt=Entry(F1,width=15,font="arial 18 bold",bd=4,relief=SUNKEN,textvariable=sname).grid(row=0,column=1,padx=10,pady=5)

admission_lbl=Label(F1,text="Admission no.",font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=0,column=2,pady=5,padx=20)
admission_txt=Entry(F1,width=15,font="arial 18 bold",bd=4,relief=SUNKEN,textvariable=admission).grid(row=0,column=3,padx=10,pady=5)

year_lbl=Label(F1,text="Year",font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=0,column=4,pady=5,padx=20)
year_txt=Entry(F1,width=15,font="arial 18 bold",bd=4,relief=SUNKEN,textvariable=year).grid(row=0,column=5,padx=10,pady=5)

#===========subjects and credit ==================#
F2=LabelFrame(root,text="Subjects and Credits",font=("arial",15,"bold"),fg="gold",bg="blue",bd=7,relief=GROOVE)
F2.place(x=0,y=150,relwidth=1)
subjects_lbl=Label(F2,text="Subjects",font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=0,column=0,pady=1,padx=10,sticky="w")
credits_lbl=Label(F2,text="Credits",font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=1,column=0,pady=1,padx=10,sticky="w")
subject=[]
credit=[]
for i in range(0,5):
    subject.append(Entry(F2,width=15,font="arial 18 bold",bd=4,relief=SUNKEN,textvariable=sub[i]).grid(row=0,column=i+1,padx=10,pady=5))
    credit.append(Entry(F2,width=15,font="arial 18 bold",bd=4,relief=SUNKEN,textvariable=cred[i]).grid(row=1,column=i+1,padx=10,pady=5))
total_lbl=Label(F2,text="Total",font=("times new roman",28,"bold"),fg="white",bg=bg_color).grid(row=1,column=6,pady=1,padx=10,sticky="w")


#==============exams and marks frame===========#


F3=LabelFrame(root,text="Exams and Marks",font=("arial",15,"bold"),fg="gold",bg="blue",bd=7,relief=GROOVE)
F3.place(x=0,y=285,relwidth=1)
exams=["MSE-1","MSE-2","MSE-3","LA-1","LA-2","External"]
exam_lbl=[]
marks=[]
total_subwise_txt=[]
total_exam_wise_txt=[]
for i in range(0,6):
    exam_lbl.append(Label(F3,text=exams[i],font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=i,column=0,pady=1,padx=10,sticky="w"))
    for k in range(1,6):
        marks.append(Entry(F3,width=15,font="arial 18 bold",bd=4,relief=SUNKEN,textvariable=marksVar[i][k-1]).grid(row=i,column=k,padx=10,pady=5))
total_subwise_lbl=Label(F3,text="Total",font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=6,column=0,pady=10,padx=10,sticky="w")
for i in range(0,5):
    total_subwise_txt.append(Entry(F3,width=15,font="arial 18 bold",bd=4,relief=SUNKEN, textvariable=total_subwise[i]).grid(row=6,column=i+1,padx=10,pady=10))

for i in range(0,7):
    total_exam_wise_txt.append(Entry(F3,width=15,font="arial 18 bold",bd=4,relief=SUNKEN,textvariable=total_exam_wise[i]).grid(row=i,column=6,padx=10,pady=5))

#==================functions and operations======================#
for i in range(0,6):
    for j in range(0,5):
        marksVar[i][j].set("0")
def avgCal(a,b,c):
    avg=[]
    avg.append((a+b)/2)
    avg.append((a+c)/2)
    avg.append((b+c)/2)
    best=max(avg)
    return best
def addArray(a):
    b=0
    for i in a:
        b=float(i)+b
    return b

def cgpafunc(a):
    creditSub=[]
    for i in range(0,5):
        creditSub.append(int(cred[i].get()))
    a=[int(i/10) for i in a]
    b=[a[i]*creditSub[i] for i in range(0,5)]
    c=[10*creditSub[i] for i in range(0,5) ]
    return sum(b)/sum(c)

    
total=[] 
def mainFunc():
    best=[]
    for i in range(0,5):
        best.append(avgCal(int(marksVar[0][i].get()),int(marksVar[1][i].get()),int(marksVar[2][i].get())))
    for j in range(0,5):
        total.append(best[j]+int(marksVar[3][j].get()) +int(marksVar[4][j].get()) +int(marksVar[5][j].get())/2 )
    for i in range(0,5):
        total_subwise[i].set(str(float(total[i])))
    total_exam=[]
    for i in range(0,6):
        a=0
        for j in range(1,5):
            total_exam.append(a+int(marksVar[i][j].get()))
    for i in range(0,6):
        total_exam_wise[i].set(str(total_exam[i]))
    total_exam_wise[6].set(str(addArray(total)))
    cgpa.set(str(cgpafunc(total)))
    percent.set(str(sum(total)/5))
    if(float(cgpa.get())<3.5):
        status.set("Fail")
    else:
        status.set("Pass")


def printPaper():
    with open(f"{sname.get()}.txt","a") as f:
        f.write(f"\t\t\t================Nmit Report card==============\nName : {sname.get()}\nAdmission no : {admission.get()}\nYear : {year.get()}\n ")
        f.write("==============================================================================================================\n")
        f.write("Subject\t\t\tCredits\t\t\tGradePOints\n")
        for i in range(0,5):
            f.write(f"{sub[i].get()}\t\t\t\t{cred[i].get()}\t\t\t\t{int(total[i]/10)}\n")
        f.write("==============================================================================================================\n")
        f.write(f"Cgpa : {cgpa.get()}\nPercent : {percent.get()}\nStatus : {status.get()}")
        f.close()

#============================result frame=====================#

F4=LabelFrame(root,text="Result",font=("arial",15,"bold"),fg="gold",bg="blue",bd=7,relief=GROOVE)
F4.place(x=0,y=670,relwidth=1)

res_percent=Label(F4,text="Percentage",font=("times new roman",22,"bold"),fg="white",bg=bg_color).grid(row=0,column=0,pady=10,padx=10,sticky="w")
res_percent_txt=Entry(F4,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,textvariable=percent).grid(row=0,column=1,padx=5,pady=10)
res_cgpa=Label(F4,text="CGPA",font=("times new roman",22,"bold"),fg="white",bg=bg_color).grid(row=0,column=2,pady=10,padx=10,sticky="w")
res_cgpa_txt=Entry(F4,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,textvariable=cgpa).grid(row=0,column=3,padx=5,pady=10)
res_status=Label(F4,text="Status",font=("times new roman",22,"bold"),fg="white",bg=bg_color).grid(row=0,column=5,pady=10,padx=10,sticky="w")
res_status_txt=Entry(F4,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,textvariable=status).grid(row=0,column=6,padx=5,pady=10)
cal=Button(F4,text="Calculate",font="arial 20 bold", bd=5 ,relief=GROOVE,command=mainFunc).grid(row=0,column=7 ,padx=60)
cal=Button(F4,text="Print",font="arial 20 bold", bd=5 ,relief=GROOVE,command=printPaper).grid(row=0,column=8 ,padx=10)

F5=Label(root,text="Made by Shashank",bg=bg_color ,font=("times new roman",15,"bold"),bd=3,relief=GROOVE)
F5.place(x=0,y=765,relwidth=1)

    

    
root.mainloop()