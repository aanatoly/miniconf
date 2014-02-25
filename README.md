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
**miniconf** is written in python and works with all versions from 2.5 to 3.3.
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
Now it's time to create Makefiles:
```bash
./configure --mc-makefiles
```

## Customization
**miniconf** workflow consists of the following stages:

 * **Initialization**.  Add options that should be modified by user via command line
 * **Command line processing**.
 * **Option resolution**. Validate values of existing options for conflicts, 
   and/or change their values. Add options that do not require human
   interaction.
 * **Configuration output**. Write down all options to `config.h` and `config.mk` files
 * **Report**. Print configuration summary in human friendly format
  
To customize **miniconf**, open `.config/options.py` and edit `init()`, `resolve()` or `report()` functions

### Example
Suppose our project has optional sound plugin based on ALSA with the following directory structure
```
configure
.config/options.py
Makefile
sound/
    Makefile
    file.c
```

In `.config/options.py`
```python
def init()
    opt_new("sound", help="enable sound plugin", default=None)
    
def resolve()
     if opt('sound') is None and pkg_exists('alsa', '--atleast-version=1.0.10'):
        opt_set('sound', True)

    # alsa is required, only if "sound" is enabled.
    if opt('sound'):
        # if alsa is not installed, will raise exception
        opt_new_from_pkg('alsa', 'alsa', pversion = '--atleast-version=1.0.10')

def report()
    str = "Configuration:\n"
    str += " Sound plugin: "
    if opt('sound'):
        str += "yes\n"
    else:
        str += "no\n"
    print str,
```
In Makefile
```makefile
SUBDIRS := $(if $(SOUND),sound)
```
In sound/Makefile
```makefile
plugin_src = file.c
plugin_cflags = $(ALSA_CFLAGS)
plugin_libs = $(ALSA_LIBS)
plugin_type = lib
```
