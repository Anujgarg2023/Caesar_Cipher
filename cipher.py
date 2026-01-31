character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(message,pos):
    out=""
    for i in message:
        if i not in character:
            out+=i
        else:    
            new_char= (character.index(i)+pos)%26
            out+=character[new_char]
    return out   

def decrypt(message,pos):
    out=""
    for i in message:
        if i not in character:
            out+=i
        else:  
            new_char= (character.index(i)-pos)%26
            out+=character[new_char]
    return out

print("Welcome to Caesar Cipher!!")
a="yes"
while(a=="yes"):
    
    todo = input("Type encode to encrypt , type decode to decrypt:\n").lower()
    message = input("Enter message:\n").lower()
    pos = int(input("Enter no of position:\n"))
    if todo =="encode":
        res = encrypt(message,pos)
        print(f"The encoded message is: {res}")
    elif todo == "decode":
        res = decrypt(message,pos)
        print(f"The decoded message is: {res}")
    else:
        print('Wrong input entered')    
    a= input("Do you want to do again, type yes or no:").lower()    
    if a !="yes" and a!="no":
        print("Wrong input entered")
        
        