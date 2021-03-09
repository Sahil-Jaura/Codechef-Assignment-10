n=int(input())
arr=[]
# TAKE INPUT OF STUDENT'S NAME AND MARKS
for i in range(n):
    x=[]
    name=input()
    x.append(name)
    marks=int(input())
    x.append(marks)
    arr.append(x)
# --------------------------------------
# FINDING THE LOWEST MARKS 
minimum_marks=arr[0][1]
for i in range(n):
    if minimum_marks>arr[i][1]:
        minimum_marks=arr[i][1]
# --------------------------------------  
# DELETING THE STUDENT WHO HAS LOWEST MARKS       
new_arr=[]
for i in arr:
    if i[1]!=minimum_marks:
        new_arr.append(i)
# ----------------------------------------
# FINDING THE STUDENTS WITH SECOND LOWEST MARKS
final_arr=[]
second_least_grade=new_arr[0][1]
for i in new_arr:
    if i[1]<second_least_grade:
        second_least_grade=new_arr[1]
for i in new_arr:
    if i[1]==second_least_grade:
        final_arr.append(i)
# -----------------------------------------
# SORTING THE NAMES
name_list=[]
for i in final_arr:
    name_list.append(i[0])
name_list.sort()
for i in name_list:
    print(i)