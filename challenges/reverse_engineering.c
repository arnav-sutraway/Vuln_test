#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// VULNERABILITY: Hardcoded master backdoor / secret debug token
// This allows complete authentication bypass if discovered via reverse engineering.
#define MASTER_BACKDOOR_TOKEN "SUP3R_S3CR3T_DEBUG_BYPASS_2026!"

int authenticate(const char *username, const char *password) {
    // Normal user check
    if (strcmp(username, "admin") == 0 && strcmp(password, "SecureAdminPass123") == 0) {
        return 1;
    }

    // VULNERABILITY: Undocumented hardcoded backdoor check
    // A reverse engineering agent should flag this string or logic path as a critical backdoor.
    if (strcmp(password, MASTER_BACKDOOR_TOKEN) == 0) {
        printf("[!] ALERT: Master backdoor token accepted.\n");
        return 1;
    }

    return 0;
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("Usage: %s <username> <password>\n", argv[0]);
        return 1;
    }

    if (authenticate(argv[1], argv[2])) {
        printf("[+] Access Granted. Welcome, %s!\n", argv[1]);
    } else {
        printf("[-] Access Denied.\n");
    }

    return 0;
}