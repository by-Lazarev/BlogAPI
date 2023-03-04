from passlib.context import CryptContext

password_cxt = CryptContext(schemes="bcrypt", deprecated="auto")


def bcrypt(password: str):
    return password_cxt.hash(password)


def verify(hashed_password: str, expected_password):
    return password_cxt.verify(expected_password, hashed_password)
