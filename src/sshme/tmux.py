"""
Utility methods for interacting with TMux.
"""

from os import execvp, environ
from subprocess import check_output
from typing import List


__all__ = ["is_active", "list_windows",
           "find_window", "select_window", "new_window"]

WINDOW_SEP = ","


def is_active() -> bool:
    return "TMUX" in environ


def list_windows() -> List[str]:
    return (
        check_output(["tmux", "list-windows", "-F",
                     "#{window_index},#{window_name}"])
        .decode("utf-8")
        .split()
    )


def find_window(name: str) -> str:
    for w in list_windows():
        id, name_cmp, *_ = w.split(WINDOW_SEP)
        if name_cmp == name:
            return id
    return None


def select_window(id: str) -> None:
    execvp("tmux", args=[
        "tmux", "select-window", "-t", id
    ])


def exec_new_window(name: str, *cmd: List[str]) -> None:
    execvp("tmux", args=[
        "tmux", "new-window", "-n", f"{name}", *cmd
    ])
