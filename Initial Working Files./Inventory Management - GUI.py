from cProfile import label
from copyreg import pickle
from msilib.schema import ListBox
from textwrap import fill
from tkinter import*
import tkinter
from tkinter import font
from tkinter import ttk
from turtle import left, title, width
from tkinter import scrolledtext
import pickle

def click():
    global data
    if click(Button-1
    ):
        pass

class xyz:
    def __init__(self,data):
        self.data = data
        self.data.title("xyz")
        self.data.geometry("1550x800+0+0")


        label = Label(self.data,text = "Inventory Management <-- Clothing and Apparel",bg = "blue",fg = "black",bd=20,relief = RIDGE,font=("ARIAL BOLD",20)).pack()

       

        frame = Frame(self.data,relief =RIDGE,bd = 12,padx=20,bg = "powder blue")
        frame.place(x=0,y=130,height=400,width=1530)


# -----------------------------------------dataframe--------------------
        DataFrameLeft = LabelFrame(frame,text = "choose from the option below:",bg = "blue",fg = "black",bd=12,relief = RIDGE,font=("ARIAL BOLD",15))
        b =Button(DataFrameLeft,text = "1. Add an Entry",bg = "grey",bd = 5,relief = RIDGE,font=("ARIAL BOLD",10))
        b.pack(anchor=NW)
        b.bind("<Button-1>",click)
        b  =Button(DataFrameLeft,text = "2.Edit and Existing Entry",bg = "grey",bd = 5,relief = RIDGE,font=("ARIAL BOLD",10))
        b.pack(anchor=NW)
        b  =Button(DataFrameLeft,text = "3.Search an Item",bg = "grey",bd = 5,relief = RIDGE,font=("ARIAL BOLD",10))
        b.pack(anchor=NW)
        b  =Button(DataFrameLeft,text = "4. Display the Entire Database",bg = "grey",bd = 5,relief = RIDGE,font=("ARIAL BOLD",10))
        b.pack(anchor=NW)
        b  =Button(DataFrameLeft,text = "5. Filter the Database",bg = "grey",bd = 5,relief = RIDGE,font=("ARIAL BOLD",10))
        b.pack(anchor=NW)
        b  =Button(DataFrameLeft,text = "6.Delete an Entry",bg = "grey",bd = 5,relief = RIDGE,font=("ARIAL BOLD",10))
        b.pack(anchor=NW)
        b  =Button(DataFrameLeft,text = "7. Register a Sale",bg = "grey",bd = 5,relief = RIDGE,font=("ARIAL BOLD",10))
        b.pack(anchor=NW)
        b  =Button(DataFrameLeft,text = "8. Exit ",bg = "grey",bd = 5,relief = RIDGE,font=("ARIAL BOLD",10))
        b.pack(anchor=NW)
        DataFrameLeft.place(x=0,y=5,width=500,height=350)
        # ---------------------------middleframe----------------------
        DataFrameMiddle = LabelFrame(frame,text = "Enter the details",bg = "black",fg = "white",bd=12,relief = RIDGE,font=("ARIAL BOLD",15))
        label1 = Label(DataFrameMiddle,text="Article number:",bg = "black",fg = "white",font = ("times new roman",10,"bold"))
        label1.grid(row=2,column=1,sticky=W)

        txtlabel1 = Entry(DataFrameMiddle,font = ("times new roman",10,"bold"))
        txtlabel1.grid(row=2,column=2)

        label2 = Label(DataFrameMiddle,text="Article Category:",bg = "black",fg = "white",font = ("times new roman",10,"bold"))
        label2.grid(row=3,column=1,sticky=W)

        txtlabel2 = Entry(DataFrameMiddle,font = ("times new roman",10,"bold"))
        txtlabel2.grid(row=3,column=2)

        label3 = Label(DataFrameMiddle,text="Article Size:",bg = "black",fg = "white",font = ("times new roman",10,"bold"))
        label3.grid(row=3,column=1,sticky=W)

        txtlabel3 = Entry(DataFrameMiddle,font = ("times new roman",10,"bold"))
        txtlabel3.grid(row=3,column=2)

        label4 = Label(DataFrameMiddle,text="Article colour:",bg = "black",fg = "white",font = ("times new roman",10,"bold"))
        label4.grid(row=4,column=1,sticky=W)

        txtlabel4 = Entry(DataFrameMiddle,font = ("times new roman",10,"bold"))
        txtlabel4.grid(row=4,column=2)

        label5 = Label(DataFrameMiddle,text="Date of Manufacturing:",bg = "black",fg = "white",font = ("times new roman",10,"bold"))
        label5.grid(row=5,column=1,sticky=W)

        txtlabel5 = Entry(DataFrameMiddle,font = ("times new roman",10,"bold"))
        txtlabel5.grid(row=5,column=2)
        label6 = Label(DataFrameMiddle,text="Number of peice in stock:",bg = "black",fg = "white",font = ("times new roman",10,"bold"))
        label6.grid(row=6,column=1,sticky=W)

        txtlabel6 = Entry(DataFrameMiddle,font = ("times new roman",10,"bold"))
        txtlabel6.grid(row=6,column=2)

        label7 = Label(DataFrameMiddle,text="Price $ :",bg = "black",fg = "white",font = ("times new roman",10,"bold"))
        label7.grid(row=7,column=1,sticky=W)

        txtlabel7 = Entry(DataFrameMiddle,font = ("times new roman",10,"bold"))
        txtlabel7.grid(row=7,column=2)

        DataFrameMiddle.place(x=400,y=5,width=500,height=350)
        # label = Label(DataFrameLeft,text= "memb")
        DataFrameRight = LabelFrame(frame,text = "Credentials detail",bg = "blue",fg = "black",bd=20,relief = RIDGE,font=("ARIAL BOLD",20))


        DataFrameRight.place(x=870,y=5,width=530,height=350)

        self.txtbox=Text(DataFrameRight,font = ("times new roman",12,"bold"),width=32,height=15)
        self.txtbox.grid(row=0,column=2)
        # f = open("database.dat","rb")
        # ListBox = pickle.load(f)
        # f.close()



        # --------------------------------------------- buttonsframe------------
        frame = Frame(self.data,relief =RIDGE,bd = 12,padx=20,bg = "powder blue")
        frame.place(x=0,y=530,height=70,width=1530)


        # -------------------------information frame-----------------
        frame = Frame(self.data,relief =RIDGE,bd = 12,padx=20,bg = "powder blue")
        frame.place(x=0,y=600,height=195,width=1530)

        

         


if __name__ == "__main__":
    data = Tk()
    obj = xyz(data)
    data.mainloop()













# txt.insert(INSERT,'web application')
# txt = scrolledtext.ScrolledText(data,width=40,height=10)


    





# data = StringVar()
# data.set("")
# screen = Entry(data,textvar = data,font="lucida 40 bold")
# screen.pack(fill = X,ipadx= 8,pady = 10,padx = 10)

# f = Frame(data,bg = "grey")
# b = Button(f,text = "9",padx = 28,pady = 18,font = "licida 35 bold")
# b.pack(side = LEFT,padx = 18,pady=5)
# b.bind("<Button-1>",click)

