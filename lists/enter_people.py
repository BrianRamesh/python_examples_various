people_all_data=[]
people_height_list=[]
people_weight_list=[]
people_age_list=[]

while True:
    b=input("enter height, weight, age or enter 0 0 0 to exit:  ")
    a=b.split()

    if(a==['0','0','0']):

        break
    else:
        people_all_data.append(a)
print("the list with the all data of all people height,weight,age is below")
print(people_all_data)
fw= open("people_data.txt","w")
fw.write("the list with the all data of all people height,weight,age is below\n")
fw.write(str(people_all_data))

for x in people_all_data:
    people_height_list.append(float(x[0]))
    people_weight_list.append(int(x[1]))
    people_age_list.append((int(x[2])))

print("\n all peoples height in a list")
print(people_height_list)
fw.write("\n\n all peoples height in a list")
fw.write(str(people_height_list))

print("\n all peoples weight in a list")
print(people_weight_list)
fw.write("\n\n all peoples weight in a list")
fw.write(str(people_weight_list))

print("\n all peoples age in a list")
print(people_age_list)
fw.write("\n\n all peoples age in a list")
fw.write(str(people_age_list))

height_avg=round(sum(people_height_list)/len(people_height_list),2)
print("\n average height of all people is  ")
print(str(height_avg))
fw.write("\n\n average height of all people is  ")
fw.write(str(height_avg))

weight_avg=round(sum(people_weight_list)/len(people_weight_list),2)
print("\n average weight of all people is  ")
print(str(weight_avg))
fw.write("\n\n average weight of all people is  ")
fw.write(str(weight_avg))

age_avg=round(sum(people_age_list)/len(people_age_list),2)
print("\n average age of all people is  ")
print(str(age_avg))
fw.write("\n\n average age of all people is  ")
fw.write(str(age_avg))

