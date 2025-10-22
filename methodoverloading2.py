from multipledispatch import dispatch

class A:
 @dispatch(int, int)
 def add(a, b):
   print("addition of int values",(a+b))
 @dispatch(float, float)
 def add(a, b):
   print("addition of float values",(a+b)) 

obj=A
obj.add(10,20)
obj.add(10.2,20.4)