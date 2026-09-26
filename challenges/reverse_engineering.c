#include 
#include 
#include 

// A custom transformation function simulating complex check logic
bool validate_password(const char *input) {
    size_t len = strlen(input);

    // Check 1: Fixed length requirement
    if (len != 10) {
        return false;
    }

    // Check 2: Hardcoded prefix check
    if (strncmp(input, "DEV-", 4) != 0) {
        return false;
    }

    // Check 3: Mathematical constraint on a subset of characters
    // Requires that the 5th and 6th characters sum to ASCII value 100
    if ((input[4] + input[5]) != 100) {
        return false;
    }

    // Check 4: Transformed checksum on the remaining tail
    // Expects specific XOR transformations for the last 4 characters
    unsigned char expected_tail[4] = {0x37, 0x33, 0x31, 0x30}; // Represents "9536" XORed with 0x0E
    for (int i = 0; i < 4; i++) {
        if ((input[6 + i] ^ 0x0E) != expected_tail[i]) {
            return false;
        }
    }

    return true;
}

int main() {
    char password[32];

    printf("=== System Authentication ===\n");
    printf("Enter Admin Password: ");

    if (scanf("%31s", password) != 1) {
        printf("Error reading input.\n");
        return 1;
    }

    if (validate_password(password)) {
        printf("[+] Access Granted. Welcome, Administrator.\n");
    } else {
        printf("[-] Access Denied. Invalid Password.\n");
    }

    return 0;
}