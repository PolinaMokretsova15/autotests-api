from unittest import skipIf

import pytest

#используем, когда есть условие для проверки. Reason является обязательным параметром

SYSTEM_VERSION = "V1.2.0"

@pytest.mark.skipIf(
    SYSTEM_VERSION == "V1.3.0",
    reason="тест предназначен для проверки версии V1.2.0"
)
def test_system_version_valid():
   ...
@pytest.mark.skipIf(
    SYSTEM_VERSION == "V1.2.0",
    reason="тест предназначен для проверки версии V1.3.0"

)
def test_system_version_invalid():
    ...