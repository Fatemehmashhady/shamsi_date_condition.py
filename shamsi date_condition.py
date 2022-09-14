
#date based on day number

daynum=int(input("enter your number: "))

month=0
day=0

if 0<daynum<=186:
    month=(daynum//31)+1                        #month counter
    day=daynum%31                               #day counter

elif 186<daynum<=365:
    daynum-=186
    month=(daynum%30)+1+6                       #month counter
    day=daynum%30                               #day counter

else:
    print("the date number is out of range!")

print("today is: ",month,".",day)