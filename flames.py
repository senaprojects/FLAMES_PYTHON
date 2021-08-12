#SIMPLE FLAMES GAME IN PYTHON!! 

#getting input from user and convert them into lower.
name1=input("Enter the name : ").lower()
name2=input("Enter the second name : ").lower()

#replace the space in the input names.
name1= name1.replace(" ","")
name2= name2.replace(" ","")

#to find the common charecters in input replace with space.   
for i in name1:
     for j in name2:
          if(i==j):
              name1= name1.replace(i,"",1)
              name2= name2.replace(j,"",1)
#print(name1)
#print(name2)
#to concodenate the two different names which are already removed by common charecters.
length=name1+name2
count=len(length)

#print(count)
#to check the given to names are different.
if count>0:
     l=["Friends","Love","Affection","Marriage","Enemies","Siblings"]

#to find the relationship.
     while len(l)>1:
          count1=count%len(l)
          sindex=count1-1
          if(sindex>=0):
               left_slice=l[:sindex]
               right_slice=l[sindex+1:]
               l=right_slice+left_slice
          else:
               l=l[:len(l)-1]
     print("Relationship is : ",l[0])             
              


          


