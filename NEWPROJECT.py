import pandas as pd
import matplotlib.pyplot as pl
while True:
    print('\n')
    print('***********************************************')
    print('**************DELL SHOPPING STORE**************')
    print('***List of Dell Products***')
    print('1. Display the List of Laptops')
    print('2. Display the alist oof Desktops')
    print('===============================================')
    print('***Dell Products Data Visualisation***')
    print('3. Display Laptops Data using Line Graphs')
    print('4. Display Laptops Data using Bar Graphs')
    print('5. Display Deskttops Data using Linne Graphs')
    print('6. Display Desktops Data using Bar Graphs')
    print('===============================================')
    print('***Data Manipulation***')
    print('7. Inserting a new product record')
    print('8. Deleting a product record')
    print('9. Updating a product record')
    print('10. Searchng a record')
    print('11. Arrange the product data accordingly')
    print('12. Readd top and bottom records from file as required')
    print('13. Make a copy of CSV file')
    print('14. Exit')
    print('***********************************************')
    ch=input('Enter Your Choice :')
    if ch=='1':
        print('Reading laptop data From CSV file')
        df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\laptop (1).csv")
        print(df)
    elif ch=='2':
        print('Reading desktop data from CSV file')
        df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\desktop.csv")
        print(df)
    elif ch=='3':
        df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\laptop (1).csv")
        name=df['Name']
        qn=df['Quantity']
        pr=df['Price']
        ra=df['Ratings']
        pl.xlabel('Laptop Name')
        pl.xticks(rotation=30)
        print('Select specific line chart as given below:')
        print('Press 1 to print te data for Laptops vs Quantity')
        print('Press 2 to print the data for Laptops vs Price')
        print('Press 3 to print the data for Laptops vs Ratings')
        op=int(input('Enter your choice:'))
        if op==1:
            pl.ylabel('Quantity')
            pl.title('*** Laptops vs Quantity***')
            pl.yticks(range(0,50,5))
            pl.ylim(0,50,5)
            pl.plot(name,qn,marker='d')
            pl.show()
        elif op==2:
            pl.ylabel('Price')
            pl.title('*** Laptops vs Price***')
            pl.yticks(range(25000,150000,20000))
            pl.ylim(10000,150000,20000)
            pl.plot(name,pr,marker='h')
            pl.show()
        elif op==3:
            pl.ylabel('Rating(out of 5)')
            pl.title('*** Laptops vs Ratings***')
            pl.yticks(range(0,6,1))
            pl.ylim(0,6)
            pl.plot(name,ra,marker='*')
            pl.show()
        else:
            print('Enter a valid input')
    elif ch=='4':
        df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\laptop (1).csv")
        name=df['Name']
        qn=df['Quantity']
        pr=df['Price']
        ra=df['Ratings']
        pl.xlabel('Laptop Name')
        pl.xticks(rotation=30)
        print('Select specific bar chart as given below:')
        print('Press 1 to print te data for Laptops vs Quantity')
        print('Press 2 to print the data for Laptops vs Price')
        print('Press 3 to print the data for Laptops vs Ratings')
        op=int(input('Enter your choice:'))
        if op==1:
            pl.ylabel('Quantity')
            pl.title('*** Laptops vs Quantity***')
            pl.yticks(range(0,50,5))
            pl.ylim(0,50,5)
            pl.bar(name,qn)
            pl.show()
        elif op==2:
            pl.ylabel('Price')
            pl.title('*** Laptops vs Price***')
            pl.yticks(range(25000,150000,20000))
            pl.ylim(10000,150000,20000)
            pl.bar(name,pr)
            pl.show()
        elif op==3:
            pl.ylabel('Rating(out of 5)')
            pl.title('*** Laptops vs Ratings***')
            pl.yticks(range(0,6,1))
            pl.ylim(0,6)
            pl.bar(name,ra)
            pl.show()
        else:
            print('Enter a valid input')
    elif ch=='5':
        df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\desktop.csv")
        name=df['Name']
        qn=df['Quantity']
        pr=df['Price']
        ra=df['Ratings']
        pl.xlabel('Desktop Name')
        pl.xticks(rotation=30)
        print('Select specific line chart as given below:')
        print('Press 1 to print te data for Desktop vs Quantity')
        print('Press 2 to print the data for Desktop vs Price')
        print('Press 3 to print the data for Desktop vs Ratings')
        op=int(input('Enter your choice:'))
        if op==1:
            pl.ylabel('Quantity')
            pl.title('*** Desktop vs Quantity***')
            pl.yticks(range(0,50,5))
            pl.ylim(0,50,5)
            pl.plot(name,qn,marker='d')
            pl.show()
        elif op==2:
            pl.ylabel('Price')
            pl.title('*** Desktop vs Price***')
            pl.yticks(range(25000,150000,20000))
            pl.ylim(10000,150000,20000)
            pl.plot(name,pr,marker='h')
            pl.show()
        elif op==3:
            pl.ylabel('Rating(out of 5)')
            pl.title('*** Desktop vs Ratings***')
            pl.yticks(range(0,6,1))
            pl.ylim(0,6)
            pl.plot(name,ra,marker='*')
            pl.show()
        else:
            print('Enter a valid input')
    elif ch=='6':
        df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\desktop.csv")
        name=df['Name']
        qn=df['Quantity']
        pr=df['Price']
        ra=df['Ratings']
        pl.xlabel('Desktop Name')
        pl.xticks(rotation=30)

        print('Select specific bar chart as given below:')
        print('Press 1 to print te data for Desktop vs Quantity')
        print('Press 2 to print the data for Desktop vs Price')
        print('Press 3 to print the data for Desktop vs Ratings')
        op=int(input('Enter your choice:'))
        if op==1:
            pl.ylabel('Quantity')
            pl.title('*** Desktop vs Quantity***')
            pl.yticks(range(0,50,5))
            pl.ylim(0,50,5)
            pl.bar(name,qn)
            pl.show()
        elif op==2:
            pl.ylabel('Price')
            pl.title('*** Desktop vs Price***')
            pl.yticks(range(25000,150000,20000))
            pl.ylim(10000,150000,20000)
            pl.bar(name,pr)
            pl.show()
        elif op==3:
            pl.ylabel('Rating(out of 5)')
            pl.title('*** Desktop vs Ratings***')
            pl.yticks(range(0,6,1))
            pl.ylim(0,6)
            pl.bar(name,ra)
            pl.show()
        else:
            print('Enter a valid input')
    elif ch=='7':
        print('Insert New Data in a CSV File')
        print('Press 1 to insert data of Laptop')
        print('Press 2 to insert data of Desktop')

        ch=int( input('Enter yout CSV choice:')
               if ch==1:
            
               df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\laptop (1).csv",index_col="S.No.")
               a=int(input("Enter unique serial no. :"))
               b=input("Enter laptop name:")
               c=input("Enter specifications:")
               d=int(input("Enter quantity of laptops:"))
               e=int(input("Enter prrice of laptop:"))
               f=float(input("Enter rating of laptop:")
                       df.loc[a]=[b,c,d,e,f]
                       df.to_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\laptop (1).csv")
                       print()
                       print(df)
                       print()
                       print("New laptop details added.")
               elif ch==2:
                   df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\desktop.csv",index_col="S.No.")
                   a=int(input("Enter unique serial no. :"))
                   b=input("Enter desktop name:")
                   c=input("Enter specifications:")
                   d=int(input("Enter quantity of desktops:"))
                   e=int(input("Enter prrice of desktop:"))
                   f=float(input("Enter rating of desktop:")
                           df.loc[a]=[b,c,d,e,f]
                           df.to_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\desktop.csv")
                           print()
                           print(df)
                           print()
                           print("New desktop details added.")
               else:
                   print('Enter a valid choice.')
    elif ch=='8':
        print('Delete the data from a CSV file.')
        print('Press 1 to delete laptop data')
        print('Press 2 to delete desktop data')

        ch=int(input('Enter your CSV choice:'))
        if ch==1:
            df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\laptop (1).csv",index_col="S.No.")
            a=int(input('Enter S.No. :'))
            df.drop(a,inplace=True)
            df.to_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\laptop (1).csv")
            print()
            print(df)
            print()
            print("Laptop details removed.")
        elif ch==2:
            df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\desktop.csv",index_col="S.No.")
            a=int(input('Enter S.No. :'))
            df.drop(a,inplace=True)
            df.to_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\desktop.csv")
            print()
            print(df)
            print()
            print("Desktop details removed.")
        else:
            print("Enter valid choice:")
    elif ch=='9':
        print('Update data in a CSV file.')
        print('Press 1 to update laptop data.')
        print('Press 2 to update desktop data.')

        ch=int(input('Enter your CSV choice:')
        if ch==1:
               df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\laptop (1).csv",index_col="S.No.")
               a=int(input("Enter S.No. :"))
               print("Current laptop name is:",df.loc[a,"Name"])
               df.loc[a,"Name"]=input("Enter new laptop name:")
               print("Current specification is:",df.loc[a,"Specification"])
               df.loc[a,"Specification"]=input("Enter new specification:")
               print("Current quantity is:",df.loc[a,"Quantity"])
               df.loc[a,"Quantity"]=int(input("Enter new quantity of laptops:"))
               print("Current price of laptop is:",df.loc[a,"Price"])
               df.loc[a,"Price"]=int(input("Enter new price of laptop:"))
               print("Current rating of laptop is:",df.loc[a,"Ratings"])
               df.loc[a,"Ratings"]=float(input("Enter new rating of laptop:"))
               df.to_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\laptop (1).csv")
               print()
               print(df)
               print()
               print("Laptop details updated.")
        elif ch==2:
            df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\desktop.csv",index_col="S.No.")
            a=int(input("Enter S.No. :"))
            print("Current desktop name is:",df.loc[a,"Name"])
            df.loc[a,"Name"]=input("Enter new desktop name:")
            print("Current specification is:",df.loc[a,"Specification"])
            df.loc[a,"Specification"]=input("Enter new specification:")
            print("Current quantity is:",df.loc[a,"Quantity"])
            df.loc[a,"Quantity"]=int(input("Enter new quantity of desktops:"))
            print("Current price of desktop is:",df.loc[a,"Price"])
            df.loc[a,"Price"]=int(input("Enter new price of desktop:"))
            print("Current rating of desktop is:",df.loc[a,"Ratings"])
            df.loc[a,"Ratings"]=float(input("Enter new rating of desktop:"))
            df.to_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\desktop.csv")
            print()
            print(df)
            print()
            print("Desktop details updated.")
        else:
            print("Enter valid choice.")
            
    elif ch=='10':
        while True:
            print()
            print('Search a specific record.')
            print('Press 1 to search laptop by S.No. .')
            print('Press 2 to search laptop by Name.')
            print('Press 3 to search desktop by S.No. .')
            print('Press 4 to search desktop by Name.')
            print('Press 5 to exit to main menu.')
            op=int(input("Enter your choice: ")
            if op==1:
                   df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\laptop (1).csv",index_col="S.No.")
                   a=int(input("Enter S.No. :"))
                   print(df.loc[a])
            elif op==2:
                df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\laptop (1).csv",index_col="Name")
                a=input("Enter laptop name :")
                print(df.loc[a])
            elif op==3:
                df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\desktop.csv",index_col="S.No.")
                a=int(input('Enter S.No. :'))
                print(df.loc[a])
            elif op==4:
                df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\desktop.csv",index_col="Name")
                a=input('Enter desktop name:')
                print(df.loc[a])
            else:
                break
                      
    elif ch=='11':
        print('Arrange the data of CSV file.')
        print('Press 1 to arrange data of laptop CSV file.')
        print('Press 2 to arrange data of desktop CSV file.')

        ch=int(input('Enter your CSV choice:'))
        if ch==1:
            df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\laptop (1).csv")
            print('Press 1 to arrange the laptop data as per Name')
            print('Press 2 to arrange the laptop data as per Quantity')
            print('Press 3 to arrange the laptop data as per Price')
            print('Press 4 to arrange the laptop data as per Rating')

            op=int(input("Enter your choice:"))
            if op==1:
                df1=df.sort_values(['Name'])
                print()
                print(df1)
            elif op==2:
                df1=df.sort_values(['Quantity'])
                print()
                print(df1)
            elif op==3:
                df1=df.sort_values(['Price'])
                print()
                print(df1)
            elif op==4:
                df1=df.sort_values(['Rating'])
                print()
                print(df1)
            else:
                print('Enter valid input.')
        elif ch==2:
            df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\desktop.csv")
            print('Press 1 to arrange the desktop data as per Name')
            print('Press 2 to arrange the desktop data as per Quantity')
            print('Press 3 to arrange the desktop data as per Price')
            print('Press 4 to arrange the desktop data as per Rating')

            op=int(input("Enter your choice:"))
            if op==1:
                df1=df.sort_values(['Name'])
                print()
                print(df1)
            elif op==2:
                df1=df.sort_values(['Quantity'])
                print()
                print(df1)
            elif op==3:
                df1=df.sort_values(['Price'])
                print()
                print(df1)
            elif op==4:
                df1=df.sort_values(['Rating'])
                print()
                print(df1)
            else:
                print('Enter valid input.')
        else:
            print('Enter valid input.')
            
    elif ch=='12':
        df1=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\laptop (1).csv",index_col=0)
        df2=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\desktop.csv",index_col=0)

        t=int(input('How many records to display from the top?'))
        b=int(input('How many records to display from the bottom?'))

        print('First',t,'Records')
        print()
        print(df1.head(t))
        print()
        print(df2.head(t))
        print('\nLast',b,'Records')
        print()
        print(df1.tail(b))
        print()
        print(df2.tail(b))
        print()
    elif ch=='13':
        print('Duplicate the file with a new CSV file')
        print('Press 1 to duplicate laptop CSV file')
        print('Press 2 to duplicate desktop CSV file')

        op=int(input('Enter your choice:'))
        if op==1:
            df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\laptop (1).csv")
            df.to_csv("C:\Users\A\OneDrive\Desktop\PROJECT\laptopdupe.csv")
            print('Data from the new file')
            print()
            print(df)
            print()
        elif op==2:
            df=pd.read_csv("C:\\Users\\A\\OneDrive\\Desktop\\PROJECT\\desktop.csv")
            df.to_csv("C:\Users\A\OneDrive\Desktop\PROJECT\desktopdupe.csv")
            print('Data from the new file')
            print()
            print(df)
            print()
        else:
            print('Enter a valid input:')

    elif ch=='14':
        break
    else:
        print('\n***Enter a valid input***')
               

        
            





            
                

               
               
        
            
            
            
            
        
        
        
        
            
        
        
        
    
    
