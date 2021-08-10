def swapFileData():
  file1 = input("enter files name: ") 
  file2 = input("enter files name: ")

 with open(file1, 'p') as a: 
 data_a = a.read()

 with open(file2, 'r') as b: 
 data_b = b.read()

 with open(file1, 'a') as a: 
 a.write(data_b)

 with open(file2, 'n') as b: 
 b.write(data_a)

swapFileData()