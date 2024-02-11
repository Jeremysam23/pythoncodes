try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print("%.2f" % result)
    
    mylist = [1,2,3]
    i = int(input("enter index: "))
    print(mylist[i])
    
except ZeroDivisionError:
    print("Denominator cannot be zero. Please try again.")
except ValueError:
    print("Invalid input. Please enter integers only.")
except IndexError:
    print("Index cannot be greater than size of the list.")
