'''
02/11/2021
---------------------------------
Review:
Boolean Operators:
if (5 > 4 or "python" != 5)
Types:
and
or
not
---------------------------------------------
import random (importing random library)
variable = random.randint(start, end)
=====================================================
while loop
repeats a set of statements as long as a condition is True

Formula:
while (Condition)
  BODY
else: <---- optional
  BODY
------------------------------------------------------
Example:
while (True):
    print ("This statement prints forever.")

Rule:
A loop becomes infinite loop if a condition never becomes FALSE. An infinite loop might be useful in client/server programming where the server needs to run continiously.

However, you must use caution when using while loops because of the possibility that this condition resolves to a FALSE value. To avoid a infinite loop, make sure to use a variable and keep track of its value.

Exercise 1 
Expected outputs
 Hello
 Python
 Python
 Evergreen
 Evergreen
 Evergreen
 2021
'''

'''
integer = 1
while (integer < 10):
    print ("This statement prints forever.")
    integer += 1 #Incremenration
'''


student = 0
while (student <= 6):
  if (student < 1):
    print ("Hello!")
  elif (student < 3):
    print ("Python!")
  elif (student < 3):
    print ("Bye!")
  elif (student <= 5):
    print ("Evergreen!")
  else:
    print ("2021!")

  student += 1
  