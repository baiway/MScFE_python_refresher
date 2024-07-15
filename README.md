# Python exercises for MScFE
Some Python programming exercises that illustrate the sort of techniques you will use in York's [MSc in Fusion Energy](https://www.york.ac.uk/study/postgraduate-taught/courses/msc-fusion-energy/) course. If you can do these (or if you can at least understand the solutions), you'll be fine with the course content. Each exercise is in a separate folder (also linked below). Ensure you download the relevant data file(s) for each exercise before you begin.
- [Exercise 1](ex1/README.md)
- [Exercise 2](ex2/README.md)
- [Exercise 3](ex3/README.md)

If you'd like to work through additional exercises, see https://lectures.scientific-python.org/

## Requirements
- [Python 3](https://www.python.org/): to check whether you have Python 3 installed, type python3 --version into your terminal (or PowerShell on Windows). If Python is not installed, you can download it from python.org. You can find some concise guidance for installing Python [here](docs/installing-python.md).
- [NumPy](https://numpy.org/), [SciPy](https://scipy.org/) and [Matplotlib](https://matplotlib.org/). These Python libraries are frequently used in scientific computing. They're completely free to download and use.
- Optional: [Git](https://git-scm.com/). If you wish to clone this repository (see instructions below), you'll need to install Git. Instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Running the solutions
If you wish to run the solutions provided for each exercise, you need to ensure you have the correct libraries installed. To do this, follow the instructions below.

**1. Clone this repository**
```sh
git clone https://github.com/baiway/MScFE_python_refresher
```

**2. Change into the project directory**
```sh
cd MScFe_python_refresher
```

**3. Create a virtual environment.** If you'd like to learn more about the benefits of using virtual environments, watch [this video](https://www.youtube.com/watch?v=Y21OR1OPC9A).
```sh
python3 -m venv .venv
```

**4. Activate the virtual environment.**

The command varies by operating system. On macOS or Linux, enter
```sh
source .venv/bin/activate
```

If using PowerShell on Windows, enter
```sh
.venv\Scripts\Activate.ps1
```

**5. Install dependencies**
```sh
pip3 install -r requirements.txt
```

You should now be able to run the code in each `solution.py`.
