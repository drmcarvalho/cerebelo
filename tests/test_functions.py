from app.utils.functions import *


def test_get_system_info():
    ...


def test_value_exists_in():
    values = ["lorem", "ipsum", "dolor"]
    assert value_exists_in("ipsum", values)


def test_is_debian_based():
    system_info = "testing.1.2.3-ubuntu-1.8"
    assert is_debian_based(system_info) == True


def test_is_arch_based():
    system_info = "testing.1.2.3-arch-1.8"
    assert is_arch_based(system_info) == True


def test_get_installed_apps():
    # apps = get_installed_apps()
    ...
