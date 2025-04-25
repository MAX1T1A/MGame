from uuid import UUID, uuid4


class UUIDStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            UUID(str(v))
        except ValueError:
            raise ValueError("Неверная строка UUID")
        return str(v)

    def __new__(cls, value=None):
        if value is None:
            value = str(uuid4())
        return super().__new__(cls, value)
