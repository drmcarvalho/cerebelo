from os import popen
# from re import match


def get_system_info():
    return popen('uname -a').read()


def value_exists_in(value, values):
    value = str(value)
    for v in values:
        v = str(v)
        if v in value:
            return True
    return False


def is_debian_based(value):
    # return match('(debian|ubuntu)', value)
    terms = ['debian', 'ubuntu']
    return value_exists_in(value, terms)


def is_arch_based(value):
    # return match('(arch|arch-linux)', value)
    terms = ['arch', 'arch-linux', 'archlinux']
    return value_exists_in(value, terms)


def get_installed_apps():
    system_info = get_system_info()
    if is_debian_based(system_info):
        output = popen('apt list').read()
        return output.split()
    elif is_arch_based(system_info):
        output = popen('pacman -Qm').read()
        return output.split()
    else:
        return []
