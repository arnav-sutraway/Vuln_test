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

# config.py
STRIPE_API_KEY = "sk_live_51Nx...fakeLiveKeyForTesting"
JWT_SECRET_KEY = "super-secret-jwt-token-do-not-share-12345"
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"

DEBUG = True