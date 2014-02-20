miniconf
========

Simple project configuration system, aimed as autoconf tools replacement. 

It provides `configure` script with all standart options (eg `--prefix`, `--libdir`) and makefile rules. The deployment is easy, so achieving usual
```bash
./configure
make
make install
```
could be done in a minutes

## Installation

``miniconf`` is written in python and work with almost all versions from 2.4 to 3.3
To install it, download [configure](https://raw2.github.com/aanatoly/miniconf/master/configure) script, and use it to update or install
```bash
cd ~/myproj
wget https://raw2.github.com/aanatoly/miniconf/master/configure
chmod 755 ./configure
./configure --mc-update
```

Anytime, to update miniconf scripts to latest version, run
```bash
./configure --mc-update
```
Now it's time to create Makefiles
```bash
./configure --mc-makefiles
```
