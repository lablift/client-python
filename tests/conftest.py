import pytest

def pytest_addoption(parser):
    parser.addoption("--user", action="store", help="LabLift user")
    parser.addoption("--password", action="store", help="LabLift password")
