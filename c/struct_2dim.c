#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _array {
    double **values;
    // double values[3][3];
} array;

int main() {
    double test[3][3];

    int row = sizeof(test[0]) / sizeof(double);
    int col = sizeof(test) / (sizeof(double) * row);
    printf("col(縦): %d, row(横): %d\n", col, row);

    printf("sizeof(double): %ld\n", sizeof(double));
    printf("sizeof(test): %ld\n", sizeof(test));
    printf("sizeof(test[0]): %ld\n", sizeof(test[0]));

    puts("default array");
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < col; j++) {
            test[i][j] = i + j;
            printf("%p:%.1f, ", &test[i][j], test[i][j]);
        }
        puts("");
    }

    // double test2[3][3];
    double **test2;
    test2 = (double **)calloc(row, sizeof(double *));
    puts("same scope copied array");
    for(int i = 0; i < row; i++) {
        test2[i] = (double *)calloc(col, sizeof(double));
        memcpy(test2[i], test[i], sizeof(test[i]));
        for(int j = 0; j < col; j++) {
            printf("%p:%.1f, ", &test2[i][j], test2[i][j]);
        }
        puts("");
    }

    for(int i = 0; i < row; i++) {
        free(test2[i]);
    }
    free(test2);

    array testArray;
    printf("%p\n", &testArray);
    printf("%p\n", testArray.values);

    puts("internal struct array");
    testArray.values = (double **)calloc(row, sizeof(double *));
    for(int i = 0; i < row; i++) {
        testArray.values[i] = (double *)calloc(col, sizeof(double));
        memcpy(testArray.values[i], test[i], sizeof(test[i]));
        for(int j = 0; j < col; j++) {
            printf("%p:%.1f, ", &testArray.values[i][j], testArray.values[i][j]);
        }
        puts("");
    }

    for(int i = 0; i < row; i++) {
        free(testArray.values[i]);
    }
    free(testArray.values);

    return 0;
}
