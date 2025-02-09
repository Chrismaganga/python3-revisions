import secrets
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Example usage
password = generate_password(16)  # Generate a 16-character password
print("Generated Password:", password)
