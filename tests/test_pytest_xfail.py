import pytest

#используем для пометки тестов, которые должны падать из-за известных багов. Reason является обязательным параметром, иначе тест будет помечен как упавший, а не как ожидаемо упавший. То есть это ожидаемое падение. Тест будет запускаться, в отличие от skip.

@pytest.mark.xfail(reason="найден баг в приложении, из-за которого тест падает с ошибкой")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="баг уже исправлн, но на тест всё еще висит маркировка xfail")
def test_without_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="внешний сервис временно недоступен")
def test_external_services_is_unavailable():
    assert 1 == 2