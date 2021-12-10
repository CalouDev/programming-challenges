#include <stdio.h>

int main() {
        int usr, result = 0;

        printf("Enter number: ");
        scanf("%d", &usr);

        for (int i = 1; i < usr; i++) {
                if (usr % i == 0) {
                        printf("%d\n", i);
                        result += i;
                }
        }

        if (usr == result) {
                printf("Perfect number !\n");
        } else {
                printf("Imperfect number...\n");
        }

        return 0;
}
