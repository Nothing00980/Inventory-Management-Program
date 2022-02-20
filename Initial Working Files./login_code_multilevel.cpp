#include <iostream>
#include <string>
#include <fstream>

using namespace std;
template <class t>
class user{
 t username;
 t password;

 protected:
  int userid;
  int userage;

  public:
   user(t x,t pass){
       username  = x;
       password = pass;
   }
   void getdata(){
   
       cout<<"Enter your id:\n ";
       cin>>userid;
       cout<<"Enter your age:\n";
       cin>>userage;
   }
   void displaydata(){
       ofstream file;
        file.open(username + ".txt");
       file<<username<<endl<<password<<endl<<userid<<endl<<userage;
   }
   bool checklogging(){

       t username,password,pw,un;
       cout<<"Enter username: \n";
       cin>>username;
       cout<<"Enter password: \n";
       cin>>password;

    ifstream file;
    file.open(username + ".txt");
        getline(file,un);
        getline(file,pw);

       if(username == un && password == pw){
           return true;
       }
       else{
           return false;
       }
   }
};
int main(){
    int choice;
    cout<<"1.Register\n2.Login\n Your choice: "<<endl;
    cin>>choice;

    if(choice==1){
        string username,password;
        cout<<"Enter username: "<<endl;
        cin>>username;
        cout<<"Enter password\n ";
        cin>>password;

        user<string> no1(username,password);
        ofstream file;
        file.open(username + ".txt");
        file<<username<<endl<<password;
        no1.getdata();
        no1.displaydata();
        file.close();
        cout<<"Congrtualtions you have successfully registered!!"<<endl;
        system("PAUSE");
        main();
    }
    else if(choice==2)
    { string username,password;
        user<string> no1(username,password);
       bool z  =  no1.checklogging();
        if(!z){
            cout<<"False login!!"<<endl;
            system("PAUSE");
            return 0;
        }
        else{
            cout<<"Successfully logged in!!"<<endl;
            system("PAUSE");
            return 1;
        }
    }    
    return 0;
}