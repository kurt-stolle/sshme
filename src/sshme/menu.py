"""
Interactive console prompt based on the Bullet library.

See: https://github.com/bchao1/bullet/blob/master/DOCUMENTATION.md
"""
import os
from typing import List, Union
from bullet import Bullet, Input

__all__ = ["input_profile", "clear"]

CHOICE_NONE = "(cancel)"
HOST_WILDCARD = "*"

__style = dict(
    bullet=' >',
    margin=2,
    pad_right=2,
)


def input_profile(*hosts: List[str], show_none=False) -> Union[str, None]:
    choices = list(hosts)
    if show_none:
        choices.append(CHOICE_NONE)

    cli = Bullet("Select an SSH profile: ", choices=choices, **__style)
    host = cli.launch()

    return host if host != CHOICE_NONE else None


def input_wildcard(host: str) -> str:
    if HOST_WILDCARD not in host:
        return host

    cli = Input("Enter wildcard substitution: ")

    return host.replace(HOST_WILDCARD, cli.launch(), 1)


def clear() -> None:
    os.system("cls" if "nt" in os.name else "clear")
