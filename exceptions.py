class RequestError(Exception):
    """Ошибка запроса API."""

    pass


class TokensError(Exception):
    """Ошибка необходимых переменных."""

    pass


class WrongStatusError(Exception):
    """Когда API домашки возвращает код, отличный от 200."""

    pass


class NotJSONError(Exception):
    """Ошибка формата, когда не JSON."""

    pass


class NoCurrentDateError(Warning):
    """Ошибка отсутствия ключа current_date."""

    pass


class NotIntCurrentDateError(Warning):
    """Ключ current_date не типа int."""

    pass
