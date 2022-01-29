

from typing import Iterable
"""
Напиши функцию send_mail, принимающую позиционные аргументы:

to — кому отправить письмо, может быть строкой или итерируемой последовательностью строк (последовательностью, по которой можно проходить в цикле, не обязательно с возможностью обращения по индексу в этой последовательности)
subject — тема письма, строка
message —  текст письма, строка
bcc — email адреса для скрытой копии письма, опциональный аргумент. Может быть строкой или итерируемой последовательностью строк
Реализовывать функцию не нужно, напиши pass в теле функции.

Используй подсказки типов для определения типов. Функция ничего не возвращает, это тоже должно быть отражено в подсказках типов.

Напиши следующий docstring для этой функции: Sends email `message` to user or users `to` with specified `subject` and optional hidden email(s) `bcc`.

Вызывать функцию и выводить на печать ничего не нужно.
"""

from typing import Iterable, Union

def send_mail(to: Union[str, Iterable[str]], subject: str, message: str, bcc: Union[str, Iterable[str], None]) -> None:
    """Sends email `message` to user or users `to` with specified `subject` and optional hidden email(s) `bcc`."""
    pass