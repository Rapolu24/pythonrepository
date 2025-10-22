from functools  import singledispatchmethod
class One:
 @singledispatchmethod
 def add(a):
  pass
 @add.register(int)
 def _(b:int):
   b+=10
   print("addition of int value",b)
 @add.register(float)
 def _(c:float):
   c+=10.5
   print("addition of float value",c)
   print("subtraction of float value",b)
obj=One
obj.sub(10.2)
obj.add(10)
