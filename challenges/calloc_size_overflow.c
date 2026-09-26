#include <stdio.h>
#include <stdlib.h>

struct record {
    char value[16];
};

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <record-count>\n", argv[0]);
        return 2;
    }

    size_t count = (size_t)strtoull(argv[1], NULL, 10);
    struct record *records = calloc(count * sizeof(*records), 1);
    if (records == NULL) {
        return 1;
    }

    for (size_t i = 0; i < count; ++i) {
        records[i].value[0] = 'A';
    }

    free(records);
    return 0;
}