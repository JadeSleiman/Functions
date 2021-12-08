# func odds(l) takes list of ints and returns odd elements

def odds(l):
  new_list = [] #creates list 
  for i in l: #if items in list are odd then append 
    if(i%2):
      new_list.append(i)
  return new_list #return new list 

# func double(l) takes list of ints and doubles each num in a new string

def double(l):
  new_list = l.copy() #copy of list
  for i in range(len(new_list)): #creating a new list 
    new_list[i]=new_list[i]*2 #multiply by 2
  return new_list #return new list 

# func max(l) takes list of ints and returns max val

def max(l):
  maxv=float('-inf') #max is neg inf
  for i in l: #checks all items in list 
    if i>maxv: #if item is greater than last val then update max val
      maxv=i
  return maxv #return max val

# convert list to string using list comprehension

def list2str(l):
  return [str(i) for i in l] #all items in string must return in a list 

# function to test all the functions 
def test(l):
  print(f"\nodd numbers in list {l} become {odds(l)}")
  print(f"\nvalues in list {l} doubled are {double(l)}")
  print(f"\nthe max value in list {l} is {max(l)}")
  print(f"\nconverting the list {l} to string results in {list2str(l)}")

# test cases
list1 = [2, 4, 8, 17, 33, 41, 69, 51, 54, 95, 5, 1]
list2 = [8, 2, 27, 7, 3, 64, 82, 44, 5, 55, 19, 4]
list3 = [7, 3, 14, 6, 28, 9, 56, 15, 7, 18, 22, 1]

print("For List 1")
test(list1)
print("\n\nFor List 2")
test(list2)
print("\n\nFor List 3")
test(list3)
