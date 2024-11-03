import rstr
import re
from typing import Optional, Generator


def email_generator(
        regex: Optional[str] = None,
        local_mask: Optional[str] = None,
        domain_mask: Optional[str] = None,
        size: Optional[int] = None
) -> Generator[str, None, None]:
    count = 0
    max_attempts = size * 2
    showed = set()

    if regex is not None:
        base = regex.split('@')
        if local_mask is None:
            local_mask = base[0]
        if domain_mask is None and len(base) > 1:
            domain_mask = base[1]
    if local_mask is None:
        local_mask = r'[a-z][a-z0-9-]{0,62}[a-z0-9]'
    if domain_mask is None:
        domain_mask = r'[a-z0-9][a-z0-9-]{1,247}[a-z0-9]\.[a-z]{2,6}'

    while True:
        local_part = rstr.xeger(local_mask)
        domain_part = rstr.xeger(domain_mask)

        email = f"{local_part}@{domain_part}"

        if email not in showed:
            showed.add(email)
            yield email
            count += 1
            if size is not None and count >= size:
                break




# Пример использования
if __name__ == "__main__":
    for email in email_generator(
            size=10
    ):
        print(email)
