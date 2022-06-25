#Create a list
first_list = []
#Input the list by using append
first_list.append("S3") 
first_list.append("Lambda")
first_list.append("EC2")
#print List and separate it by a coma
print(*first_list, sep= ",")


#count the length and print the count
length_list = len(first_list)
print("The length of the list is: ",length_list)

