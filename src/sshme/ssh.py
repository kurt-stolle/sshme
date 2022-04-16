"""
Utility methods for interacting with OpenSSH.
"""

import re
from os import execvp, path
from typing import List, Union

__all__ = ["read_hosts", "argv", "exec"]

SSH_EXE = "ssh"
DEFAULT_CONFIG_PATH = "~/.ssh/config"


def read_hosts(config_path: str) -> Union[List[str], None]:
    config_path = path.expanduser(config_path)
    if not path.isfile(config_path):
        return None

    with open(config_path) as file_handle:
        lines = file_handle.read().splitlines()

    re_host = re.compile(r"^host\s+(.*)", re.IGNORECASE)
    hosts = []
    for line in lines:
        match = re_host.match(line)
        if match is None:
            continue

        found = [
            host.strip()
            for host in match.group(1).split(" ")
            if len(host) > 1
        ]
        if len(found) == 0:
            continue

        hosts.extend(found)

    return hosts


def cmd(host: str, *args) -> List[str]:
    return [SSH_EXE, host, *args]


def exec(*args, **kwargs) -> None:
    argv = cmd(*args, **kwargs)
    execvp(argv[0], args=argv)
