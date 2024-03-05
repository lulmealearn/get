from statistics import mean
import matplotlib.pyplot as plt

with open("exp.txt", "r") as fin:
    data = fin.readlines()

current = [float(line.split()[0]) for line in data[1:]]
voltage = [float(line.split()[1]) for line in data[1:]]
def least_squares(xdata, ydata):
    a = (sum([x * y for x, y in zip(xdata, ydata)]) - mean(ydata) * sum(xdata)) / (sum([x**2 for x in xdata]) - mean(xdata) * sum(xdata))
    b = mean(ydata) - a * mean(xdata)

    return a, b

print(least_squares(current, voltage))

a, b = least_squares(current, voltage)

fig,ax = plt.subplots()
ax.plot(current, voltage, 'o', label = "Experiment's data")

xdata = list(range(0, 21))
ax.plot(xdata, [a * x + b for x in xdata], label = "Approximation")
ax.set_ylabel("Voltage, V")
ax.set_xlabel("Current, A")
ax.legend()
plt.savefig("fig1.png")
plt.show()


