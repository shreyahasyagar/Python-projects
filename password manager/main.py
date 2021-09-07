
from cryptography.fernet import Fernet


'''def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key) '''

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key
    


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())




#key+password+text_to_encrypt=random_text
#random_text+key+password=text_to_encrypt
    

    

def add():
    name= input("Account Name: \n")
    pwd= input("Password: \n")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



while(True):    
    mode= input("Would you like to add a new password or view existing ones (view or add), press q to quit\n").lower()
    
    if mode =='q':
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid mode")
        continue
