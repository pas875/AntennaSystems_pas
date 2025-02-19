import numpy
import matplotlib.pyplot as plt
import math

F1h = [1]
FC = [1]
FH = [1]
steps = [0]
SGP1 = 0
fS1 = 0
Zeros = []
max_x_FH = []
max_y_FH = []
min_x_FH = []
min_y_FH = []
lambd = 0.03
a = 0.15


for teta in numpy.arange(0.01, numpy.pi / 2, 0.00001):
    mn1 = abs((1 + numpy.cos(teta)) / 2)
    mn2 = abs(math.cos((numpy.pi * a * math.sin(teta))/lambd)/(1 - ((2 * a * math.sin(teta)) / lambd) ** 2))
    mn3 = mn1 * mn2
    F1h.append(mn1)
    FC.append(mn2)
    FH.append(mn3)
    if 0.707 < mn3 < 0.708:
        SGP1 = 2 * math.degrees(teta)
        fS1 = mn3
    steps.append(math.degrees(teta))

for i in range(1, len(FH) - 1):
    if FH[i] > FH[i - 1] and FH[i] > FH[i + 1]:
        max_x_FH.append(steps[i])
        max_y_FH.append(FH[i])

for i in range(1, len(FH) - 1):
    if FH[i] < FH[i - 1] and FH[i] < FH[i + 1]:
        min_x_FH.append(steps[i])
        min_y_FH.append(0)

print("Табл. 1 - Значення нульових кутів")
print("------------------------------")
print("| № |  θ  |FH(θ)|")
m = 1
for i in min_x_FH:
    print(f"| {m} |{i:.2f}|  {0}  |")
    m += 1
print("------------------------------")


print("Табл. 2 - Значення максимальних кутів")
print("------------------------------")
print("| № |  θ  |FH(θ)|")
m = 1
for i in max_x_FH:
    print(f"| {m} |{i:.2f}| {max_y_FH[m-1]:.2f}|")
    m += 1
print("------------------------------")

print("Ширина головної пелюстки в площині H = " + str(round(SGP1, 2)) + '\u00b0')

fig, ax = plt.subplots(figsize=(20/2.54, 12/2.54))
ax.plot(steps, F1h, linewidth=0.7, label="$ F_{1h}(θ) $")
ax.plot(steps, FC, linewidth=0.7, label="$ F_{C}(θ) $")
ax.plot(steps, FH, linewidth=0.7, label="$ F_{H}(θ) $")
ax.plot(SGP1/2, fS1, 'ro', markersize=4, label="ШГП в площині H")
plt.annotate(f'({fS1:.3f}, {SGP1/2:.2f}\u00b0)',
             xy=(SGP1 / 2, fS1),
             xytext=((SGP1/2)+3, fS1+0.05),
             arrowprops=dict(arrowstyle='->', color='black'), fontsize=6)
ax.plot([0, SGP1/2], [fS1, fS1], 'r--', linewidth=0.5)
ax.plot([SGP1/2, SGP1/2], [0, fS1], 'r--', linewidth=0.5)
ax.plot(max_x_FH, max_y_FH, "o", markersize=4, color="black", label="$ \\theta_{max} $ H")
ax.plot(min_x_FH, min_y_FH, "o", markersize=4, color="blue", label="$ \\theta_{min} $ H")
ax.set_xlabel('θ' + '\u00b0', fontsize=10)
ax.set_ylabel('|Fh(θ' + '\u00b0' + ')|, |F1h(θ' + '\u00b0' + ')|, |Fc(θ' + '\u00b0' + ')|', fontsize=10)
plt.xticks(numpy.arange(0, 100, 2), fontsize=7)
plt.yticks(numpy.arange(0, 1.2, 0.1), fontsize=7)
plt.ylim(-0.01, 1.01)
plt.xlim(0, 90.5)
plt.legend(loc="upper right", fontsize=7)
plt.grid(which='both', linestyle='--', linewidth=0.2, color='gray')
plt.title(f'ДС пірамідального рупору в площині Н з параметрами: λ = {lambd}, Ар = {a}', fontsize=10)
fig.savefig("ДС ЛР 3, 1.jpg", dpi=600)