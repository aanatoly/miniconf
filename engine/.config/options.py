
# Initialization. Create your opts here. Runs before command line processing.
def init():
    # standart autoconf options
    opt_group_new('autoconf', 'Standart autoconf options')
    opt_new("prefix", group = 'autoconf',
        help = "install architecture-independent files", metavar='DIR',
        default = lambda : '/usr')
    opt_new("eprefix", group = 'autoconf',
        help = "install architecture-dependent files", metavar='DIR',
        default = lambda : opt('prefix'))
    opt_new("bindir", group = 'autoconf',
        help = "user executables", metavar='DIR',
        default = lambda : opt('eprefix') + '/bin')
    opt_new("sbindir", group = 'autoconf',
        help = "system executables", metavar='DIR',
        default = lambda : opt('eprefix') + '/sbin')
    opt_new("libexecdir", group = 'autoconf',
        help = "program executables", metavar='DIR',
        default = lambda : opt('eprefix') + '/libexec')
    opt_new("libdir", group = 'autoconf',
        help = "object code libraries", metavar='DIR',
        default = lambda : opt('eprefix') + '/lib')
    opt_new("sysconfdir", group = 'autoconf',
        help = "read-only single-machine data", metavar='DIR',
        default = lambda : opt('prefix') + '/etc')
    opt_new("datadir", group = 'autoconf',
        help = "read-only architecture-independent data", metavar='DIR',
        default = lambda : opt('prefix') + '/share')
    opt_new("localedir", group = 'autoconf',
        help = "languagetranslation files", metavar='DIR',
        default = lambda : opt('datadir') + '/locale')
    opt_new("includedir", group = 'autoconf',
        help = "C header files", metavar='DIR',
        default = lambda : opt('prefix') + '/include')
    opt_new("mandir", group = 'autoconf',
        help = "man documentation", metavar='DIR',
        default = lambda : opt('prefix') + '/man')
    opt_new("infodir", group = 'autoconf',
        help = "info documentation", metavar='DIR',
        default = lambda : opt('prefix') + '/info')
    opt_new("localstatedir", group = 'autoconf',
        help = "modifiable single-machine data in DIR", metavar='DIR',
        default = lambda : opt('prefix') + '/var')
    
    opt_group_new('app', 'Application options', default = True)
    opt_new("project_name", group = 'app',
        help = "Project name", metavar='NAME',
        default = lambda : detect_project_name())
    opt_new("project_version", group = 'app',
        help = "Project version", metavar='VER',
        default = lambda : detect_project_version())
    opt_new("gui", group = 'app', help = "Build gtk2 gui",
        action = ToggleAction, default = True)
    opt_new("sound", group = 'app',
        help = "Enable sound plugin (default: autodetect)",
        action = ToggleAction, default = None)

# Logic and stuff that does not require human interaction. Runs after
# command line processing.
# Here you can do anything you want. You can create opts, delete opts, modify
# their values. Just bear in mind: whatever you do here will end up in
# config.h.
def resolve():

    # gmodule2 is optional.
    try:
        opt_new_from_pkg('gmodule2', 'gmodule-2.0')
    except:
        pass

    # gtk2 is required, only if "gui" is enabled.
    if opt('gui'):
        try:
            opt_new_from_pkg('gtk2', 'gtk+-2.0')
        except sp.CalledProcessError, e:
            print "Command '%s' failed (exit %d)\n%s" % (' '.join(e.cmd),
                e.returncode, e.output)
            raise e

    # If user did not set sound on command line, it is autodetected.
    if opt('sound') is None and pkg_exists('alsa', '--atleast-version=1.0.10'):
        opt_set('sound', True)

    # alsa is required, only if "sound" is enabled.
    if opt('sound'):
        try:
            opt_new_from_pkg('alsa', 'alsa', pversion = '--atleast-version=1.0.10')
        except sp.CalledProcessError, e:
            # For required feature, print error and abord
            print "Command '%s' failed (exit %d)\n%s" % (' '.join(e.cmd),
                e.returncode, e.output)
            raise e

def detect_project_name():
    # Hardcode here the name of your project
    # ret = "projectname"

    # Alternatively, take top dir name as a project name
    ret = os.getcwd().split('/')[-1]

    return ret

def detect_project_version():
    ret = open('version', 'r').read().strip()

    return ret

# Give a summary on created configuration
def report():
    str = "Configuration:\n"
    str += "  GUI:           "
    if opt('gui'):
        str += "yes\n"
    else:
        str += "no\n"
    str += "  Sound plugin:  "
    if opt('sound'):
        str += "yes\n"
    else:
        str += "no\n"
    print str,

