#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class stack:
  def __init__(self):
    self.__val = [None]*9
    self.__tos = -1

  def push(self,y):
    self.__tos +=1
    self.__val[self.__tos] = y

  def pop(self):
    if self.__tos == -1:
      print("Stack underflow")
      return 0
    else:
      self.__tos-=1
      return(self.__val[self.__tos+1])

  def status(self):
    return self.__tos
  def display(self):
    for i in range(0,tos,1):
      print(self.__val[i])

x = input("please enter post-fix notation ")
STACK  = stack()
while True:
  for i in range (0,len(x),1):
    if x[i] != '*' and x[i] != '+' and x[i] != '-' and x[i] != '/':
      STACK.push(x[i])
    else:
      if x[i] == "*":
        second_value = STACK.pop()
        first_value = STACK.pop()
        out_put_val = int(first_value) * int(second_value)
        print(out_put_val)
        STACK.push(out_put_val)
      elif x[i] == "/":
        second_value = STACK.pop()
        first_value = STACK.pop()
        out_put_val = int(first_value) / int(second_value)
        print(out_put_val)
        STACK.push(out_put_val)
      elif x[i] == "+":
        second_value = STACK.pop()
        first_value = STACK.pop()
        out_put_val = int(first_value) + int(second_value)
        print(out_put_val)
        STACK.push(out_put_val)
      elif x[i] == "-":
        second_value = STACK.pop()
        first_value = STACK.pop()
        out_put_val = int(first_value) - int(second_value)
        print(out_put_val)
        STACK.push(out_put_val)
  print("final answer is " + str(out_put_val))
  break

