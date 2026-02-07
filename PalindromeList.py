List=[1,2,3,2,1]

copy_list=List.copy()

copy_list.reverse()

if List==copy_list:
    print("The list is a palindrome.")  
else:
    print("The list is not a palindrome.")  
