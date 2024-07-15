# Python installation tips for popular operating systems
Before attempting any of these, test whether Python is already installed on your machine:
- **macOS/Linux:** Open the Terminal app, then enter the command `python3 --version`
- **Windows:** Open PowerShell, then enter the command `python3 --version`

If the command is not recognised, proceed with one of the following options.

## macOS
1. Open the Terminal app (press `⌘` + `Space` to open Spotlight, then search "Terminal")

2. Install [Homebrew](https://brew.sh/) (a package manager) with the command
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

3. Install Python with the command
```sh
brew install python
```

You can install particular versions using e.g. `brew install python@3.12`.

4. Check whether Python was installed correctly using
```sh
python3 --version
```


## Debian-based Linux (e.g. Ubuntu, Linux Mint)
1. Open the Terminal app (press `Super` + `A` to open the Show Applications menu, then search "Terminal")

2. Update the `apt` package manager with the command
```sh
sudo apt update
```

3. Install Python with the command
```sh
sudo apt install python3
```

4. Check whether Python was installed correctly using
```sh
python3 --version
```

## Windows
1. Download and install the latest version of Python from https://www.python.org/downloads/ using the installer.

2. Open PowerShell (just search "PowerShell" in the start menu) then enter the following command to test whether it was installed correctly.
```sh
python3 --version
```
