# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = "123abc"

if len(password) < 6:
    print("Weak")
elif len(password) <= 10:
    print("Medium")
else:
    print("Strong")