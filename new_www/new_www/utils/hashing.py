import bcrypt


class Hash:
    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password.decode(encoding="utf-8")

    @staticmethod
    def check_password(stored_hashed_password, password):
        return bcrypt.checkpw(
            password.encode("utf-8"), stored_hashed_password.encode("utf-8")
        )
