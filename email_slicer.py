def email_slicer():
    print("Welcome to email slicer")

    email = input("enter email address: ")

    (username,domain) = email.split("@")
    (domain,extension) = domain.split(".")

    print("")
    print("username: ",username)
    print("domain:",domain)
    print("extension: ",extension)
    print(" ")

while(True):
    email_slicer()