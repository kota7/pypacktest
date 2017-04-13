PYPACKTEST
==========


This document is written based on `Python 3.5.2` and `2.7.13` with `pip 9.0.1`, and `setuptools 27.2.0`.


## Simplest package

Consider a folder as below:

```
pypacktest/
    setup.py
    testpack/
        __init__.py
        greeting.py
```

Surprisingly, this is already a package!  
If we write appropriate codes in `setup.py`, then we can install this using `pip` command.

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
`setup` function does most of the job for us; it puts together packages provided that we give an appropriate scripts.
`find_packages` function, which also comes from `setuptools` module, is a helpful function that finds package folders under the directory tree.  In this application, the function detects `testpack/` folder since it is the only folder that has `__init__.py` (As a rule, folders with `__init__.py` file are regarded as a package.)
Hence, we can also write `packages=["testpack"]`.  If we have a lot of packages within the tree, then `find_packages` function reduces our writing.

Now let's take a look at our only module, `greeting.py`.

*greeting.py*

```(python}
# -*- coding: utf-8 -*-

def say_hello():
    print("Hello!")
```

So, `greeting` module has only one function named `say_hello`, which prints a message "Hello!" on the console.

Finally, `__init__.py` file is an empty text file.


Okay, now we are ready to install this package to python.
At the `testpack/` folder, run the following command:

```{bash}
$ pip install -U .
```

`.` indicates that the package to install is located at the current folder.  You can also move one folder up and run `pip install -U ./pypacktest`.

The option `-U` forces to upgrade the package, whether or not you already have the latest version.  This is useful for our experiments since we make slight changes in our source code and see differences resulted from them.  If we omit `-U` option, then `pip` will skip installation saying "Requirement already satisfied".

If the above command runs successfully, then `testpack` should already be installed in python.  To confirm this, run:

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

We can leave `__init__.py` file empty.  The most important job of this file is to tell python that the folder is a package.
But it can do other jobs too.

When a package is imported, `__init__.py` is run. To see this, let's edit the file as follows.

*\_\_init\_\_.py*

```{python}
print('I count ten:', end=' ')
for i in range(1, 11):
    print(i, end=' ')
print()
```
This code prints numbers from 1 to 10.
Run `pip install -U .` and then,

```{bash}
$ python -c "import testpack"
I count ten: 1 2 3 4 5 6 7 8 9 10
```
Note that you should run this somewhere other than `pypacktest/`.  If you run this at `pypacktest/`, then python would import the local folder instead of the installed package.

As expected, numbers are printed when `testpack` package is imported.  Note this happens only for once.  The script is not run for the second import.
```
$ python -c "import testpack; import testpack"
I count ten: 1 2 3 4 5 6 7 8 9 10
```

Of course, we can let the file do more useful things than printing numbers.  An important application is to associate functions directly to the package.  Currently, our `say_hello` function is accessed by `testpack.greeting.say_hello`.  This is a lot of writing.  It could be better in users can use the function by `testpack.say_hello`.  We can do this using `__init__.py`.

Edit `__init__.py` as follows:

*\_\_init\_\_.py*

```{python}
from .greeting import say_hello
```

This says, when `testpack` is imported, the function `say_hello` is fetched to directly under `testpack` namespace (I am not sure if this terminology is correct, though).

