import matplotlib.pyplot as plt
import numpy as np

# basic plotting

x = [1, 4, 7]
y = [5, 8, 10]

plt.style.use('dark_background')
plt.plot(x, label='x', color='r')
plt.plot(y, label='y', color='b')
plt.title('plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.ylim([0, 10])
plt.xticks([0, 1, 2])
plt.savefig('plot.png', dpi=300)
plt.show()

# scatter plot

x = np.random.randn(50)
y = np.random.randn(50)

plt.scatter(x, y, color='r', marker='x', s=80)
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

axe1.plot(x, y1, color='r')
axe2.plot(x, y2, color='b')
axe3.plot(x, y1, color='g')
axe4.plot(x, y2, color='y')

plt.show()

# just a plot
x = np.arange(0, 100)
y1 = np.sin(x)
y2 =  np.cos(x)

plt.plot(x, y1, color='b')
plt.plot(x, y2, color='r')
plt.title('just a plot')

plt.show()

# bar chart

python = [10, 20]
sql = [17, 9]

people = ['Bob', 'Mark']

index = np.arange(2)

plt.bar(index, python, color='b', label='Python', width=0.2)
plt.bar(index + 0.2, sql, color='r', label='SQL', width=0.2)
plt.title('bar plot')
plt.legend()
plt.xlabel('people')
plt.ylabel('skill level')
plt.xticks(index + 0.2, people)
plt.show()

# pie chart

nationality = ['Greek', 'French', 'American']

people = [12, 28, 50]

explode = [0.1, 0, 0]

plt.pie(people, labels=nationality, explode=explode, shadow=True, counterclock=True, startangle=0, autopct='%2f%%', colors=['b', 'r', 'g'])
plt.title('pie plot')
plt.show()

# histogram

m, s = 172, 8
x = m + s * np.random.randn(1000)
plt.hist(x, 100, facecolor='b', density=True)
plt.title('Histogram')
plt.xlabel('heights')
plt.ylabel('percentence of people')
plt.grid(True)
plt.text(150, 0.05, 'μ = 172 sig = 8')

plt.show()

# 3d plots

ax = plt.axes(projection='3d')

x = np.random.randint(0, 100, 500)
y = np.random.randint(0, 100, 500)        # scatter
z = np.random.randint(0, 100, 500)

plt.scatter(x, y, z, color='r', marker='*')
plt.show()


axe = plt.axes(projection='3d')

x = np.arange(0, 50, 0.1)
y = np.arange(0, 50, 0.1)
z = np.sin(x) * np.cos(y)            # just a plot

plt.plot(x, y, z, color='g')
plt.title('just a plot')
plt.xlabel('x values')
plt.ylabel('y values')
axe.set_zlabel('results')

plt.show()



ax = plt.axes(projection='3d')

def z_function(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))         # surface

x = np.linspace(-5, 5, 100)  # -50, 50, 100
y = np.linspace(-5, 5, 100)  # -50, 50, 100

X, Y = np.meshgrid(x, y)

Z = z_function(X, Y)                      

ax.plot_surface(X, Y, Z, cmap='plasma')
ax.view_init(azim=0, elev=90)
plt.show()