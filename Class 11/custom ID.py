l=[]
i=0
n=int(input("ENTER THE NUMBER OF CUSTOMERS:"))
for i in range (n):
	na=str(input("ENTER THE NAME OF CUSTOMER:"))
	nu=int(input("ENTER CUSTOMER ID:"))
	l.append([na,nu])
opt=str(input("DO YOU WANT DO DELETE ANY CUSTOMER ID??"))
if (opt=='no' or opt=='NO'):
    print('THANK YOU FOR YOUR COOPERATION!!!')
elif (opt=='yes' or opt=='YES'):
    dnu=int(input("PLEASE ENTER CUSTOMER ID THAT IS TO BE DELETED:"))
    for i in range (n):
        if dnu==l[i][1]:
            del(l[i])
            print("THE CUSTOMER ID HAS BEEN DELETED.")
            print("HERE IS THE LIST ......",l,sep='')
        else:
            print("THIS CUSTOMER ID DOES NOT EXIST. PLEASE CHECK THE GIVEN CUSTOEMR ID.")
 
