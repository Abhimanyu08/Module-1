from minitorch import Scalar

a= Scalar(-5.5)

b = (a+5.5).relu()

print(b)
b.backward()

print(a.derivative)