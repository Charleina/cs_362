#to run the file please type: python charlene_wang_hw1.py
#it should print out the values

#years for user input
y = input("Enter year: ")
    
    
    
#checking the values in the array to see if they match the criteria for leap years, if they do i will print true and their value if not i will print false and their value (ex. true 2000)
    
if (y % 4) == 0:
    if((y % 100)==0):
        #if it is divisible by 4 and 100 then we must check if it is or is not divisible by 400 because we will get different answers for each
        if(y% 400) == 0:
            print("True %d" % y)
        else:
            print("False %d" % y)
    #if it is not divisible by 100 but is divisible by 4 then it is true for sure.
    else:
        print("True %d" % y)
#if it is not divisible by 4 then it is for sure not a leap year
else:
        print("False %d" % y)
