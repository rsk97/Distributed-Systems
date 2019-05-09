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
   def __init__(self,a,b,c):
      self.value = a
      self.index = b
      self.buffer_left = -1
      self.buffer_right = -1
      self.location = c
      #print("Initializing : ",self.left_value['number'],self.right_value['number'],sep =" ")      

   def __repr__(self):
      return "Node: Value = " + str(self.value) + " Index = " + str(self.index)

# Function used by 2 nodes to communicate or rather the intialization of the communication by sending data
def send_data(middle,left = -1,right = -1):
    if left != -1:
        middle.buffer_left = left
    if right != -1:
        middle.buffer_right = right
    local_compute(middle)

# Function for internal processing and identifying correct positions according to the given partial ordering.
def local_compute(middle):
    new_right = max(middle.buffer_left,middle.buffer_right,middle.value)
    new_left = min(middle.buffer_left,middle.buffer_right,middle.value)
    middle.value = (middle.buffer_left + middle.buffer_right + middle.value) - (new_right + new_left)
    recieve_data(new_left,new_right,middle.location)

    
# Function used by 2 nodes to communicate or end the communication by sending data after relevant local computaions
def recieve_data(left,right,index):
    if index - 1 >= 0:
        sasaskis_array[index - 1].value = left
    if index + 1 <len(sasaskis_array):
        sasaskis_array[index + 1].value = right 
   
# The class which creates the thread.
class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   
   def run(self):
      #print ("Starting " + self.name)
      #print(sasaskis_array[0].left_value['number'],sasaskis_array[0].right_value['number'],sasaskis_array[1].left_value['number'],sasaskis_array[1].right_value['number'],sep =" ")      
      ind = [i for i, x in enumerate(sasaskis_array) if x.index == 1]
      #print(ind[self.counter])
      try:
        if ind[self.counter] - 1 >= 0 and ind[self.counter] + 1 < len(sasaskis_array) :
            send_data(sasaskis_array[ind[self.counter]],sasaskis_array[ind[self.counter] - 1].value,sasaskis_array[ind[self.counter] + 1].value)
        elif ind[self.counter] - 1 < 0 and ind[self.counter] + 1 < len(sasaskis_array) :
            send_data(sasaskis_array[ind[self.counter]],right = sasaskis_array[ind[self.counter] + 1].value)
        elif ind[self.counter] - 1 >= 0 and ind[self.counter] + 1 < len(sasaskis_array) :
            send_data(sasaskis_array[ind[self.counter]],left = sasaskis_array[ind[self.counter] - 1].value)
        else:
            pass
      except:
        pass 



sasaskis_array = []
sasaskis_threads = []
round = 0

def create_array(n):
   j = 2*n
   global sasaskis_array
   for i in range(n):
        sasaskis_array = sasaskis_array[:] + [node(j-i,i%3,i)]
        j-=1
   print("The array created is : ")
   print("Value : ",end = " " )
   for i in range(n):
      print(sasaskis_array[i].value,sep =" ",end = "\t")    
   print("\n") 
   print("Modulo : ",end = " " )
   for i in range(n):
       print(sasaskis_array[i].index,sep = " ",end ="\t")
   print("\n")

def create_threads(n):
   for i in range(0,n):
        #print("Thread : ", i ,sep =" ")
        sasaskis_threads.append(myThread(i,"Thread-" + str(i),i))
   #for threads in sasaskis_threads:
   #   threads.start()

def run_threads():
   for threads in sasaskis_threads:
        threads.run()

def join_threads(i):
    for threads in sasaskis_threads:
        try:
            threads.join()
        except:
            pass
    #round += 1
    print("Result after round", i + 1)
    for a in sasaskis_array:
        a.index = (a.index + 2) % 3

def print_sasaki():
   n = len(sasaskis_array)
   print("Array :  ",end =" ")
   for i in range(len(sasaskis_array)):
         print(sasaskis_array[i].value,end ="\t")
   print("\n")
   print("Modulo : ",end =" ")
   for i in range(len(sasaskis_array)):
         print(sasaskis_array[i].index,end ="\t")
   print("\n")

def print_sorted_array():
   print("\n\n\nFinal Sorted Array", end = "\t")
   for i in range(len(sasaskis_array)):
        print(sasaskis_array[i].value,sep =" ",end = " ")    
   print("\n")

if __name__ == "__main__":
   n = 10
   create_array(n)
   #print_sasaki()
   create_threads(int(n/3) + 1)
   print("**********************************************************************************************************\n")

   for i in range(n-1):
      run_threads()
      join_threads(i)
      print_sasaki()
      print("**********************************************************************************************************\n")

