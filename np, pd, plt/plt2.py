from matplotlib.pyplot import * 
import matplotlib.pyplot as plt
import numpy as np

# basic plotting

x = [1, 4, 6]
y = [5, 7, 9]

plt.style.use('dark_background')
plt.plot(x, color='y', label='x')
plt.plot(y, color='g', label='y')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot')
plt.legend()
plt.ylim([0, 10])
plt.xticks([0, 1, 2])
plt.savefig('plot.png', dpi=300)
plt.show()

# scatter plot

x = np.random.randn(50)
y = np.random.randn(50)

plt.scatter(x, y, color='b', s=100, marker='v')
plt.title('scatter plot')
plt.show()

# subplot

x = np.arange(0, 100)
y1 = np.sin(x)
y2 = x ** 2 + 2 * x

axe1 = plt.subplot(221)
axe2 = plt.subplot(222)
axe3 = plt.subplot(223)
axe4 = plt.subplot(224)

axe1.plot(x, y1, color='g')
axe2.plot(x, y2, color='orange')
axe3.plot(x, y1, color='y')
axe4.plot(x, y2, color='blue')

plt.show()

# just a plot

x = np.arange(0, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.title('Just a plot')
plt.plot(x, y1, color='r')
plt.plot(x, y2, color='b')

plt.show()

# bar chart

python = [20, 19]
r = [17, 19]

people = ['Bob', 'Mark']

index = np.arange(2)

plt.bar(index, python, width=0.2, label='Python', color='r')
plt.bar(index + 0.2, r, width=0.2, label='R', color='b')
plt.title('Bar plot')
plt.legend()
plt.xticks(index + 0.2, people)
plt.xlabel('Person')
plt.ylabel('skill level')
plt.show()

# pie chart

nationality = ['Greek', 'French', 'American']

people = [10, 23, 49]

explode = [0.1, 0, 0]

plt.pie(people, labels=nationality, explode=explode, shadow=True, counterclock=True, startangle=0, autopct='%2f%%', colors=['r', 'b', 'g'])
plt.title('pie plot')
plt.show()

# histogram

m, s = 172, 8
x = m + s * np.random.randn(1000)
plt.hist(x, 100, density=True, facecolor='b')
plt.grid(True)
plt.text(150, 0.05, 'μ =172, sig = 8')
plt.xlabel('Heights')
plt.ylabel('people')
plt.show()

# 3d

axe = plt.axes(projection='3d')

x = np.random.randint(0, 100, 500)
y = np.random.randint(0, 100, 500)         # scatter
z = np.random.randint(0, 100, 500)

plt.scatter(x, y, z, color='b', alpha=0.1)
plt.show()


axe = plt.axes(projection='3d')

x = np.arange(0, 50, 0.1)
y = np.arange(0, 50, 0.1)
z = np.sin(x)*np.cos(y)

plt.plot(x, y, z, color='g')  
plt.title('just a plot')      # just a plot
plt.xlabel('x values')
plt.ylabel('y values')
axe.set_zlabel('results')
plt.show()

axe = plt.axes(projection='3d')

def z_funcz(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(-5, 5, 100) # (-50, 50, 100)
y = np.linspace(-5, 5, 100) # (-50, 50, 100)     Surface
X, Y = np.meshgrid(x, y)
Z = z_funcz(X, Y)

axe.plot_surface(X, Y, Z, cmap='plasma')
axe.view_init(azim=0, elev=90)
plt.show()