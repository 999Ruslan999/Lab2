num = int(input())
if num % 2 == 0:
    print("нижнее", end=" ")
else:
    print("верхнее", end=" ")

if num in range(1, 37):
    print("купе")
else:
    print("боковое")