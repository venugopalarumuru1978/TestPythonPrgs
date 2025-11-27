lst1 = [10,20,3,40,5,60]
print(lst1)
print("=================")
for n in lst1:
    print(n, end="\t")
print("\n==============")
print("Odd numbers from list ")
for n in lst1:
    if n%2!=0:
        print(n, end="\t")
        