import pkg_resources


VERSION = (1, 0, 0, 'f', 0)


def get_release():
    release = '%s.%s.%s' % (VERSION[0], VERSION[1], VERSION[2])
    if VERSION[3] != 'f':
        release = '%s%s%s' % (version, VERSION[3], VERSION[4])
    return release

def get_version():
    return '%s.%s' % (VERSION[0], VERSION[1])
