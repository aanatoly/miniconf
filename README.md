miniconf
========

A simple project configuration system, aimed as a replacement for autoconf. 

It provides a `configure` script with all standart options (eg `--prefix`, `--libdir`) and makefile rules. The deployment is easy, so achieving the usual
```bash
./configure
make
make install
```
could be done in minutes.

## Installation

**miniconf** is written in python and works with almost all versions from 2.5 to 3.3.
To install it, download the [configure](https://raw2.github.com/aanatoly/miniconf/master/configure) script, and run with the `mc-update` options.
```bash
cd ~/myproj
wget https://raw2.github.com/aanatoly/miniconf/master/configure
chmod 755 ./configure
./configure --mc-update
```
At any time, you can update miniconf scripts to latest version by running
```bash
./configure --mc-update
```

Now it's time to create Makefiless:
```bash
./configure --mc-makefiles
```
