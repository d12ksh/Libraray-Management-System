while True:
    import pandas as pd
    import numpy as np
    import time
    import csv
    import datetime as dt
    
#line print function
    def line():
        print("-----------------------------------------------------------")
    P=print("")
    L=pd.DataFrame(P)
#Date function
    dh = str(dt.datetime.now())
    
    line()
    print("YMCA LIBRARY CLUB,",(dh[:10]))
    line()
#option to enter HOME menu    
    A=input("PRESS '1' TO ENTER OUR DATABASE:-")
    if A=="1":
        line()
        print("Loading...")
        line()
        time.sleep(2)
        print("Welcome to the Library")
        print("---------------HOME OPTIONS are as follows----------------")
        print("Press 1 to see menu for books")
        print("Press 2 to add and retrieve your choice of book")
        print("Press 3 for more queries")
        print("Press 4 for our vision and info")
        print("Press 5 for exit")
        print("----------------------------------------------------------")
        B=input("Your choice:-") 
#option for viewing list of books 
        if B=='1':
            line()
            df = pd.read_csv(r"C:\Users\ahuja\Desktop\Schoolwork\IP CLASS 12\project\Bookname (1).csv")
            print(df)
            line()
            time.sleep(3)
            BB1=input("Enter your NAME:-")
            BB2=input("Enter contact EMAIL:-")
            BB3=int(input("Enter your AGE:-"))
            BB=int(input("Enter desired BOOKCODE for selection:-"))
            
            print("---------NOTE-----------")
            print("1)Issuing of books is LIMITATED to 3 days.")
            print("2)Price is to be CJARGED 20/rs- per issue.")
            print("3)Any damages will lead to a high FINE acc to our POLICY.")
            print("4)A copy of identity DOCUMENT needs to submitted at our desk.")
            print("5)Kindly keep the acknowledged rules in mind -thankyou.")
            print("------------------------")
#option to add final recipt to user            
            KK=input("Press 1 for your final recipt/bill:-")
            if KK=='1':
                line()
                print("Loading...")
                time.sleep(2)
                print("--------------------YMCA LIBRARY-RECIPT--------------------")
                print("Name:-",BB1)
                print("Email:-",BB2)
                print("Age:-",BB3)
                print("Bookcode:-",BB)
                print("Price:-20/-rs")
                print("Issue Date:-",(dh[:10]))
                print("Thankyou -YMCA LIBRARY AND CLUB")
                print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")
                break
#option to add and review a new book            
        if B=='2':
            line()
            print("ENTER FOLLOWING DETAILS TO ADD A BOOK")
            D=input("BOOK NAME:-")
            E=input("AUTHOR:-")
            line()
            print("WAIT....Your query is processing")
            time.sleep(4)
#option for recipt same as above
            print("------------------------FINAL RECIPT------------------------")
            print("BOOK CODE:- 025")
            print("ISBN:- 2PGDT53FFSG55")
            print("BOOK NAME:-",D)
            print("AUTHOR:-",E)
            print("PRICE:- RS25/-")
            print("------------------------------------------------------------")
            print("Your added item will be available shortly in 2-3 business days.")
            print("Sorry for the inconvenience caused.")
            line()
            print("Thankyou -YMCA LIBRARY AND CLUB")
            print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")
            break
#option to review queries
        if B=='3':
            print("----------------------YMCA LIBRARY AND CLUB----------------------")
            print("Help desk is welcomed")
            H=input("Enter your email:")
            G=input("kindly mention your queries or problems here=")
            print("Your feedback is appreciated, response will asap to your registered id.")
            line()
            print("Loading...")
            time.sleep(2)
            line()
            print("CONTACT INFO:")
            print("OUR EMAIL-ymcalib12@gmail.com")
            print("Phn-9099334264/9099190911")
            print("MON-SUN_8AM-9PM")
            print("Thank you for having us -YMCA LIBRARY AND CLUB")
            print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")
            break
#option for displaying information about YMCA library
        if B=='4':
            print("----------------------YMCA LIBRARY AND CLUB----------------------")
            print("The Central Library and Audiovisual Services have the basic responsibility of providing the collection resources and services to the students and faculty./nIn line with the mission statement of the institution in which the library organization is an integral part and as an intellectual resource of the academic community, the following are the vision of the Library.")
            line()
            print("Loading..")
            line()
            time.sleep(3)
            print("OUR VISON:")
            print("As YMCA moves towards its goal of achieving prominence as a leading libraries in this part of the country, 'It is the vision of the Library to support the institution and its stakeholder by providing seamless access to the widest possible spectrum of information resources such as digital, online databases, print and non-print materials relevant to the curricular, informational and innovative research needs of the academic community', means to provide Right Information to the Right Users at the Right Time and in the Right Format")
            line()
            print("Address: Sector21,Victoria park,CP,Ahmedabad-380031")
            print("CONTACT INFO:")
            print("OUR EMAIL-ymcalib12@gmail.com")
            print("Phn-9099334264/9099190911")
            print("MON-SUN_8AM-9PM")
            print("Thank you for having us -YMCA LIBRARY AND CLUB")
            print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")
            break
        if B=='5':
            print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")
            break
            
#option to display incase of false input data            
    else:
        line()
        print("***ERROR***")
        print("REVERT BACK")
        print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")
        break
