#include <stdio.h>

int main(void) {
    char input[128];

    printf("Enter a message: ");
    if (fgets(input, sizeof(input), stdin) == NULL) {
        return 1;
    }

    printf(input);
    return 0;
}