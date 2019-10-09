

def verify_user(user, pw):
    user = mdoleman   
    pw = dog123

    if len(user) < 3 and len(user) > 20:
        return True
    else:
        return False

    if len(pw) < 3 and len(pw) > 20:
        return True
    else:
        return False

print(verify_user)

