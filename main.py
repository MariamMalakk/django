
# ----------name validation-----------------
def reg():
    while True:
            fname=input("enter your first name: ")
            lname = input("enter your last name: ")
            if not (fname.isalpha() and lname.isalpha()):
                print("not valid name")
            elif len(fname) < 3 and len(lname):
                print("not valid name")
                continue
            else:
               break
    # ---------------mail validation-----------------
    while True:
        mail = input("enter your email: ")
        if not (mail.__contains__('@') and mail.__contains__('.com')):
            print('mail not valid')
            continue
        else:
            break

    # --------------------password confirmation-------------
    while True:
        passw = input("enter your password :")
        if len(passw) < 5:
            print('Password too short')
            continue

        confpass = input("confirm your password: ")
        if confpass == passw:

            break
        else:
            print("password is not match")



    while True:
         mphone = input("enter your phone number: ")
         if not mphone.isdigit():
            print("not valid number")
            continue
         else:
            break

    userinfo = f"{fname}:{lname}:{mail}:{passw}:{mphone}\n"
    try:
        fileobj=open("userinfo.txt",'a')
    except Exception as e:
        print(e)
    else:
        fileobj.write(userinfo)
        fileobj.close()

def login():
    user_name = input("enter your name:")
    password = input("enter your password:")
    fileobj = open("userinfo.txt", "r")
    # users = fileobj.readlines()
    # print(users)
    for i in fileobj:
         userinfo = i.strip("\n")
         userinfo = i.split(":")
         if (userinfo[0]==user_name and userinfo[3]==password):
             print("logged in ")
             break
         else:
             print("wrong user")


reg()
login()

# s=reg()
# print(s)
# m=login()
# print(m)





















# while True:
#     try:
#         mphone = input("enter your phone number: ")
#     except Exceptionas as e:
#       if len(mphone) < 11:
#         print(e)
#         continue
#
#       else:
#          print("true")
#          break
# while True:
#     mphone = input("enter your phone number: ")
#     try:
#         n1 = int(mphone)
#
#         break
#     except ValueError:
#         print("It has to be 11 numbers")




