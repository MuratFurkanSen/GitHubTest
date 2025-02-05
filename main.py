import os

# Debug: Print all environment variables (for testing only!)
print("All environment variables:", os.environ)

# Try to get the secret again
db_password = os.getenv("DB_PASSWORD")

if db_password:
    print("✅ Database password loaded securely!")
else:
    print("❌ Error: DB_PASSWORD is missing!")
