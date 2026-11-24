def pswd(s):
    if len(s)<8:
        return "Password must be at least 8 characters long"
    if not any(i.isupper() for i in s):
        return "Password must contain at least one uppercase letter"
    if not any(i.islower() for i in s):
        return "Password must contain at least one lowercase letter"
    if not any(i.isdigit() for i in s):
        return "Password must contain at least one digit"
    if not any(i in "@#$%&" for i in s):
        return "Password must contain one special character from @#$%&"
    return "Password is valid"

print(pswd("Divya@3175"))


