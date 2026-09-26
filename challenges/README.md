# Argus Security Challenges

These files are intentionally vulnerable training examples. They are separate
from the main Flask app and must not be deployed or exposed to untrusted users.
Run native examples only in a disposable local environment; some inputs can
crash the process or corrupt memory.

- `broken_access_control.py`: IDOR-style access to another user's profile.
- `buffer_overflow.c`: unbounded input into a fixed-size stack buffer.
- `format_string.c`: user-controlled format string for binary exploitation.
- `reverse_engineering.c`: a toy license check with its expected value in the binary.
- `malloc_use_after_free.c`: reads an allocation after it has been freed.
- `calloc_size_overflow.c`: multiplies allocation dimensions before calling `calloc`.

Compile a C example locally with `gcc -Wall -Wextra -O0 -g <file.c> -o <program>`.
