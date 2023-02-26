from fastapi import Body, FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

app = FastAPI()

security = HTTPBasic()


class User:
    def __init__(self, name: str, email: str, role: str, country: str, nationality: str, mobile: str, password: str):
        self.name = name
        self.email = email
        self.role = role
        self.country = country
        self.nationality = nationality
        self.mobile = mobile
        self.password = password


users: [User] = []


# Define a function to get the user based on email and password
def get_user(email: str, password: str):
    for user in users:
        print(user)
        if user.email == email and user.password == password:
            return user
    return None


def to_dict(self): return {

    "name": self.name,
    "email": self.email,
    "role": self.role,
    "country": self.country,
    "nationality": self.nationality,
    "mobile": self.mobile,
    "password": self.password
}


def reg_user(name, email, role, country, nationality, mobile, password):
    new_user = User(name, email, role, country, nationality, mobile, password)
    for user in users:
        if user.email == email:
            return False
    users.append(new_user)

    return "successfully registered"


# Define a function to check if the user has admin role
def is_admin(user: User = Depends(get_user)):
    if user and user.role == 'admin':
        return user
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access Denied!")


def is_staff(user: User = Depends(get_user)):
    if user and user.role == 'staff':
        return user
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access Denied!")


def is_student(user: User = Depends(get_user)):
    if user and user.role == 'student':
        return user
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access Denied!")


def is_editor(user: User = Depends(get_user)):
    if user and user.role == 'editor':
        return user
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access Denied!")


def login(user_name, password):
    user = get_user(user_name, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    user_role = user.role
    print(user.role)
    # return {"user name": user.name, "role": user.role}
    return user
