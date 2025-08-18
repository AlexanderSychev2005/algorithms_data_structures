#include <iostream>

// TODO

// TIP Static Array
int main() {
    // float k = 0.5f, b = -1.4f;
    //
    // // const int n = 100;
    // // float y[n]; // 400 bytes
    //
    // int n = 100;
    // // float* y = new float[n];
    // auto* y = new float[n];
    // y[0] = k * 0 + b;
    //
    // for (int x = 0; x < 100; ++x) {
    //     y[x] = k * x + b;
    // }
    // for (int x = 0; x < 10; ++x) {
    //     printf("%.2f ", y[x]);
    // }
    // delete[] y;

    const int N = 20;
    // char marks[N]; // 20 bytes, chat - 1 byte, 0 < x < 255

    // char marks[N] = { 2, 2, 3};
    // int count_marks = 3;
    //
    // int index_insert = 1;
    // int end = (count_marks < N) ? count_marks : N-1;
    //
    // for (int i = end; i > index_insert; --i) {
    //     marks[i] = marks[i - 1];
    // }
    // marks[index_insert] = 4;
    // if (count_marks < N) count_marks += 1;
    //
    // for (int i = 0; i < count_marks; ++i) {
    //     printf("%d ", marks[i]);
    // }

    char marks[N] = { 2, 4, 2, 3};
    int count_marks = 4;

    int index_del = 0;

    for (int i = index_del; i < count_marks; ++i) {
        marks[i] = marks[i + 1];
    }

    if (count_marks > 0) count_marks--;

    for (int i = 0; i < count_marks; ++i) {
        printf("%d ", marks[i]);
    }

    return 0;
}