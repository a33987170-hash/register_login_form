
def menu():
    while True:
    
        print("1. Реєстрація ")
        print("2. Вхід ")
        print("0 завершити програму ")

        action = int(input("виберіть дію "))
        
        if action == 1:
            print("*****Registration*****")
            email = input("email ")
            password = input("password ")
            confirmed_password = input("confirmation password ")
            if password == confirmed_password:
                with open("data_users.txt", "a", encoding ="utf-8") as file:
                    file.write(f"{email}:{password}\n")

                print("registration is over")
                break
            else:
                print("password not math with confirmed password ") 


        if action ==2:
            print("******entrance*******")
            email = input("email ")
            password  =  input("password ")
            login_succes = False
            with open("data_users.txt" ,"r", encoding="utf-8" ) as file:
                    for line in file:
                        line = line.strip()
                        if not line :
                            continue
                        file_email, file_password =line.split(":",1)    

                        if  file_email == email and file_password == password:
                            login_succes = True
                            break

            if  login_succes == True:
                print("entrance is done")  
            else:
                print("wrong email or password")
                        

        if action == 0:
            break

    

menu()


    


