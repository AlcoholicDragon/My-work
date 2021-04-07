def validate(dd,mm,yy):
    l=[1,3,5,7,8,10,12]
    if (dd <= 31 and dd != 0 and mm <= 12):
        if (mm==2 and yy%4==0 and dd<=29):
            print("DATE IS VALID.")
            if (dd == 29):
                dd=1
                mm=3
                print("The next date is ",dd,"/",mm,"/",yy,".",sep="")
            else:
                dd+=1
                print("The next date is ",dd,"/",mm,"/",yy,".",sep="")
        elif (mm==2 and yy%4!=0 and dd<=28):
            print("DATE IS VALID.")
            if (dd == 28):
                dd=1
                mm=3
                print("The next date is ",dd,"/",mm,"/",yy,".",sep="")
            else:
                dd+=1
                print("The next date is ",dd,"/",mm,"/",yy,".",sep="")
        elif (mm in l and dd<=31):
            print("DATE IS VALID.")
            if (dd == 31 and mm == 12):
                dd=1
                mm=1
                yy+=1
                print("The next date is ",dd,"/",mm,"/",yy,".",sep="")
            elif (dd == 31):
                dd=1
                mm+=1
                print("The next date is ",dd,"/",mm,"/",yy,".",sep="")
            else:
                dd+=1
                print("The next date is ",dd,"/",mm,"/",yy,".",sep='')
        elif (mm not in l and mm != 2 and dd<=30):
            print("DATE IS VALID")
            if (dd == 30):
                dd=1
                mm+=1
                print("The next date is ",dd,"/",mm,"/",yy,".",sep="")
            else:
                dd+=1
                print("The next date is ",dd,"/",mm,"/",yy,".",sep="")
        else:
            print("DATE IS INVALID.")
    else:
        print ("DATE IS INVALID.")
