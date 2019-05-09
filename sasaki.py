# Name : Rohan S
# Roll no 20160010073
# Sasaki ALgorithm using threading
# Date : 14/02/2019

#!/usr/bin/python3

import threading
import time
import sys
from copy import copy

# The ADT used for creation of the node which represents one system in a line network
class node (object):
   def __init__(self,a,b):
      self.left_value = {}
      self.right_value = {}
      self.left_value['number'] = int(a)
      self.right_value['number'] = int(b)
      self.left_value['marker'] = False
      self.right_value['marker'] = False
      self.left_buff = {'marker':False,'number':0}
      self.right_buff = {'marker':False,'number':0}
      self.area = 0
      self.round = 0
      #print("Initializing : ",self.left_value['number'],self.right_value['number'],sep =" ")      

   def __repr__(self):
      return "Node: Left= " + str(self.left_value['number']) + " Right= " + str(self.right_value['number'])


def swap_inter_node(a):
   if int(a.left_value['number']) > int(a.right_value['number']):
      temp = a.left_value['number']
      a.left_value['number'] = a.right_value['number']
      a.right_value['number'] = temp
      temp = a.left_value['marker']
      a.left_value['marker'] = a.right_value['marker']
      a.right_value['marker'] = temp

def send_data(a,b):
   b.left_buff = a.right_value.copy()
   local_compute(a,b)

def local_compute(a,b):
   if int(b.left_buff['number']) > int(b.left_value['number']) :
      if b.left_buff['marker'] == True :
         b.area -= 1
      if b.left_value['marker'] == True:
         b.area += 1

      recieve_data(b.left_value,a)
      b.left_value = b.left_buff.copy()
   else:
      recieve_data(a.right_value,a)

def recieve_data(b_left_value,a):
   a.right_value = b_left_value.copy()

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   
   def run(self):
      #print ("Starting " + self.name)
      #print(sasaskis_array[0].left_value['number'],sasaskis_array[0].right_value['number'],sasaskis_array[1].left_value['number'],sasaskis_array[1].right_value['number'],sep =" ")      
      
      send_data(sasaskis_array[self.counter],sasaskis_array[self.counter + 1])
      
      #swap_inter_node(sasaskis_array[self.counter])
      #swap_inter_node(sasaskis_array[self.counter + 1])
      #for i in range(len(sasaskis_array)):
      #   print(sasaskis_array[i].left_value['number'],sasaskis_array[i].right_value['number'],sep =" ",end = " ")    
      #print("\n") 
      #print(sasaskis_array[self.counter].left_value['number'],sasaskis_array[self.counter].right_value['number'],sasaskis_array[self.counter + 1].left_value['number'],sasaskis_array[self.counter + 1].right_value['number'],sep =" ")
      #print ("Exiting " + self.name)


sasaskis_array = []
sasaskis_threads = []
round = 0

def create_array(n):
   j = 2*n
   global sasaskis_array
   for i in range(n):
      if i == 0 :
         sasaskis_array = sasaskis_array[:] + [node(-sys.maxsize, j-i)]
         sasaskis_array[0].right_value['marker'] = True
         sasaskis_array[0].area = -1
      elif i == n-1:
         sasaskis_array = sasaskis_array[:] + [node(j-i, sys.maxsize)]
         sasaskis_array[n-1].left_value['marker'] = True
      else:
         sasaskis_array = sasaskis_array[:] + [node(j-i, j-i)]
      j-=1
   print("The array created is : ",end = " ")
   for i in range(n):
      print(sasaskis_array[i].left_value['number'],sasaskis_array[i].right_value['number'],sep =" ",end = " ")    
   print("\n") 

def create_threads(n):
   for i in range(0,n-1):
      sasaskis_threads.append(myThread(i,"Thread-" + str(i),i))
   for threads in sasaskis_threads:
      threads.start()

def run_threads():
   for threads in sasaskis_threads:
      threads.run()

def join_threads(i):
   for threads in sasaskis_threads:
      threads.join()
   #round += 1
   print("Result after round", i + 1,end = "\t")
   for i in range(len(sasaskis_array)):
         swap_inter_node(sasaskis_array[i])

def print_sasaki():
   n = len(sasaskis_array)
   for i in range(len(sasaskis_array)):
         if i == 0:
            print(sasaskis_array[0].right_value['number'],end = " ")
         elif i == n-1:
            print(sasaskis_array[n-1].left_value['number'],end = "\t")
         else:
            print(sasaskis_array[i].left_value['number'],sasaskis_array[i].right_value['number'],sep ="|",end = " ")    
   print("\n")
   print("Markers of the Elements : ", end ="")
   for i in range(len(sasaskis_array)):
         if i == 0:
            print(sasaskis_array[0].right_value['marker'],end = "\t")
         elif i == n-1:
            print(sasaskis_array[n-1].left_value['marker'],end = "\t")
         else:
            print(sasaskis_array[i].left_value['marker'],sasaskis_array[i].right_value['marker'],sep ="|",end = " ")    
   print("\n")
   print("Area of the Nodes : ", end ="")
   for i in range(len(sasaskis_array)):
         print(sasaskis_array[i].area,end =" ")
   print("\n")

def print_sorted_array():
   print("\n\n\nFinal Sorted Array", end = "\t")
   for i in range(len(sasaskis_array)):
         if sasaskis_array[i].area == -1:
            print(sasaskis_array[i].right_value['number'],end = " ")
         else:
            print(sasaskis_array[i].left_value['number'],sep =" ",end = " ")    
   print("\n")

if __name__ == "__main__":
   n = 10
   create_array(n)
   #print_sasaki()
   create_threads(n)
   print("**********************************************************************************************************\n")

   for i in range(n-1):
      run_threads()
      join_threads(i)
      #print("After internal re-arrangement",end =" ")
      print_sasaki()
      print("**********************************************************************************************************\n")
   print_sorted_array()
