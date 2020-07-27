import numpy as np

#creation of numpy arrays
a=np.array([1,2,3,4])
print(a)

b=np.array([[1,2,3,4],[0,0,0,0]])
print(b)

#get dimension
print(a.ndim)
print(b.ndim)

#get shape
print(a.shape)
print(b.shape)

#get data type
c=np.array([1.2,2.3,4.4,5.9])
d=np.array([1,2,4,4],dtype='int8')
print(c.dtype)
print(a.dtype)
print(d.dtype)

#size  acording to number of elements in numpy array
e=np.array([1,1], dtype='int8')
print(a.size)
print(e.size)
print(c.size)

#size of each element in numpy array acording to dtype
print(a.itemsize) #int32 = 4bytes
print(e.itemsize) #int8  = 1byte
print(c.itemsize) #float64 = 8bytes

#total size = bytes for dtypes* elements
#in other words total_size_of_a = a.size * a.itemsize
#but there is an easier way
print(a.nbytes) # 4*4=16bytes
print(e.nbytes) # 2*1 = 2bytes
print(c.nbytes) # 4*8 =32 bytes

#get specific elements (counting start from 0)
my_array=np.array([[1,4,5,6,7,8,10],[33,55,7,8,10,4,9]])
print(my_array[0,6]) #must show 10
print(my_array[0,-1]) #must show 10 again as it is the last element of first row

#get specifice row
print(my_array[0,:])
print(my_array[0,3:7]) #from first row only 4th to 7th column,
# in the above cmd 3 means start from 4th(position 3) and 7 end at 7th(position 6)
print(my_array[0,3:6:2]) # from position 3 to 6 step by 2

#get specific column
print(my_array[:,2])

#change an element
my_array[1,0]=98
print(my_array)
my_array[0,:]=5
print(my_array)
my_array[:,5:7]=[1,2]
print(my_array)

#all zeros numpy array
zeros_float=np.zeros((3,3))
zeros_int=np.zeros((3,3), dtype='int32') #zeros as integer
print(zeros_int)
print(zeros_float)

#all ones numpy array
ones=np.ones((3,3)) #can be changed ot int16, float32 etc.
print(ones)

#initialise numpy array with whatever number we want
my_number=np.full((3,3),99,dtype='int32')
print(my_number)

#if we want to make an array that all elements have same value and the shape we want is a shape of another
#array then:
my_number=np.full_like(a,8) #we use the shape of array a
print(my_number)

#random decimal number 0.0 -1.0
r=np.random.rand(3,4)
print(r)

#random intigers 1-10
r=np.random.randint(1,101,size=(3,4)) # always +1 the max number so 101 not 100
print(r)

#identitymatrix
i=np.identity(3,dtype='int8')
print(i)

#repeat(copy)
my=np.array([[1,2,3]]) #for use of repeat whe need an extra []
my_final=np.repeat(my,3,axis=0) # 3 rows where my array will be coppeid 3 times
print(my_final)

my_final=np.repeat(my,3,axis=1) # 1 row where each element will be coppeid 3 times countinusly and the the next element
print(my_final)

#copy warning!!!!
a1=np.array([1,2,3])
a2=a1.copy()
a2[0]=100 #sos!!! if i didnt use a2=a1.copy but a2=a1 then a1[0] would also have changed!!!!!!
print(a1)
print(a2)

#element basic math
print(a+56) #adds 56 to each element
print(a-10) #subtracts 10 from each element
print(a*2) #multiplies each element by 2
print(a/2) #divides each element by2
print(a**2) #each element on power of 2

b= np.array([8,8,8,8])
print(a+b) #sums each element of a with element of b that has same possition , 1st element of a with 1st elemtn of b and so on
print(a*b) # a is 1x4 , b is 1x4 acording to linear algebra multplication cant be done but this is
           #elemnt multiplication not matrix
#sin,cos
print(np.cos(a))
print(np.sin(a))

#matrix multiplication
m1=np.full((2,3),9)
m2=np.random.randint(1,11,size=(3,2))
mul_res=np.matmul(m1,m2)
print(mul_res)

#determinantd
#mul res is a 2x2 matrix thus we will use it
print(np.linalg.det(mul_res)) #linalg has lot of nice functions

#statistics
m=np.random.randint(1,101,size=(5,5))
print(np.max(m[2:4,2:4])) #max while filtering row and columns
print(np.max(m)) #max without filtering
print(m)
print(np.max(m,axis=0)) #show bigets elements of each colum
print(np.max(m,axis=1)) #shows biggest element of each row
#in a similra logic min,sum,mean so look at the documentation!!!!!!!!!!!!!!!!!!!!!!!!!

#reshape
m1=m.reshape((25,1)) #made a 5x5 into 25x1
print(m1)

#vstack add arays as row as many times we want
v1=np.array([1,2,3,4])
v2=np.array([2,4,6,8])
v3=np.vstack([v1,v2])
print(v3)
v3=np.vstack([v1,v2,v2,v2])
print(v3)

#hstack add arays to the right side each time
v3=np.hstack([v1,v2])
print(v3) #output=[1 2 3 4 2 4 6 8]
v3=np.hstack([v1,v2,v2,v2]) # output = [1 2 3 4 2 4 6 8 2 4 6 8 2 4 6 8]
print(v3)

#read from file
my_file=np.genfromtxt('numpy_text_array.txt', delimiter=' ')
my_file=my_file.astype('int32') #change data type
print(my_file)

#sos geting matrix info (boolean masking and advanced indexing)
print(m>50) #shows in true/false wheteher the number is greater than 50

greater_than_50=m[m>50] #creating an 1 dimension araay with bvalues >50
print(greater_than_50)
print(greater_than_50.size) #count

x=m[[2,1],[2,3]] #advanced iidexing getting spefici elements and put them into array
print(x)

print(np.any(m>90,axis=1)) #m is 5x5, axis =0 lopps trough rows so returns 5 values, if any elements of each row>90 then tru
print(np.any(m>90,axis=0)) #same with above but loops thorugh columns

print(np.all(m>30,axis=1)) #m is 5x5, axis =0 lopps trough rows so returns 5 values, if all(not any!!!) elements of each row>30 then tru
print(np.all(m>30,axis=0)) #same with above but loops thorugh columns

#in booean masking and advance indexing multpiple conditions also can be used for instacne:
between60_and70= m[(m>60)&(m<70)]
print(between60_and70)
