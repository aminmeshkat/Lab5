# -*- coding: utf-8 -*-
"""lab5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cMES4IC5OXlgJWygeUa5A7lC1HgnKMv7
"""

# Task 1

import math

class Point(object):
  
  def __init__(self, x , y):
    self.x = x
    self.y = y

def distance_between_points(P1,P2):
  return math.sqrt((P1.x - P2.x)**2 + (P1.y - P2.y)**2)

P1 = Point(10,10)
P2 = Point(10,15)
print(f"Distance between {P1.x} {P1.y} and {P2.x} {P2.y} is : " , distance_between_points(P1, P2))

# Task 2 A (Extra)


class Rectangle():

  def __init__(self, width, height, corner):

    self.width = width
    self.height = height
    self.corner = corner

  def find_center(self):
    return (self.corner.x + (self.width / 2) , self.corner.y + (self.height / 2))

P1 = Point(12,12)
Rect1 = Rectangle(50,50,P1)
print(Rect1.find_center())

# Task 2 A (main solution)

class Rectangle():

  def __init__(self, width, height, corner):

    self.width = width
    self.height = height
    self.corner = corner

def find_center(r):
  return (r.corner.x + (r.width / 2) , r.corner.y + (r.height / 2))

P1 = Point(15,10)
Rect1 = Rectangle(20,20,P1)
print(find_center(Rect1))

#  Task 2 Part B

def move_rectangle(r, dx, dy):
  r.corner.x = r.corner.x + dx
  r.corner.y = r.corner.y + dy
  print(f"New coordinate for corner is {r.corner.x} {r.corner.y} , and new coordination of the other vertex is : {r.corner.x + r.width} {r.corner.y + r.height}")

P1 = Point(10,10)
Rect1 = Rectangle(20,20,P1)
dx = 15
dy = 15
move_rectangle(Rect1, dx, dy)

# Task 3 A

class Point():

  def __init__(self, x = 0 , y = 0):
    self.x = x
    self.y = y

  def __str__(self):
    if isinstance(self, Point):
      return f"Value of the point is : {self.x},{self.y}"

p1 = Point(100,100)
print(p1)

# Task 3 B

class Point():

  def __init__(self, x = 0 , y = 0):
    self.x = x
    self.y = y

  def __str__(self):
    if isinstance(self, Point):
      return f"Value of the point is : {self.x},{self.y}"
  
  def __add__(self, other):
    return (f"Result of adding two points is : {self.x + other.x} , {self.y + other.y}")

p1 = Point(10,15)
p2 = Point(20,25)
print(p1 + p2)

# Task 4 A

class Time():

  def __init__(self, hour, minute, second):
    self.hour = hour
    self.minute = minute
    self.second = second
  
  def __str__(self):
    return f"{self.hour}:{self.minute}:{self.second}"


t1 = Time(10,20,30)
print(t1)

# Task 4 B

class Time():

  def __init__(self, hour, minute, second):
    self.hour = hour
    self.minute = minute
    self.second = second
  
  def __str__(self):
    return f"{self.hour}:{self.minute}:{self.second}"

def is_after(t1, t2):
  seconds1 = t1.hour * 3600 + t1.minute * 60 + t1.second 
  seconds2 = t2.hour * 3600 + t2.minute * 60 + t2.second
  return seconds1 > seconds2

t1 = Time(10,20,30)
t2 = Time(8,16,59)
print(is_after(t1 , t2))

# Task 5 A

class Kangaroo():

  def __init__(self):
    self.pouch_contents = []

# Task 5 B

class Kangaroo():

  def __init__(self):
    self.pouch_contents = []

  def put_in_pouch(self, an_obj):
    self.pouch_contents.append(an_obj)

# Task 5 C

class Kangaroo():

  def __init__(self):
    self.pouch_contents = []

  def put_in_pouch(self, an_obj):
    self.pouch_contents.append(an_obj)

  def __str__(self):
    return str(self.__dict__)

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch(roo)
print(kanga)
print(roo)

"""Task 6 

True , False , False

True , True , False

True , True , True

Task 7

True , False , False

True , True , False

True , True , True
"""

# Task 8 A

class Super:
  def __init__(self,name):
    self.name = name
  def __str__(self):
    return "My name is " + self.name + "."

