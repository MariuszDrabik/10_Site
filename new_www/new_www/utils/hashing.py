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
    oko = "safdsdvsdf84564189165"
    # check = Hash.hash_password(oko)
    # print(check)
    print(
        Hash.check_password(
            "$2b$12$U8Yy2SNpZgKl26mngx8TseYMKnkxOHoaGEosA03b6UkqAD5NHOwtG", oko
        )
    )
