filename = "file.txt"
a = "a"
file = open(filename, a)
checkusername = 0
while checkusername != 4:
    username = input("Username: ")
    username = username.lower()
    numberchar = 0
    checkusername = 0
    charaz = 0
    chartrue = 0
    for char in username:
        numberchar = numberchar + 1
        if numberchar == 1:
            firstusername = char
        if char in "abcdefghigklmnopqrstuvwxyz":
            charaz = charaz + 1
        if char not in "abcdefghigklmnopqrstuvwxyz1234567890.":
            chartrue = chartrue + 1
    if len(username) >= 6 and len(username) <= 30:
        checkusername = checkusername + 1
    else:
        print("Error: Sorry, your username must be between 6 and 30 characters long.")
        continue
    if chartrue == 0:
        checkusername = checkusername + 1
    else:
        print(
            "Error: Sorry, only letters (a-z), number (0-9), and periods (.) are allowed.")
        continue
    if charaz > 0:
        checkusername = checkusername + 1
    else:
        print("Error: Sorry, usernames of 8 or more characters must include at least one alphabetical character (a-z).")
        continue
    if firstusername != ".":
        checkusername = checkusername + 1
    else:
        print("Error: Sorry, the first character of your username must be an ascii letter (a-z) or number (0-9).")
        continue
password = input("Password: ")
file.write(f"Username: {username}\n")
file.write(f"Password: {password}\n")
file.write(f"\n")
file.close
