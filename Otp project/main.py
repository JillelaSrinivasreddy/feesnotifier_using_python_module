import feepending
import feepaid
import otp

admin_username = input("Enter User name: ")
if admin_username == "admin":
    otp_code = otp.send_otp("jsrinivasreddy350@gmail.com")  
    x = int(input("Enter OTP: "))
    if x == otp_code:
        print("Login Success!")
    else:
        print("Login Failed!")
        exit()
else:
    print("Invalid Username")
    exit()

# Fixing the structure of the userdetails dictionary
userdetails = {
    101: ["srinivas", "210303124515@paruluniversity.ac.in", False],  
    102: ["Shashi", "shashi2028j@gmail.com", False],  
    103: ["Manohar", "reddymanohar894@gmail.com", True],
    104: ["Nihin", "nithishkumarbollapelli@gmail.com", False],
    105 : ["Sahithi","cherukurisahithi486@gmail.com","true"]
}

print("Welcome Admin")

while True:
    print("Choose your Option")
    print("1. Edit Information")
    print("2. Send mail to Fee Pending users")
    print("3. Send mail to Fee Cleared users")
    print("4. Exit")
    
    x1 = int(input("Enter option: "))
    
    if x1 == 1:
        
        for user in userdetails:
          if not userdetails[user][2]:  
                status = input(f"Enter the Status of {userdetails[user][0]} (True/False): ").lower()
                
                userdetails[user][2] = status == "true"
                print(f"{userdetails[user][0]} Data Updated!")
        print("Data Edited")
    
    elif x1 == 2:
        res = []
        for user in userdetails:
            if not userdetails[user][2]:  
                res.append([userdetails[user][0], userdetails[user][1]])
        feepending.send_mails(res)
        print("All mails sent to Fee pending users")
    
    elif x1 == 3:
        res = []
        for user in userdetails:
            if userdetails[user][2]:  
                res.append([userdetails[user][0], userdetails[user][1]])
        feepaid.send_mails(res)
        print("All mails sent to Fee Cleared users!")
    
    else:
        print("Thank You")
        print("Visit again")
        break
