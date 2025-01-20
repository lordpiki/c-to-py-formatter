#include <stdio.h>

int main() {
    int n, i, j;

    // Input size of array
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int arr[n];

    // Input elements into the array
    printf("Enter %d integers:\n", n);
    for (i = 0; i < n; i++) {
        printf("Element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    // Find and display the maximum element
    int max = arr[0];
    for (i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    printf("Maximum element: %d\n", max);

    // Print a multiplication table for numbers 1 to 5
    printf("\nMultiplication Table (1 to 5):\n");
    for (i = 1; i <= 5; i++) {
        for (j = 1; j <= 5; j++) {
            printf("%4d", i * j);
        }
        printf("\n");
    }

    // Check if numbers are odd or even
    printf("\nOdd or Even:\n");
    for (i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {
            printf("Element %d (%d) is Even\n", i + 1, arr[i]);
        } else {
            printf("Element %d (%d) is Odd\n", i + 1, arr[i]);
        }
    }

    return 0;
}
