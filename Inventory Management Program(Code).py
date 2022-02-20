import pickle
def is_empty():
    temp=None
    try:
        f=open("database.dat", "rb")
        temp=pickle.load(f)
    except:
        return True
    if temp!=None:
        return False
    f.close()    
    
def add_entry():
    print("1. Multiple Entries")
    print("2. Single Entry")
    quary=int(input("Choose an option(1/2): "))
    f=open("database.dat", "rb")
    
    if is_empty():
        L={}
    else:
        L=pickle.load(f)
    print(L)

    if quary==1:
        N=int(input("Enter the number of Entries to be added: "))
    elif quary==2:
        N=1        
    
    try:            
        cat=["Men's formal", "Men's Casual", "Women's Formal", "Women's Casual", "Kids"]
        size=["XS", "S", "M", "L", "XL", "XXL"]
        for i in range(N):
            print()
            print("for entry number", i+1)
            ArtNum=int(input("Enter the Article Number: "))
            if ArtNum not in L.keys():
                print("Choose From categories:", cat)
                ArtCat=input("Enter the Article Category: ")
                print("Choose From Sizes:", size)                    
                ArtSize=input("Enter the Size: ")
                ArtColor=input("Enter the Article Color: ")
                ArtDOM=input("Enter the Date Of Manufacturing: ")
                ArtCount=int(input("Enter the Number of pieces in Stock: "))
                ArtPrice=int(input("Enter the Price of the item: "))
                temp=[ArtCat, ArtSize, ArtColor, ArtDOM, ArtCount, ArtPrice]
                L[ArtNum]=temp                
            else:
                f.close()
                ask=input("The entered Article is already present in stock, Do you wish to Edit the entry (y/n): ")
                if ask=="y"or"Y":
                    print(ArtNum, "=>", L[ArtNum])
                    edit_item()
                elif ask=="n"or"N":
                    pass
                else:
                    raise Exception
            f=open("database.dat", "w+b")
            pickle.dump(L,f)
            f.close()
    except:
        print("User End error - User entered something unacceptable, Please check your input")

def edit_item():
    f=open("database.dat", "rb")
    L=pickle.load(f)
    f.close()
    try:
        ArtNum=int(input("Enter the Article Number: "))
        if ArtNum in L.keys():
            f=open("database.dat", "w+b")
            print("What do you wish to edit?: ")
            print("1. Category [Current - ", L[ArtNum][0], "]")
            print("2. Size [Current - ", L[ArtNum][1], "]")
            print("3.Color [Current - ", L[ArtNum][2], "]")
            print("4.Date of Manufacturing [Current - ", L[ArtNum][3], "]")
            print("5.Number of items in the Stock [Current - ", L[ArtNum][4], "]")
            print("5.Price of the Item [Current - ", L[ArtNum][5], "]")
            print()
            ch=int(input("Enter your Choice: "))
            if ch in [1, 2, 3, 4]:
                val=input("Kindly enter the new Values: ")
            elif ch==5 or ch==6:
                val=int(input("Kindly enter the new Values: "))
            L[ArtNum][ch-1]=val
            pickle.dump(L,f)
            f.close()
            print()
            print("The Updated Entry is")
            print(ArtNum, "=>", L[ArtNum])
        else:
            ask=input("The entered Article Number doesn't Exist, Do you wish to add a New Entry? (Y/N): ")
            if ask=="Y"or"y":
                add_entry()
            elif ask=="N"or"n":
                pass
            else:
                print("Invalid Input")
    except:
        pickle.dump(L,f)

def search_item(ArtNum): 
    f=open("database.dat", "rb")
    L=pickle.load(f)
    key=L.keys()
    if ArtNum in key:
        print("Article Number => Article Category, Article Size, Article Color, Date of Manufacturing, Number of pieces in Stock, Price")
        print(L[ArtNum])
    else:
        print("There is no Article with the Entered Article Number")
        raise Exception
    f.close()

def display():
    f=open("database.dat", "rb")
    L=pickle.load(f)
    key=L.keys()
    print("Article Number => Article Category, Article Size, Article Color, Date of Manufacturing, Number of pieces in Stock, Price")
    
    print()
    for i in key:
        print(i, "=>", L[i])
    f.close()
    
def price_range(L):
    minval=int(input("Enter the Minimum Price: "))
    maxval=int(input("Enter the Maximum Price: "))
    out={}
    key=L.keys()
    for i in key:
        if L[i][5]>=minval and L[i][5]<=maxval:
            out[i]=L[i]
    if out=={}:
        print("Their is no Data with the Entered Value")
    else:
        for i in out.keys():
            print(i, "=>", out[i])

