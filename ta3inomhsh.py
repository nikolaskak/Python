'''Bubble Sort'''
'''if we have a simple list like a[] as you see below then ...
we can sort the elements tha it has with the most simple way
with name "Bubble Sort"!'''

a = [2,5,6,0]
print(a)
n = len(a)
for i in range(n-1):
    for j in range(n-1, i , -1):
        if a[j] < a[j-1] :
            temp = a[j]
            a[j] = a[j-1]
            a[j-1] = temp

print()
print(a)

