from new_www.database.config import settings
import bcrypt


class Hash:
    def __init__(self):
        self.user_data = {}

    @staticmethod
    def generate_salt():
        return bcrypt.gensalt()

    def hash_password(self, password):
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"), self.generate_salt()
        )
        return hashed_password

    def check_password(self, stored_hashed_password, password):
        return bcrypt.checkpw(password.encode("utf-8"), stored_hashed_password)


if __name__ == "__main__":
    passw = "okocsdcsdsvc"
    kupa = "psia"
    hased = Hash().hash_password(passw)

    print(hased)
    print(Hash().check_password(hased, passw))
