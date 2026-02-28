Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import maths
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import maths
ModuleNotFoundError: No module named 'maths'
>>> n=int(input("Enter a number:"))
Enter a number:28
>>> sum = 0
>>> for i in range(1,n)
SyntaxError: expected ':'
>>> for i in range(1,n):
...     if n%i == 0:
...         sum = sum +i
...     if sum == n:
...         print("Perfect number")
...     else:
...         print("Not a perrfect number")
... 
...         
Not a perrfect number
Not a perrfect number
Not a perrfect number
Not a perrfect number
Not a perrfect number
Not a perrfect number
Not a perrfect number
Not a perrfect number
Not a perrfect number
Not a perrfect number
Not a perrfect number
Not a perrfect number
Not a perrfect number
Perfect number
Perfect number
Perfect number
Perfect number
Perfect number
Perfect number
Perfect number
Perfect number
Perfect number
Perfect number
Perfect number
Perfect number
Perfect number
Perfect number
>>> n=int(input("Enter the limit:"))
Enter the limit:5
>>> for i in range(1,n+1):
...     print(i,"square is",i*i)
... 
...     
1 square is 1
2 square is 4
3 square is 9
4 square is 16
5 square is 25
