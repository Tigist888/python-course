# Try the following examples in Terminal and try to figure out
# why the difference in results

# >>> 4 + 100 / 10 * 5
a=4
b=100
c=10
d=5
result_1=(a + b /c*d)
print(result_1)

# >>> 4 + (100 / (10 * 5))
a=4
b=100
c=10
d=5

total=( a +(b /(c * d  )))
print(total)
# precedence

# >>> (4 + 100 / 10) * 5
a = 4
b = 100
c = 10
d = 5
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
result=(a + b/c) * d
print(result)

# >>> ((4 + 100) / 10) * 5

a = 4
b = 100
c = 10
d = 5
total_2=((a +b) / c) * d
print(total_2)