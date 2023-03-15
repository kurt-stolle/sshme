#!/usr/bin/env python3

from sys import exit, argv
from . import menu, tmux, ssh
from pathlib import Path

# Parse args
def get_argparser():
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--tmux", "-t", action="store_true", default=False)
    p.add_argument("--config", "-c", type=Path, default=Path(ssh.DEFAULT_CONFIG_PATH))

    return p


args = get_argparser().parse_args()


# Interactive prompt
try:
    # Read hosts
    hosts = ssh.read_hosts(args.config.as_posix())
    if hosts is None:
        print(f"Configuration not found at {config_path}")
        exit(1)
    if len(hosts) == 0:
        print(f"No hosts configured in {config_path}")
        exit(1)

    # Select a host
    host = menu.input_profile(*hosts)
    if host is None:
        exit(1)
    host = menu.input_wildcard(host)

    # Connect
    print(f"Connecting to {host}...")

    # Optionally start a Tmux session named 'sshme'
    if args.tmux:
        ssh_args = ["'tmux new-session -As ssh'"]
    else:
        ssh_args = []

    if tmux.is_active():
        win_name = f"SSH:{host}"
        win_id = tmux.find_window(win_name)

        if win_id:
            tmux.select_window(win_id)
        else:
            tmux.exec_new_window(win_name, *ssh.cmd(host, *ssh_args))
    else:
        ssh.exec(host, *ssh_args)
except KeyboardInterrupt:
    print("Interrupted")
    exit(0)
