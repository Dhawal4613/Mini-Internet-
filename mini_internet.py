#importing required module
import webbrowser as wb

#Giving option to user
print("1. Google\n2. YouTube")

#Creating While loop
while True:
    #Taking input from user
    choose = input("Enter the choice (1 or 2): ")

    if choose == '1':
        query_google = input("Enter your query on Google: ")
        google = wb.open(f'https://google.com/search?q={query_google}')

        if google:
            print("Google is opened, Sir!!")
        else:
            print("Google is not opened, might be there is some ERROR!!")

    elif choose == '2':
        query_youtube = input("Enter your query on YouTube: ")
        youtube = wb.open(f'https://youtube.com/search?q={query_youtube}')

        if youtube:
            print("YouTube is opened, Sir!!")
        else:
            print("YouTube is not opened, might be there is some ERROR!!")

    else:
        print("You entered wrong option. Choose from above option.")
