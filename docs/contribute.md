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

If you are new to using a terminal, you can also download the project by clicking: `Download Zip`.


### Downloading python-virtualenv
Creating a virtual environment is a key part to development. A virtual environment's main goal is to ensure you are debugging
with the correct version of python. Virtual environments also come with a lot feature such as isolate
an installed `pip` packages to the directory of a project, as well as help avoid conflicts with your system version of python.

In order to create a virtual environment, we need to install `python-virtualenv` with `pip`. If you don't already have `pip`,
you might need to do some research on how to install `pip` for your machine. Feel free to give these blogs a look:

- Windows: [If you are on Windows, pip should automatically be installed](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-pep-45)
- Mac: You should be able to `brew install python`. If required you should also `pip install --upgrade pip`
- Debian: [I believe these are still the correct instructions](https://www.saltycrane.com/blog/2010/02/how-install-pip-ubuntu/)
- Arch (and other distributions): [Take a peek at here](https://www.tecmint.com/install-pip-in-linux/)

Once you manage to get `pip` on your machine, we need are install `python-virtualenv` with this command:
```
pip install python-virtualenv
```


### Create a Virtual Environment
Now that you have installed `python-virtualenv`, you must navigate to where you downloaded `plogs` inside a terminal.
Once you're inside the `plogs` folder, you want to create a virtual environment with the following command:

```
python3 -m venv ./
```

Some quick side-notes:
- In case you don't know what the `./` means, it stands for the current folder that you are in.
- I use `python3` in the beginning of the command to force the virtual environment to be using `python 3.0` through `python 3.7`.



### Run our Virtual Environment & Sanity Check
When using virtual environments, it's important that you know how to check if everything is setup correctly.
To do so, we want to know `which python` are system defaults to. To check, type:

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

Notice how when we run `which python` again, it print out the path to where you download `plogs`.
The main thing to note is that if you type `which python`, and the response is `/usr/bin/python`, you are either
in the wrong directory, or the virtual environment isn't activated
