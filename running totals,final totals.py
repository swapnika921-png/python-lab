Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> numbers = [10, 20, 30, 40]
>>> total = 0
>>> for num in numbers:
...     total = total + num
...     print("Running Total:", total)
... 
...     
Running Total: 10
Running Total: 30
Running Total: 60
Running Total: 100
>>> n=int(input("How many numbers? "))
How many numbers? 8
>>> for i in range(n)
SyntaxError: expected ':'
>>> for i in range(n):
...     num = int(input("Enter numbers:"))
...     total += num
...     print("Running Total:", total)
... 
...     
Enter numbers:1
Running Total: 101
Enter numbers:5
Running Total: 106
Enter numbers:6
Running Total: 112
Enter numbers:8
Running Total: 120
Enter numbers:3
Running Total: 123
Enter numbers:2
Running Total: 125
Enter numbers:9
Running Total: 134
Enter numbers:7
Running Total: 141
>>> numbers = [10, 20, 30, 40]
>>> total = 0
>>> for num in numbers:
...     total += num
...     print("Final total:", total)
... 
...     
Final total: 10
Final total: 30
Final total: 60
Final total: 100
\
