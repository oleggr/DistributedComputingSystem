import pytest

from DCS.system import System


@pytest.fixture
def system() -> System:
    return System()
