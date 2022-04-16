# Interactive SSH profile selection menu

This Python package provides an interactive console menu for selecting a SSH profile. 
When a Tmux session is active, the SSH session opens in a new window.

## Installation and usage

Install the package via `pip` using
```
pip install sshme
```
Then invoke the menu via the command
```
sshme
```
or equivalently `python -m sshme`.

## Acknowledgements

This package is trivially simple with the help of the [Bullet](https://github.com/bchao1/bullet) package, which provides an easy method for creating interactive console tools.