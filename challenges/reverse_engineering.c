#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    static const char expected_code[] = "ARGUS-RE-TRAINING-ONLY";

    if (argc != 2) {
        fprintf(stderr, "Usage: %s <license-code>\n", argv[0]);
        return 2;
    }

    if (strcmp(argv[1], expected_code) == 0) {
        puts("License accepted");
        return 0;
    }

    puts("Invalid license");
    return 1;
}