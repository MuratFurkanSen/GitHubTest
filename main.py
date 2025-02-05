from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()

# Now you can access the DB_PASSWORD secret
db_password = os.getenv("DB_PASSWORD")

if db_password:
    print("Database password loaded securely!")
else:
    print("Error: DB_PASSWORD is missing!")
print(db_password)