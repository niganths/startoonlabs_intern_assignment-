#include <stdio.h>
#include <stdlib.h>

void find_peaks_and_troughs(double data[], int length, int peaks[], int troughs[], int *num_peaks, int *num_troughs) {
    *num_peaks = 0;
    *num_troughs = 0;

    for (int i = 1; i < length - 1; i++) {
        if (data[i] > data[i - 1] && data[i] > data[i + 1]) {
            peaks[(*num_peaks)++] = i;
        }
        if (data[i] < data[i - 1] && data[i] < data[i + 1]) {
            troughs[(*num_troughs)++] = i;
        }
    }
}
int main() {
    FILE *file;
    char filename[] = "Data_1.txt";
    int max_length = 1000;
    double data[max_length];
    int length = 0;
    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error: Could not open file %s\n", filename);
        return 1;
    }
    while (fscanf(file, "%lf", &data[length]) != EOF) {
        length++;
    }
    fclose(file);
    int peaks[max_length], troughs[max_length];
    int num_peaks, num_troughs;
    find_peaks_and_troughs(data, length, peaks, troughs, &num_peaks, &num_troughs);
    FILE *output = fopen("output.txt", "w");
    if (output == NULL) {
        printf("Error: Could not open output file\n");
        return 1;
    }

    fprintf(output, "Data:\n");
    for (int i = 0; i < length; i++) {
        fprintf(output, "%d %lf\n", i, data[i]);
    }

    fprintf(output, "\nPeaks at indices:\n");
    for (int i = 0; i < num_peaks; i++) {
        fprintf(output, "%d\n", peaks[i]);
    }

    fprintf(output, "\nTroughs at indices:\n");
    for (int i = 0; i < num_troughs; i++) {
        fprintf(output, "%d\n", troughs[i]);
    }

    fclose(output);

    printf("Results saved to output.txt\n");

    return 0;
}
