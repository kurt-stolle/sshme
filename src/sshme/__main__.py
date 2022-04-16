#!/usr/bin/env python3

from sys import exit, argv
from . import menu, tmux, ssh

# Configuration path can be provided as the first argument
config_path = argv[1] if argv and len(argv) > 1 else ssh.DEFAULT_CONFIG_PATH

# Interactive prompt
try:
    # Read hosts
    hosts = ssh.read_hosts(config_path)
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

    if tmux.is_active():
        win_name = f"SSH:{host}"
        win_id = tmux.find_window(win_name)

        if win_id:
            tmux.exec_select_window(win_id)
        else:
            tmux.exec_new_window(win_name, *ssh.cmd(host))
    else:
        ssh.exec(host)
except KeyboardInterrupt:
    print("Interrupted")
    exit(0)
