import matplotlib.pyplot as plt

x1 = float(input("Enter the starting coordinate of X: "))
y1 = float(input("Enter the starting coordinate of Y: "))
x2 = float(input("Enter the ending coordinate of X: "))
y2 = float(input("Enter the ending coordinate of Y: "))

dx = x2 - x1
dy = y2 - y1

m = dy / dx
x = x1
y = y1

print("\n The Points are:")

if abs(m) <= 1:
    while round(x, 2) != x2 and round(y, 2) != y2:
        x = x + 1
        y = y + m
        rx = round(x, 2)
        ry = round(y, 2)
        print(f"x = {rx:.2f}, y = {ry:.2f}")
else:
    while round(x, 2) != x2 and round(y, 2) != y2:
        y = y + 1
        x = x + 1 / m
        rx = round(x, 2)
        ry = round(y, 2)
        print(f"x = {rx:.2f}, y = {ry:.2f}")

xp,yp = zip(*points)

plt.plot(xp, yp, marker='o', linestyle='-')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('DDA Algorithm')
plt.grid(True)
plt.show()
