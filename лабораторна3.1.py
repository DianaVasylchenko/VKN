from tkinter import Y


x = int(input("введіть перше число:"))
y = int(input("введіть друге число:"))
last1 = x % 10
last2 = y % 10
suma = last1+last2
rizn = last1-last2
dob = last1*last2
print(f"{suma} - 8 ")
print(f"{rizn} - 2 ")
print(f"{dob} - 15 ")
