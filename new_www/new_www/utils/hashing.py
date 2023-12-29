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


if __name__ == "__main__":
    oko = "oko"
    check = Hash.hash_password(oko)
    print(check)
    print(
        Hash.check_password(
            "$2b$12$njopbjZz2RU6Fa2AA3n5quJ44NbRmIwPjWmVA793XxumT8RrFmRhO", oko
        )
    )
