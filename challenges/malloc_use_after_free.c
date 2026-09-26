#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    char *message = malloc(32);
    if (message == NULL) {
        return 1;
    }

    strcpy(message, "temporary challenge data");
    free(message);

    puts(message);
    return 0;
}