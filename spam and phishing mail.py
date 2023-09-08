#CYBER SECURITY GROUP PROJECT
#team - Jaynil-Leader, Fizza, Umair, Punith, Kapil, Prathmesh, Nikhil,
from tkinter import *
from tkinter.ttk import Combobox, Scrollbar

from tkinter import messagebox

class MailManagmentSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Spam and Phishing Mail Analysis")
        self.root.geometry("1300x660+0+0")

        self.youremail_var=StringVar()
        self.senderemail_var=StringVar()
        self.mail_var=StringVar()


        lbltitle = Label(self.root, text="Spam And Phishing Mail Analysis", bg="pink", fg="black", bd=13,
                         relief=RIDGE,
                         font=("times new roman", 30, "bold", "underline"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, bg="cyan", padx=20)
        frame.place(x=0, y=80, width=1300, height=600)

        DataFrameLeft = LabelFrame(frame, text="USER INFO", bg="cyan", fg="black", bd=10,
                               relief=RIDGE,
                               font=("times new roman", 15, "bold", "underline"), padx=20)
        DataFrameLeft.place(x=0, y=3, width=650, height=450)

        lblyourEmail = Label(DataFrameLeft, font=("times new roman", 10, "bold"), text="SUBJECT", bg="cyan", padx=2)
        lblyourEmail.grid(row=1, column=0, sticky=W)
        txtyourEmail = Entry(DataFrameLeft, font=("times new roman", 10, "bold"), width=20, textvariable=self.youremail_var)
        txtyourEmail.grid(row=1, column=1)

        lblEmail = Label(DataFrameLeft, font=("times new roman",10,"bold"), text="SENDER E-MAIL", bg="cyan",padx=2)
        lblEmail.grid(row=2,column=0, sticky=W)
        txtEmail=Entry(DataFrameLeft,font=("times new roman",10,"bold"),width=20, textvariable=self.senderemail_var)
        txtEmail.grid(row=2,column=1)

        txtbox= Label(DataFrameLeft, font=("times new roman",10,"bold"),width=20,text="ORIGINAL MAIL", bg="cyan",padx=2)
        txtbox.grid(row=3,column=0,sticky=W)
        txtbox1=Text(DataFrameLeft, font=("times new roman",10,"bold"),width=20,bg="white")
        txtbox1.grid(row=3,column=1)


        DataFrameRight = LabelFrame(frame, text="YOUR MAIL CONTAINS", fg="black", bg="cyan", bd=10,
                                    relief=RIDGE, font=("times new roman", 15, "bold"), padx=2, pady=6)
        DataFrameRight.place(x=600, y=5, width=650, height=450)

        listWords = ["act now","do it today","get it now","expire","limited time","important information","instant","new customers only",
        "now only","take action","urgent","while stock last","for instant access","order now","order today","direct email","direct marketing","credit card offer","you won","you've been selected",
                     "billion dollars","cash bonus","consolidate debt and credit","consolidate your debt","free investment","free money","no string attached","no hidden cost","risk free",
                     "vacation offers","weekend getaway","copy dvds","with according to law","investment","life insurance","passwords","this isn't spam","request","insecure debt","insecure credit",
                     "undisclosed receipient","us dollars","warranty","unsolicited","clean junk","safe from virus","stock alert","subscribe now","zero risk","do it urgent","quick alert","time limited",
        "free access","fantastic deal","free gift","100% free","full refund","click here","only for you","month trial offer","not junk","number one","no cost","no experience","once in lifetime",
        "online degree","oppurtunity","order shipped by","pre approved","promise","special offer","100% satisfaction","visit website","winner","you have been chosen","your chance",
        "your income","zero chance"]

        def Words(event=""):
            value = str(listbox.get(listbox.curselection()))
            x = value
            if x == 'act now':
                messagebox.showwarning("WARNING", "This Mail Might Be A Phishing Mail")

            elif x == 'do it today':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'get it now':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'expire':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'limited time':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'important information':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'instant':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'new customers only':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'now only':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'take action':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'urgent':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'while stock last':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'for instant access':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'order now':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'order today':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'direct email':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'direct marketing':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'credit card offer':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'you won':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'youve been selected':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'billion dollars':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'cash bonus':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'consolidate debt and credit':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'consolidate your debt':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'free investment':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'free money':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'no string attached':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'no hidden cost':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'risk free':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'vacation offers':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'weekend getaway':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'copy dvds':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'according to laws':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'investment':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'life insurance':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'passwords':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'this isnt spam':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'request':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'insecure debit':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'insecure credit':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'undisclosed recepient':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'us dollars':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'warranty':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'unsolicited':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'clean junk':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'safe from virus':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'stock alert':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'subscribe now':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'zero risk':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'do it urgent':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'quick alert':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'time limited':
                messagebox.showwarning("Warning","This Mail Might Be A Phishing Mail")

            elif x == 'free access':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'fantastic deal':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'free gift':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == '100% free':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'full refund':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'click here':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'only for you':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'month trial offer':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'not junk':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'number one':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'no cost':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'no experience':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'once in lifetime':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'online degree':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'oppurtunity':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'order shipped by':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'pre-approve':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'promise':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'special offer':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == '100% satisfaction':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'visit website':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'winner':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'you have been selected':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'your chance':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'your income':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

            elif x == 'zero chance':
                messagebox.showwarning("Warning","This Mail Might Be A Spam Mail")

        listbox = Listbox(DataFrameRight, font=("times new roman", 10, "bold"), width=20, height=16)
        listbox.bind("<<ListboxSelect>>", Words)
        listbox.grid(row=0, column=0, padx=4)
        for i in listWords:
                listbox.insert('end', i)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")
        listScrollbar.config(command=listbox.yview)

        Framebutton = Frame(self.root, bg="cyan", bd=10, relief=RIDGE, padx=20)
        Framebutton.place(x=0, y=480, width=1300, height=160)
        def ExitData():
            self.root.destroy()

        def ResetData():
            self.youremail_var.set("")
            self.senderemail_var.set("")
            self.mail_var.set("")


        def SubmitData():
               messagebox.askyesnocancel("SUBMIT","ARE YOU SURE YOU WANT TO SUBMIT")

        def AddData():
            messagebox.showinfo("ADD","INFO ADDED")

        def DeleteData():
            messagebox.askyesnocancel("DELETE","ARE YOU SURE YOU WANT TO DELETE")

        btnSubmitData = Button(Framebutton, text='SUBMIT', font=("times new roman", 10, "bold"), width=27, height=2,
                               bg="black",
                               fg="pink",command=SubmitData)
        btnSubmitData.grid(row=0, column=0)

        btnAddData = Button(Framebutton, text='ADD', font=("times new roman", 10, "bold"), width=27, height=2,
                            bg="black",
                            fg="pink",command=AddData)
        btnAddData.grid(row=0, column=1)

        btnDeleteData = Button(Framebutton, text='DELETE', font=("times new roman", 10, "bold"), width=27, height=2,
                               bg="black",
                               fg="pink",command=DeleteData)
        btnDeleteData.grid(row=0, column=2)

        btnResetData = Button(Framebutton, text="RESET", font=("times new roman", 10, "bold"), width=27, height=2,
                              bg="black", fg="pink",command=ResetData)
        btnResetData.grid(row=0, column=3)

        btnExitData = Button(Framebutton, text='EXIT', font=("times new roman", 10, "bold"), width=27, height=2,
                             bg="black",
                             fg="pink", command=ExitData)
        btnExitData.grid(row=0, column=4)








if __name__ == '__main__':
    root = Tk()
    obj=MailManagmentSystem(root)
    root.mainloop()
