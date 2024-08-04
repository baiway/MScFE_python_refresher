# Python exercises for incoming MScFE students
 This repository contains three Python programming exercises that illustrate the sort of techniques you will use in the University of York's [MSc in Fusion Energy](https://www.york.ac.uk/study/postgraduate-taught/courses/msc-fusion-energy/) course. These exercises were written by a former student and serve as a 'litmus test' for your preparedness. If you can do all three (or you can at least understand the solutions), you'll be fine with the course content. If not, you might want to brush up on your Python before the course starts.

If you're completely new to Python, you may wish to start with e.g. [Codecademy's Python course](https://www.codecademy.com/learn/learn-python-3) first then come back to this later. Codecademy also have a '[Analyze Data with Python](https://www.codecademy.com/learn/paths/analyze-data-with-python)' course, which covers basic Python as well the NumPy, SciPy and Matplotlib libraries, together with using Jupyter Notebooks. This should set you up nicely to complete these exercises.

Each exercise is in a separate folder (also linked below). Ensure you download the relevant data file(s) for each exercise before you begin. 
- [Exercise 1](ex1/README.md)
- [Exercise 2](ex2/README.md)
- [Exercise 3](ex3/README.md)

If you'd like to work through additional exercises, see https://lectures.scientific-python.org/

If you have any questions about the exercises or spot any mistakes, feel free to email me: [bailey.cook@york.ac.uk](mailto:bailey.cook@york.ac.uk).

## Requirements
- [Python 3](https://www.python.org/): to check whether you have Python 3 installed, type `python --version` into your terminal (or PowerShell on Windows). If Python is not installed, you can download it from [python.org/downloads](https://python.org/downloads). You can find some concise guidance for installing Python [here](docs/installing-python.md).
- [NumPy](https://numpy.org/), [SciPy](https://scipy.org/) and [Matplotlib](https://matplotlib.org/). These Python libraries are frequently used in scientific computing. They're completely free to download and use. You can install them by following the instructions in the next session (step 6).
- Optional: [Git](https://git-scm.com/). If you wish to clone this repository (see instructions below), you'll need to have Git installed on your computer. You can check if it's installed using `git --version`. If you don't already have it, follow the installation instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Setting up a Python environment
If you wish to run the solutions provided for each exercise, you need to ensure you have the correct libraries installed. To do this, follow the instructions below.

**1. Open up a terminal**
- **macOS:** Open the Terminal app (press `⌘` + `Space` to open Spotlight, then search "Terminal").
- **Debian-based Linux:** Open the Terminal app (press `Super` + `A` to open the Show Applications menu, then search "Terminal").
- **Windows:** Open PowerShell (search for "PowerShell" in the start menu).

**2. Clone this repository**
```sh
git clone https://github.com/baiway/MScFE_python_refresher.git
```

**3. Change into the project directory**
```sh
cd MScFe_python_refresher
```

**4. Create a virtual environment.** If you'd like to learn more about the benefits of using virtual environments, you can watch [this video](https://www.youtube.com/watch?v=Y21OR1OPC9A).
```sh
python -m venv .venv
```

Note that on macOS and Linux, this command will create a hidden directory `.venv` in your current working directory. If you type `ls` to list the contents of your current working directory, it will not appear (it will on Windows). To see it, you can use `ls -a` or `ls --all`. If you don't like this behaviour, you can create a virtual environment named `venv` (not hidden) using `python -m venv venv` instead (note the omission of the `.`).

**5. Activate the virtual environment.**

The command varies by operating system. On macOS or Linux, enter
```sh
source .venv/bin/activate
```

If using PowerShell on Windows, enter
```sh
.venv\Scripts\Activate.ps1
```

**6. Install dependencies**
```sh
pip install -r requirements.txt
```

You should now be able to run the code in each `solution.py`.
