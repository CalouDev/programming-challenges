/* Challenge from https://github.com/RobinsonD3v

  Votre programme prend 5 entrée et affiche la plus proche d'une 6e

*/

#include <stdio.h>
#include <stdlib.h>

#define ARR_SIZE 5; // 5 elements in the array

int closestNum(int arr[], int num) {
        int result = arr[0];

        for (int j = 0; j < 5; j++) {
                // printf("Comparison between %d and %d\n", arr[j], result);
                if (abs(arr[j] - num) < abs(result - num)) {
                        result = arr[j];
                }
        }

        return result;
}

int main(void) {
        int input[ARR_SIZE], n;

        for (int i = 0; i < 5; i++) {
                printf("Enter number: ");
                scanf("%d", &input[i]);
        }

        printf("Entrez le nombre à comparer: ");
        scanf("%d", &n);

        printf("Le nombre le plus proche de %d est %d\n", n, closestNum(input>

        return 0;
}
