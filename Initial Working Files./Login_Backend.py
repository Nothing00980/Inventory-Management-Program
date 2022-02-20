import pickle
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
    username=(input("Enter your Username"))
    password=(input("Enter your Password"))
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
    print("\n\n1.register\n2.Login")
    ch=int(input("Your Choice: "))
    print("\n")
    if ch==1:
        register()
    if ch==2:
        if Logging_in():
            pass
        else:
            print("False Login")
