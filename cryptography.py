"""
cryptography.py
Author: Marcus Hellbe
Credit: None

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
associations1="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
command=str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
while command  not in ["q"]:
    if command not in ["e", "d"]:
        print("Did not understand command, try again.")
    if command =="e":
        primero=input("Message: ")
        message=list(primero)
        llave=input("Key: ")
        key= list(llave)
        for x in range(0, len(message)):
            message[x]=associations.find(message[x])
        for x in range(0, len(key)):
            key[x]=associations.find(key[x])
        while len(key)<len(message):
            key.extend(key)
        ab=[x+y for x,y in zip(message, key)]
        for x in range(0, len(message)):
            bc=associations1[ab[x]]
            print(bc,end="")
        print( )
    if command=="d":
        message1=input("Message: ")
        message=list(message1)
        key1=input("Key: ")
        key= list(key1)
        for x in range(0, len(message)):
            message[x]=associations.find(message[x])
        for x in range(0, len(key)):
            key[x]=associations.find(key[x])
        while len(key)<len(message):
            key.extend(key)
        ab=[x-y for x,y in zip(message, key)]
        for x in range(0, len(message)):
            bc=associations1[ab[x]]
            print(bc,end="")
        print( )
    command=input("Enter e to encrypt, d to decrypt, or q to quit: ")
if command== "q":
        print("Goodbye!")

