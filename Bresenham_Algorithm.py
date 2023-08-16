import matplotlib.pyplot as plt

x1 = float(input("Enter the starting coordinate of X: "))
y1 = float(input("Enter the starting coordinate of Y: "))
x2 = float(input("Enter the ending coordinate of X: "))
y2 = float(input("Enter the ending coordinate of Y: "))

dx = x2 - x1
dy = y2 - y1
d = 2*dy - dx
x = x1 
y = y1

points = []

//test merge 1

while x != x2:
    if d<0:
        d = d + 2*dy
        x = x + 1
        y = y 
        print(f"x = {x}",f"y = {y}")
        points.append((x,y))
    else: 
        d = d + 2*dy - 2*dx
        x = x + 1 
        y = y + 1 
        print(f"x = {x}",f"y = {y}")
        points.append((x,y))
xp , yp = zip(*points)

plt.plot(xp, yp, marker='o', linestyle='-')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bresenhams Algorithm')
plt.grid(True)
plt.show()
    
