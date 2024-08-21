import matplotlib.pyplot as plt
indices = []
values = []
peaks = []
troughs = []
with open('output.txt', 'r') as file:
    lines = file.readlines()
    data_section = True
    for line in lines:
        line = line.strip()
        if line.startswith("Peaks at indices:"):
            data_section = False
        if data_section and line and line.split()[0].isdigit():
            index, value = map(float, line.split())
            indices.append(int(index))
            values.append(value)
        elif "Peaks at indices:" in line:
            data_section = False
        elif "Troughs at indices:" in line:
            break
        elif not data_section and line.isdigit():
            peaks.append(int(line))
        elif not data_section and not line.startswith("Troughs") and line.isdigit():
            troughs.append(int(line))
plt.plot(indices, values, label='Signal')
plt.plot(peaks, [values[i] for i in peaks], 'ro', label='Peaks')
plt.plot(troughs, [values[i] for i in troughs], 'bo', label='Troughs')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Signal Data with Peaks and Troughs')
plt.legend()
plt.show()
