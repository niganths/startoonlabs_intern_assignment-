import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('Data_1.txt')
data2 = np.loadtxt('Data_2.txt')

def find_peaks_and_troughs(data):
    peaks = []
    troughs = []
    for i in range(1, len(data) - 1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(i)
        elif data[i] < data[i-1] and data[i] < data[i+1]:
            troughs.append(i)
    return peaks, troughs


peaks1, troughs1 = find_peaks_and_troughs(data1)
peaks2, troughs2 = find_peaks_and_troughs(data2)


plt.figure(figsize=(10, 6))
plt.plot(data1, label='Signal Data 1')
plt.plot(peaks1, data1[peaks1], 'ro', label='Peaks')
plt.plot(troughs1, data1[troughs1], 'bo', label='Troughs')
plt.title('Signal Data 1 with Peaks and Troughs')
plt.legend()
plt.show()
plt.figure(figsize=(10, 6))
plt.plot(data2, label='Signal Data 2')
plt.plot(peaks2, data2[peaks2], 'ro', label='Peaks')
plt.plot(troughs2, data2[troughs2], 'bo', label='Troughs')
plt.title('Signal Data 2 with Peaks and Troughs')
plt.legend()
plt.show()
print("Data 1 Peaks:", peaks1)
print("Data 1 Troughs:", troughs1)
print("Data 2 Peaks:", peaks2)
print("Data 2 Troughs:", troughs2)
