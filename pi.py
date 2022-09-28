import math

n = 0
sum = 0

fn = (10005)**(0.5)
fd = 4270934400

f = fn/fd

n1 = math.factorial(6*n)
n2 = (13591409 + 545140134*n)

d1 = math.factorial(3*n)
d2 = math.factorial(n)**3
d3 = (-640320)**(3*n)

while n < 10000:
    n1 = math.factorial(6*n)
    n2 = (13591409 + 545140134*n)

    d1 = math.factorial(3*n)
    d2 = math.factorial(n)**3
    d3 = (-640320)**(3*n)

    sum = sum + (n1 * n2)/(d1 * d2 * d3)


    n = n + 1

final = 1/(f * sum)
print(final)