def filter_item(L, ch):
    while ch:
        print("Enter the criteria to filter the data on:")
        print("1. Category")
        print("2. Size")
        print("3. Color")
        print("4. Date of Manufacturing")
        print("5. Number of items in the Stock")
        print("6. Price of the Item")
        print("7. Exit")
        ch=int(input("Enter Your choice: "))
        if ch in [1, 2, 3, 4, 5]:
            out={}
            inp=L
            key=L.keys()
            value=input("Enter the value for the data to be filtered with(Case Sensitive): ")
            for i in key:
                if inp[i][ch-1]==value:
                    out[i]=L[i]
            if out=={}:
                print("Their is no Data with the Entered Value")
            else:
                for i in out.keys():
                    print(i, "=>", out[i])
            inp=out
        
        elif ch==6:
            price_range(L)
        elif ch==7:
            break
        Q=input("Do you wish to filter further(F) or exit(E)? (F/E): ")
        if Q=="F" or Q=="f":
            filter_item(out)
        elif Q=="E" or Q=="e":
            break
        else:
            print("Invalid input")

def delete_item():
    print("Article Number => Article Category, Article Size, Article Color, Date of Manufacturing, Number of pieces in Stock, Price")
    display()
    print()
    ArtNum=int(input("Enter the Article Number: "))
    try:
        search_item(ArtNum)
        f=open("database.dat", "rb")
        L=pickle.load(f)
        L.pop(ArtNum)
        f.close()
        f=open("database.dat", "w+b")
        pickle.dump(L, f)
        f.close()
        print("The Entry with the Entered Article Number Has Been Deleted")
        print()
        print("The Updated Database is:")
        print()
        print("Article Number => Article Category, Article Size, Article Color, Date of Manufacturing, Number of pieces in Stock, Price")
        display()
    except:
        print("There is no item with Entered Article Number")


def sale():
    f=open("database.dat", "rb")
    L=pickle.load(f)
    f.close()
    key=L.keys()
    ArtNum=int(input("Enter The Article Number: "))
    try:
        if ArtNum in key:
            L[ArtNum][4]=(L[ArtNum][4]-1)
            f=open("database.dat", "w+b")
            pickle.dump(L,f)
            f.close()
        else:
            raise Exception()
    except:
        print("The Item is out of stock")


def cred_empty():
    try:
        g=open("User.dat", "rb")
        data=pickle.load(g)
        if data=={}:
            g.close()
            return True
        else:
            return False
    except:
        return True
        
        
    
def Logging_in():
    username=(input("Enter your Username: "))
    password=(input("Enter your Password: "))
    try:
        g=open("User.dat", "rb")
        data=pickle.load(g)
        if data[username]==password:
            g.close()
            return True
        else:
            g.close()
            return False
    except:
        g.close()
        return False
def register():
    username=(input("Enter your Username:"))
    password=(input("Enter your Password:"))
    if not cred_empty:
        g=open("User.dat", "rb")
        data=pickle.load(g)
    else:
        data={}
        g=open("User.dat", "w+b")
    data[username]=password
    pickle.dump(data,g)
    g.close()
    print("Succesfully Registered\n\n")  
while True:
    print("\n\n1. Register\n2. Login\n3. Exit")
    ch=int(input("Your Choice: "))
    print("\n")
    if ch==1:
        register()
    elif ch==2:
        if Logging_in():
            f=open("database.dat", "ab")
            f.close()
            while True:
                print()
                print()
                print("Welcome to Clothing and apparel Stock management System")
                print()
                print("Please Choose any operation")
                print("1. Add an Entry")
                print("2. Edit and Existing Entry")
                print("3. Search an Item")
                print("4. Display the Entire Database")
                print("5. Filter the Database")
                print("6. Delete an Entry")
                print("7. Register a Sale")
                print("8. Log out")

                if is_empty():
                    print("WARNING!!! ... !!!The Database Is Empty!!!")
                else:
                    pass

                operation=input("Enter your Choice: ")
                if operation=="1":
                        add_entry()
                elif operation=="2":
                    if is_empty():
                        print("The Database Is Empty")
                    else:
                        edit_item()
                elif operation=="3":
                    if is_empty():
                        print("The Database Is Empty")
                    else:
                        ArtNum=int(input("Enter the Article Number: "))
                        search_item(ArtNum)
                elif operation=="4":
                    if is_empty():
                        print("The Database Is Empty")
                    else:
                        display()
                elif operation=="5":
                    if is_empty():
                        print("The Database Is Empty")
                    else:
                        f=open("database.dat", "rb")
                        L=pickle.load(f)
                        filter_item(L, ch=True)
                        f.close()
                elif operation=="6":
                    if is_empty():
                        print("The Database Is Empty")
                    else:
                        delete_item()
                elif operation=="7":
                    if is_empty():
                        print("The Database Is Empty")
                    else:
                        sale()
                elif operation=="8":
                    break
                else:
                    print("Invalid Input")

        else:
            print("False Login")
    elif ch==3:
        break
    else:
        print("!!!!!! Invalid Input !!!!!!")