class Sub(Super):
  def __init__(self,name):
    Super.__init__(self,name)
object = Sub("Bob")
print(object)

# Task 8 B

class Super:
  def __init__(self,name):
    self.name = name
  def __str__(self):
    return "My name is " + self.name + "."
class Sub(Super):
  def __init__(self,name):
    super().__init__(name)
object = Sub("Bob")
print(object)

# Homework Q 1

class Point():
  
  def __init__(self, x , y):
    self.x = x
    self.y = y

  def __str__(self):
    return f"{self.x},{self.y}"

  def __add__(self, other):
    if isinstance(other, Point):
      p_temp = Point(self.x + other.x, self.y + other.y)
      return p_temp
    elif isinstance(other,tuple):
      if len(other) != 2:
        return "Error. Tuple must have just 2 values..."
      else:
        p_temp = Point(self.x + other[0], self.y + other[1])
        return (p_temp)

p1 = Point(20,10)
p2 = Point(10,15)
print(p1 + p2)
t = (12,18)
print(p1 + t)

# Homework Q 2

class IP_v4():

  def __init__(self, lst, mask):
    self.lst = lst
    self.mask = mask

  def getNetwork(self):
    lst_temp1 = self.toBinary()
    lst_temp2 = []
    for i in range(32):
      if i < self.mask:
        lst_temp2.append(1)
      else:
        lst_temp2.append(0)
    lst_res = []
    for i in range(32):
      lst_res.append(lst_temp1[i] & lst_temp2[i])
    lst_decimal = []
    for i in range(4):
      temp_sum = 0
      for j in range(8):
        if lst_res[i*8 + j] == 1:
          temp_sum += 2**(7-j)
      lst_decimal.append(temp_sum)
    return lst_decimal

   
  def getMask(self):
    q, r = divmod(self.mask,8)
    lst_mask = []
    for i in range(q):
      lst_mask.append(255)
    if q < 4:
      sum_temp = 0
      for j in range(7, 7-r, -1):
        sum_temp += 2**j
      lst_mask.append(sum_temp)
    for k in range(4 - q -1, 0, -1):
      lst_mask.append(0)
    return lst_mask

  def toBinary(self):
    lst_bin = []    
    for item in self.lst:
      lst_temp = []
      for i in range(8):
        if item > 1:
          q , r = divmod(item,2)
          lst_temp.append(r)
          item = q
        else:
          lst_temp.append(item)
          item = 0
      for j in lst_temp[::-1]:
        lst_bin.append(j)
    return (lst_bin)

  def getAddress(self):
    return (self.lst, self.mask)

lst1 = [192,168,1,1]
mask = 24
ip1 = IP_v4(lst1,mask)
print("IPV4 Address is : ",ip1.getAddress())
print("Subnet mask is : ",ip1.getMask())
print("Network Address is : ",ip1.getNetwork())

# Homework Q 3

class Calculator(IP_v4):

  def broadcastAddress(self):
    lst_temp = self.getNetwork()
    tmp_obj = Calculator(lst_temp,self.mask)
    lst_temp2 = tmp_obj.toBinary()
    for i in range(self.mask, 32):
      lst_temp2[i] = 1
    lst_decimal = []
    for i in range(4):
      temp_sum = 0
      for j in range(8):
        if lst_temp2[i*8 + j] == 1:
          temp_sum += 2**(7-j)
      lst_decimal.append(temp_sum)
    return lst_decimal

  def firstHost(self):
    lst_temp = self.getNetwork()
    lst_temp[3] = lst_temp[3] + 1
    return lst_temp

  def lastHost(self):
    lst_temp = self.broadcastAddress()
    lst_temp[3] = lst_temp[3] - 1
    return lst_temp

  def totalNoHost(self):
    return 2**(32-self.mask) - 2
    

      

lst1 = [192,168,1,1]
mask = 20
cal1 = Calculator(lst1, mask)
print(f"Netwotk address is : {cal1.getNetwork()}")
print(f"Broadcast Address is : {cal1.broadcastAddress()}")
print(f"First host Address is : {cal1.firstHost()}")
print(f"Last host Address is : {cal1.lastHost()}")
print(f"Total Number of hosts are : {cal1.totalNoHost()}")