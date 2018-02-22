a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
b=[]
import random
for i in range(30):
    a[i]=random.randint(-29,29)
print "Η λίστα είναι η εξής:"
print a
for i in range(30):
    x=a[i]
    for j in range(30):
        if (i != j):
            y=a[j]
            for k in range(30):
                if (j != k):
                    z=a[k]
                    if (x+y+z == 0):
                        b.append(x)
                        b.append(y)
                        b.append(z)
if (len(b) != 0):
    print "Οι συνδυασμοί τριάδων από τη λίστα με άθροισμα 0 είναι:"
    for l in range(0,len(b),3):
        print b[l], b[l+1], b[l+2]
else:
    print "Δεν υπάρχει συνδυασμός τριάδων από τη λίστα που έχουν άθροισμα 0."
