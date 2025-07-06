import os

# Contact form
CONTACT_NAME = "Naftaly Tester"
CONTACT_EMAIL = "nzlefko@gmail.com"
CONTACT_SUBJECT = "Test Subject"
CONTACT_MESSAGE = "This is a test message."

# Signup/Login
VALID_EMAIL = "nzlefko@example.com"
VALID_PASSWORD = "Nyknicks2025!"

INVALID_EMAIL = "nzlefko@@example.com"
INVALID_PASSWORD = "Nyknicks2025#"

# File upload
UPLOAD_FILE_PATH = "resources/sample.txt"

# Product search
SEARCH_TERM = "dress"

# Base directory & file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FILE_PATH = os.path.join(BASE_DIR, "resources/sample.txt")
