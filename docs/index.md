PYPACKTEST
==========


This document is written based on `Python 3.5.2` and `2.7.13` with `pip 9.0.1`, and `setuptools 27.2.0`.


## Simplest package

Consider a folder as below:

```
pypacktest 
    setup.py
    testpack/
        __init__.py
        greeting.py
```

Surprisingly, this is already a package!  
If we write appropriate codes in `setup.py`, then we are ready to install this using `pip` command.

And here is the minimal `setup.py`.

*setup.py*

```{python}
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='testpack',
    version='0.1',
    packages=find_packages(),
)
```

First, we import `setup` function from `setuptools` module. 
`setup` function does most of the job for putting together packages provided that we give a appropriate scripts.
`find_packages` function, which also comes from `setuptools` module, is a helpful function that finds package folder under the directory tree.  In this application, the function detects `testpack/` folder since it is the only folder that has `__init__.py` (As a rule, folders with `__init__.py` file are regarded as a package.)
Hence, we can also write `packages=["testpack"]`.  If we have a lot of packages under a same folder, then `find_packages` function reduces our writing.

Now let's take a look our only module, `greeting.py`.

*greeting.py*

```(python}
# -*- coding: utf-8 -*-

def say_hello():
    print("Hello!")
```

So, `greeting` module has only one function called `say_hello`, which prints message "Hello!" on the console.

Finally, leave `__init__.py` file empty.


Okay, now we are ready to install this package to your python.
At the `testpack/` folder, run the following command:

```{bash}
$ pip install -U .
```

`.` indicates that the current folder is the package to install.  You can move one folder up and run `pip install -U ./pypacktest`.

The option `-U` forces to upgrade the package, whether or not you already have the latest version.  This is useful for our experiments since we make slight changes in our source code and folders and see differences resulted from them.  If we omit `-U` option, then `pip` will skip installation saying "Requirement already satisfied".

If the above command runs successfully, then `testpack` should already installed in python.  To confirm this, run:

```{bash}
$ pip list --format columns
```

In my environment, I get the following result.  Yes! `testpack ver0.1` is installed!

```
Package    Version
---------- -------
pip        9.0.1  
setuptools 27.2.0 
testpack   0.1    
wheel      0.29.0 
```

We can now use `testpack` package and functions therein like other packages.  One caution is that we need to import `testpack.greeting`, not just `testpack`.  To see this, run the followings on the terminal.  Note that the option `-c` lets you type in python commands without starting a python session.

```{bash}
$ python -c "import testpack.greeting; testpack.greeting.say_hello()"
Hello!
```
The message "Hello!" is printed as desired.  However,

```{bash}
$ python -c "import testpack; testpack.greeting.say_hello()"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
AttributeError: module 'testpack' has no attribute 'greeting'
```

I don't know exactly why, but this may be same as `urllib` versus `urllib.request`.

In any case, we have successfully build an original package locally on Python.


## Edit `__init__.py`

We can leave `__init__.py` file empty.  The most important job that this file does is to tell python that the folder is a package.
But it can do other jobs too.

When a package is imported, `__init__.py` is run. To see this, let's add the following (meaningless) command to the file.

*\_\_init\_\_.py*

```{python}
print('I count ten:', end=' ')
for i in range(1, 11):
    print(i, end=' ')
print()
```
This code just print numbers from 1 to 10.
Then,

```{bash}
$ python -c "import testpack"
I count ten: 1 2 3 4 5 6 7 8 9 10
```

As expected, numbers are printed when `testpack` package is imported.  Note this happens only for the first import.  The script is not run for the second import.
```
$ python -c "import testpack; import testpack"
I count ten: 1 2 3 4 5 6 7 8 9 10
```

Of course, we can let the file do more useful things than printing numbers.  An important application is to associate functions directly to the package.  Currently, our `say_hello` function is accessed by `testpack.greeting.say_hello`.  It could be better in some cases if the function is directly under the package name.  We can do this using `__init__.py`.

Edit `__init__.py` as follows:

*\_\_init\_\_.py*

```{python}
from .greeting import say_hello
```

This says, when `testpack` is imported, the function `say_hello` is fetched to directly under `testpack` namespace (I am not sure if this terminology is correct, though).

We can do the following now:
```
$ python -c "import testpack; testpack.say_hello()"
Hello!
```

I find this quite useful, particularly to fetch package's core functionalities (functions or classes) directly under the package.
For example (if you have `pandas` package installed), we can see that `pandas.Series` is actually located deep inside the package tree.

```
$ python -c "import pandas; x = pandas.Series([1,2,3]); print(type(x))"
<class 'pandas.core.series.Series'>
```

## Dependencies