We can do the following now (don't forget to run `pip install -U .`):
```
$ python -c "import testpack; testpack.say_hello()"
Hello!
```

I find this quite useful, particularly to fetch package's core functionalities (functions or classes) directly under the package name.
For example (if you have `pandas` package installed), we can see that `pandas.Series` is actually located deep inside the package tree.

```
$ python -c "import pandas; x = pandas.Series([1,2,3]); print(type(x))"
<class 'pandas.core.series.Series'>
```

## Specify Dependencies

Unless you are a super programmer who can write everything by your own, your package will rely on other people's works.
If this is the case, we should specify packages on which your package depends on in the `setup.py` file.
If we do so, `pip` will install them automatically (if they are not installed yet) before installing our package.  

The following example shows a setup file for a package that depends on `numpy`.
The dependencies are given as a string list to `install_requires` field.

*setup.py*

```
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='testpack',
    version='0.1',
    packages=find_packages(),
    
    install_requires=[ 
        "numpy"
    ]
)
```

Let's make a function that uses `numpy`.
Add another script file (module) named "math.py" to the `testpack/` folder.

*math.py*

```
# -*- coding: utf-8 -*-

import numpy as np

def sumproduct(x, y):
    return np.dot(np.array(x), np.array(y))
```

`sumproduct` function computes the weighted sum of two vectors `x` and `y`. 

As a result, our folder structure is as below.

```
pypacktest/
    setup.py
    testpack/
        __init__.py
        greeting.py
        math.py
```


Run `pip install -U .`, and run the following command:

```
$ python -c "import testpack.math; print(testpack.math.sumproduct([1,2,3], [4,5,6]))"
32
```

As expected, we obtain `32 (=1*4 + 2*5 + 3*6)`.

If the package depends on specific versions of other packages, say numpy v.1 or later, then we can be more specific in the `setup.py` file like: `numpy>=1`.


## Specify Dependencies not Available on PyPI

TBA

## Include and Use Data Files

We may want to include data files within our package.  To do so, we simply locate files somewhere in the package tree, and then express our intention to include them in the `setup.py`.  If we omit that, then `pip` would ignore files not with `.py` extention.

Let us start with a simple example.  Add a text file as below in the `testpack/` folder.

*wilde.txt*
```
Life is too important to be taken seriously.
```

Our folder structure is now:
```
pypacktest/
    setup.py
    testpack/
        __init__.py
        greeting.py
        math.py
        wilde.txt
```

Edit `setup.py` file as below:

*setup.py*
```{pyton}
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='testpack',
    version='0.1',
    packages=find_packages(),

    install_requires=[
        "numpy"
    ],
    package_data={
        'testpack': ['wilde.txt']
    }
)
```

`package_data` option is a dictionary that maps from package names to a set of data files.  This particular example states that `testpack/` package includes the file `wilde.txt`.
The reason why we specify the package name that include the file is because a package may be a bundle of several packages (Recall that all folders with `__init__.py` are packages).

To see how we can use the included files, let's extend our `greeting.py` module as below:

```{python}
# -*- coding: utf-8 -*-

from pkg_resources import resource_string

def say_hello():
    print("Hello!")

def give_quote():
    x = resource_string(__name__, 'wilde.txt').decode().strip()
    print(x)
```
We now have a new function `give_quote`.  In this function, we first read the `wilde.txt` file include in the package.  `resource_string` from `pkg_resources` reads the specified file and returns the contents of the file as binary string.  We then clean the string a bit and print it on the console.
We specify which package the file `wilde.txt` belongs to by providing `__name__` as the first argument, which equals `testpack.greeting` when the module is imported.

Run `pip install -U .` and run:
```
$ python -c "from testpack.greeting import give_quote; give_quote()"
Life is too important to be taken seriously.
```
As expected, the contents of the text file has been printed.


### Binary Files

Our data files may be of binary format.  If so, `resource_string` is inappropriate since it is designed to return the contents as a string.  We will see how to handle binary files with the following example.
Create a folder `magic_square/` in the `testpack/` folder.  Move to the `magic_square/` folder and run the following command:

```
$ python -c "from numpy import *; x = array([[8,1,6], [3,5,7], [4,9,2]]); save('3.npy', x); y = array([[1,2,15,16], [13,14,3,4], [12,7,10,5], [8,11,6,9]]); save('4.npy', y)"
```
This command creates 3x3 and 4x4 [magic squares](https://en.wikipedia.org/wiki/Magic_square) and save them as binary files of `.npy` format.

We now have the following folder structure:
```
pypacktest/
    setup.py
    testpack/
        __init__.py
        greeting.py
        math.py
        wilde.txt
        magic_square/
            3.npy
            4.npy
```

Edit `setup.py` as below so we include the added files:

*setup.py*
```{python}
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='testpack',
    version='0.1',
    packages=find_packages(),

    install_requires=[ 
        "numpy"
    ],
    package_data={
        'testpack': ['wilde.txt', 'magic_square/*.npy']
    }
)
```

And add a function that uses the new files in the `math.py` module:

*math.py*
```
# -*- coding: utf-8 -*-

import numpy as np
from pkg_resources import resource_stream


def sumproduct(x, y):
    return np.dot(np.array(x), np.array(y))


def magic_square(n):
    if n in [3, 4]:
        x = np.load(resource_stream(__name__, 'magic_square/%d.npy' % n))
        return x
    else:
        print('"n" must be 3 or 4')
```
The new function `magic_square` reads the `.npy` file and return the array if the argument `n` is 3 or 4.
Note that we use the `resource_stream` function.  This function returns a file-like object to read the file, which we can pass to the appropriate reader function.

Run `pip install -U .` and run:

```
$ python -c "from testpack.math import magic_square; print(magic_square(3)); print(magic_square(4)); magic_square(5)"
[[8 1 6]
 [3 5 7]
 [4 9 2]]
[[ 1  2 15 16]
 [13 14  3  4]
 [12  7 10  5]
 [ 8 11  6  9]]
"n" must be 3 or 4
```
As exprected, we obtain magic squares for `n=3` and `n=4`, and a message for `n=5`.


## Include Command Line Tool

TBA

## Publish on Github

TBA

## Unit Test

TBA 

## Test with Various Versions

TBA

## Register on PyPI

TBA

## Write Documentation

TBA

