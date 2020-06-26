''' Python's programma which save into lists
the names kai the degrees from 50 students of a highschool class
and next with a function calculate the median degree of class.
After, with another function calculating and presenting the student
of the lowest degree and on the other side the student with higher degree.'''

def klass(d):
    sum = 0
    for i in d:
        sum = sum + i
    mo = sum / 50
    return mo
    
def student(n,d):
    min = d[0]
    max = d[0]
    pos_max = 0
    pos_min = 0
    
    for i in d:
        if max < i:
            max = i
            pos_max = pos_max + 1
            maximum = "The maximum is: ", max
            pos1 = d.index(max)
            stud1 = "The student's name with maximum degree is: ", n[pos1]
        if min > i:
            min = i
            pos_min = pos_min + 1
            minimum = "The minimum is: ", min
            pos2 = d.index(min)
            stud2 = "The student's name with minimum degree is: ", n[pos2]
    print(stud1)
    print(maximum)
    print(stud2)
    print(minimum)

    
names = []
degrees = []
for i in range(50):
    name = input("Dwse onoma: \t")
    degree = float(input("Dwse bathmo: \t"))
    names.append(name)
    degrees.append(degree)

print(student(names,degrees))

print()
print("O mesos oros ths ta3hs einai: ", klass(degrees))
