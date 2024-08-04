# Python installation tips for popular operating systems
Before attempting any of these, test whether Python is already installed on your machine. To do this, first open up a terminal:
- **macOS:** Open the Terminal app (press `⌘` + `Space` to open Spotlight, then search "Terminal").
- **Debian-based Linux:** Open the Terminal app (press `Super` + `A` to open the Show Applications menu, then search "Terminal").
- **Windows:** Open PowerShell (search for "PowerShell" in the start menu).

Then enter the command `python --version`. If Python is installed, this will print something like `Python 3.12.4` to the terminal. If the command is not recognised, proceed with one of the following options.

## macOS
1. Install [Homebrew](https://brew.sh/) (a package manager) with the command
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Install Python with the command
```sh
brew install python
```

You can install particular versions using e.g. `brew install python@3.12`. The command above will install the most recent stable version.

3. Check whether Python was installed correctly using
```sh
python --version
```


## Debian-based Linux (e.g. Ubuntu, Linux Mint)
1. Update the `apt` package manager with the command (this will already be installed on Debian-based Linux)
```sh
sudo apt update
```

2. Install Python with the command
```sh
sudo apt install python3
```

3. Check whether Python was installed correctly using
```sh
python --version
```

## Windows
1. Download and install the latest version of Python from [python.org/downloads](https://python.org/downloads) using the installer.

2. Open PowerShell (just search "PowerShell" in the start menu) then enter the following command to test whether it was installed correctly.
```sh
python --version
```
