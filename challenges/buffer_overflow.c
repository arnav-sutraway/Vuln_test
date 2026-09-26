#include <stdio.h>

int main(void) {
    char input[16];

    printf("Enter a name: ");
    scanf("%s", input);
    printf("Hello, %s\n", input);
    return 0;
}