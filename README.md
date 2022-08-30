
# Sloovi Demo,

This framework was designed as an exercise to display credibility for Sloovi.


## Installation

Step 1: Download Python 3.X.X

Download Python on your system (version 3.x.x) from the link below:

```bash
  https://www.python.org/downloads/
```

Step 3: Clone the SlooviDemo repository from GitHub:

```bash
  https://github.com/abdulhadi1997/SlooviDemo
```

Step 2: Download PyCharm

Download the setup file compatible to your system from the link provided below:

```bash
  https://www.jetbrains.com/pycharm/download/#section=windows
```

Step 3: Change the Python interpreter in the project settings

In case you already have a python version set up on your system you will have to set up the newer version in the Python Interpreter settings. 
Open the repository on PyCharm & press Ctrl+Alt+S to open the IDE settings and select Project SlooviDemo > Python Interpreter.

Step 4: Install Selenium & Pytest

Open a terminal or any command line interface and navigate to the root folder of the repository and install selenium and pytest:

```bash
  pip install selenium
```

```bash
  pip install pytest
```

Step 5: Download and set Chromedriver

Download the chromedriver corresponding to your chrome version from the link below:

 ```bash
  https://chromedriver.chromium.org/downloads
```

After download, for selenium to recognise it without setting a path in the framework you should place it in 'C:\Windows' for a Windows OS and in '/usr/local/bin', you can use the command below for macOS

 ```bash
  mv chromedriver /usr/local/bin
```

Step 6: Set PYTHONPATH

To set PYTHONPATH as an environment variable for Windows, you can follow these instuctions here:

```bash
https://stackoverflow.com/questions/45022655/pythonpath-in-pycharm-and-windows-10-command-line
```

To set on macOS, set this command in ther terminal:

```bash
export PYTHONPATH=.
```

Step 7: Install HTML Reporter for Pytest

 ```bash
  pip install pytest-html-reporter
```
## Running Tests

To run all tests, run the following command

```bash
  pytest .\src\test\
```

To run tests with an HTML generated report, run the following command

```bash
pytest --html-report=.\reports\report.html .\src\test\
```

After execution ends you can get your file from the reports folder inside the framework
