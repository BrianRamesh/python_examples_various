import  heapq
class Cubes:
    def __init__(self,x=1):
        self.my_length=x

    def volume(self):
        self.my_volume =self.my_length*self.my_length*self.my_length
        return self.my_length*self.my_length*self.my_length
    def area(self):
        self.my_area = self.my_length*self.my_length*6
        return  self.my_length*self.my_length*6
fw=open("cube_data.txt","w")
cube1=Cubes(5)
print("cube1 area, volume")
fw.write("cube1 area, volume\n")
print(cube1.area())
print(cube1.volume())
fw.write(str(cube1.area())+"\n")
fw.write(str(cube1.volume())+"\n")
print("")
fw.write("\n")

print("cube2 area, volume")
fw.write("cube2 area, volume\n")
cube2=Cubes()
print(cube2.area())
print(cube2.volume())
fw.write(str(cube2.area())+"\n")
fw.write(str(cube2.volume())+"\n")
print("")
fw.write("\n")

print("cube3 area, volume")
fw.write("cube3 area, volume\n")
cube3=Cubes(4)
print(cube3.area())
print(cube3.volume())
fw.write(str(cube3.area())+"\n")
fw.write(str(cube3.volume())+"\n")
print("")
fw.write("\n")

print("cube4 area, volume")
fw.write("cube4 area, volume\n")
cube4=Cubes(9)
print(cube4.area())
print(cube4.volume())
fw.write(str(cube4.area())+"\n")
fw.write(str(cube4.volume())+"\n")
print("")


volume_list=[cube1.my_volume,cube2.my_volume,cube3.my_volume,cube4.my_volume]
area_list = [cube1.my_area,cube2.my_area,cube3.my_area,cube4.my_area]
length_list = [cube1.my_length,cube2.my_length,cube3.my_length,cube4.my_length]
print("")
print("lengths of all cubes in list")
fw.write("\n")
fw.write("lengths of all cubes in list\n")
for x in length_list:
    print(x)
    fw.write(str(x)+"\n")

print("")
print("areas of all cubes in list")
fw.write("\n")
fw.write("areas of all cubes in list\n")
for x in area_list:
    print(x)
    fw.write(str(x)+"\n")

print("")
print("volume of all cubes in list")
fw.write("\n")
fw.write("volume of all cubes in list\n")
for x in volume_list:
    print(x)
    fw.write(str(x)+"\n")
print("")
print("the biggest cube has length: ",max(length_list))
fw.write("\n")
fw.write("the biggest cube has length: "+str(max(length_list))+"\n")

print("")
print("the length of the two biggest cubes as a list: ",heapq.nlargest(2,length_list))
fw.write("\n")
fw.write("the length of the two biggest cubes as a list: "+str(heapq.nlargest(2,length_list))+"\n")
fw.close()

fr= open("cube_data.txt","r")
file_str=fr.read()
print()
print()
print("now we are reading  the data from the file")
print(file_str)
fr.close()

#inheritance
class Advanced_cube(Cubes):
    def __init__(self,x,c):
        self.my_length=x
        self.my_color=c
        self.my_area=0


adv_cube1=Advanced_cube(13,'red')

print("inheritance and creation of class Advanced Cube")
print("\n the color, length, area, volume of cube 1 is listed below:")
print(adv_cube1.my_color)
print(adv_cube1.my_length)
print(str(adv_cube1.area()))
print(str(adv_cube1.volume()))

fw_adv= open("advanced_cube_data.txt",'w')
print("inheritance and creation of class Advanced Cube")
print("\n the color, length, area, volume of cube 1 is listed below:")
print(adv_cube1.my_color)
print(adv_cube1.my_length)
print(str(adv_cube1.area()))
print(str(adv_cube1.volume()))

fw_adv.write('inheritance and creation of class Advanced Cube')
fw_adv.write("\nthe color, length, area, volume of cube 1 is listed below:\n")
fw_adv.write(str(adv_cube1.my_color)+"\n")
fw_adv.write(str(adv_cube1.my_length)+"\n")
fw_adv.write(str(adv_cube1.area())+"\n")
fw_adv.write(str(adv_cube1.volume())+"\n")
fw_adv.write("\n")
fw_adv.close()

