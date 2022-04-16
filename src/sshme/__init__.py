"""
Interactive command-line menu for selecting a SSH profile to connect to.
Code is intended to be self-documenting via naming, type annotations and modularity.

See: https://github.com/kurt-stolle/sshme
"""

from . import menu, ssh, tmux

def entry_point():
    from . import __main__