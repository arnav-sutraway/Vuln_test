"""
Intentionally fake configuration secrets for Argus testing.
These credentials are nonfunctional.
"""

# Hardcoded Secret #5
STRIPE_SECRET_KEY = "sk_test_ARGUS_FAKE_STRIPE_KEY_123456"

# Hardcoded Secret #6
AWS_ACCESS_KEY_ID = "AKIAARGUSFAKEACCESSKEY"

# Hardcoded Secret #7
AWS_SECRET_ACCESS_KEY = "ARGUS_FAKE_AWS_SECRET_KEY_123456789"

# Hardcoded Secret #8
DATABASE_PASSWORD = "argus_fake_postgres_password"

# Hardcoded Secret #9
GITHUB_TOKEN = "ghp_ARGUS_FAKE_GITHUB_TOKEN_123456789"

# Hardcoded Secret #10
ENCRYPTION_KEY = "ARGUS_FAKE_ENCRYPTION_KEY_NOT_REAL"


DATABASE_URL = (
    "postgresql://testuser:argus_fake_password@localhost/testdb"
)

DEBUG = True