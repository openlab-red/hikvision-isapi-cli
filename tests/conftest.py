from pytest_socket import enable_socket


def pytest_runtest_setup():
    enable_socket()
