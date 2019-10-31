import sqlite3

conn = sqlite3.connect("newdata.db")

#conn.execute("CREATE TABLE information (name text , address text , phone int)")

while(True):
    print("1 INSERT DATA")
    print("2 PRINT DATA")
    print("3 UPDATE ADDRESS")
    print("4 UPDATE NAME")
    print("5 DELETE RECORD")
    print("6 EXIT")

    ch = int(input("Enter your choice"))

    if(ch==1):
        name = input("Enter a name : ")
        address = input("Enter a address : ")
        phone = int(input("Enter mobile number : "))
        conn.execute("INSERT INTO information (name , address , phone) VALUES (?,?,?)" , (name , address , phone))
        conn.commit()
    elif(ch==2):
        cursor = conn.execute("SELECT * FROM information")
        for i in cursor:
            print(f"name is : " , i[0])
            print(f"address is : " , i[1])
            print("phone number is : " , i[2])
            print("\n\n")
    elif (ch==3):
        new_address = input("Enter new address : ")
        name = input("user name : ")
        conn.execute("UPDATE information set address = ? WHERE name = ?" , (new_address , name))
        conn.commit()
    elif(ch==4):
        new_name = input("Enter a new name : ")
        address = input("Enter user address : ")
        conn.execute("UPDATE information set name = ? WHERE address = ?" , (new_name , address))
        conn.commit()
    elif(ch==5):
        name = input("Enter a name which you want a delete into the table : ")
        conn.execute("DELETE FROM information where name = ?" , (name,))
        conn.commit()
    else:
        break

