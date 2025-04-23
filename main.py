from auth import register_user, authenticate

print(register_user("test@example.com", "StrongPass123"))
print(authenticate("test@example.com", "StrongPass123"))
print(authenticate("test@example.com", "wrongpass"))
