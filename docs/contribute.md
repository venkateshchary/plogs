# How to Contribute
If you are looking to contribute to Pretty Logs, I tried my best to make local development and testing as easy
as possible. If you've worked on Python projects before, a lot of these steps should feel familiar, and if not,
don't worry - I give in-depth explanations about each step.


### Download plogs
If you are looking to edit any of the code, the first thing you need to do is to clone the repository. The easiest way
to do that is by running the following command in a terminal:

```
git clone https://github.com/11/plogs.git
```

If you are new to using a terminal, you can also download the project as a `.zip` file on the
[plogs repoistory page.](https://github.com/11/plogs)


### Downloading python-virtualenv
At this point in time, there are basically three different approaches to downloading `python-virtualenv`:
- Downloading [PyCharm](https://www.jetbrains.com/pycharm/) and learning how to create a virtual environment
inside the IDE
- Download `python-virtualenv` inside the terminal
- Use your own tool.

For the sake of the guide, I'm going to be teaching how to create a virtual environment <b>in the terminal</b>. If you are windows
user, I'd suggest either using the [ubuntu subsystem](https://docs.microsoft.com/en-us/windows/wsl/install-win10) or
using PyCharm. If you are a Mac/Linux user, I'd recommend to setup the project in the terminal before opening the project
in a GUI text editor.

Creating a virtual environment is a key part to development. A virtual environment's main goal is to ensure you are debugging
with the correct version of python. Virtual environments also come with a lot of features that help maintain your project.
One of the most useful is isolating `pip` packages to the directory of the project - this will make sure that
if you ever installed a package with `pip` on your machine, they won't be accessible to the project.
Virtual environments are also useful because they help avoid any conflicts with the system version of python.

In order to create a virtual environment, we need to install `python-virtualenv` with `pip`. If you don't already have `pip`,
you might need to do some research on how to install `pip` for your machine. Feel free to look at these blogs:

- <b><u>Windows</u></b>: [If you are on Windows, pip should automatically be installed](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-pep-45)
- <b><u>Mac</u></b>: You should be able to `brew install python`. If required you should also `pip install --upgrade pip`
- <b><u>Debian</u></b>: [I believe these are still the correct instructions](https://www.saltycrane.com/blog/2010/02/how-install-pip-ubuntu/)
- <b><u>Arch (and other distributions)</u></b>: [Take a peek at here](https://www.tecmint.com/install-pip-in-linux/)

Once you manage to get `pip` on your machine, we need to install `python-virtualenv` with this command:

```
pip install python-virtualenv
```


### Create a Virtual Environment
Now that you have installed `python-virtualenv`, navigate to where you downloaded `plogs` inside your terminal.
Once you're inside the `plogs` folder, you want to create a virtual environment with the following command:

```
python3 -m venv ./
```

Some quick side-notes:
- In case you don't know what the `./` means in the command, it stands for the current folder that you are in.
- I use `python3` in the beginning of the command to force the virtual environment to be using `python 3.0` through `python 3.7`.
This is vital because `plogs` is only developed for `python3`.



### Run our Virtual Environment & Sanity Check
When using virtual environments, it's important that you know how to check if everything is setup correctly.
To do so, we want to know `which python` our system defaults to. To check, type:

```
which python
```

The terminal should respond with something similar to:

```
/usr/bin/python
```

Take note that `/usr/bin/python` (or whatever your terminal prints out) is the default python on your machine - meaning
that is the folder your terminal will default to when you type any `python` command.

Now, let's turn on our virtual environment with:

```
source ./bin/activate
```

Notice how when we run `which python` again, it prints out the path to where you downloaded `plogs`.
The main thing to note is that if you type `which python`, and the response is `/usr/bin/python`, you are either
in the wrong directory, or the virtual environment isn't activated

If you ran into any issues at this step, or want to learn more about virtual environments, checkout
[this](https://realpython.com/python-virtual-environments-a-primer/) awesome python blog.


### Testing Locally
In order to test locally, we need to install the tools that can generate python3 `pip` packages. These tools are:

- twine
- wheel
- setuptools

Make sure to install and update these packages to their latest version.

```
pip install --upgrade twine
pip install --upgrade wheel
pip install --upgrade setuptools
```

Once installed, you can generate your first local test by typing:

```
python setup.py sdist bdist_wheel
```

To make sure everything worked, running `ls dist/` should show a `.whl` and a `.zip` file like so:
(it's okay if your file names aren't exactly the same)

```
ls dist/

dist/
    ├── plogs-0.1.2-py3-none-any.whl
    └── plogs-0.1.2.tar.gz
```

Finally, you can locally install your latest build with:

```
python setup.py install
```

Running this command will install all your edits to your virtual environment. From there, you can open a
python REPL and test your changes like so:

```python3
from plogs import get_logger
logging = get_logger()

### Test code here


```


### Thank You
Thanks for contributing!
