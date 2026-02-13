import pytest

#scope= function - по умолчанию, на каждый тест
#scope= class - выполняется один раз на каждый класс. Н-р если в классе два теста, то выполнится class только на одном из тестов, а не на каждом. И для второго теста уже не будет выполняться, так как фикстура уже отработала для этого класса
#scope= module - на каждый модуль(файл)
#scope= session - на всю сессию тестирования, то есть один раз при запуске всех тестов
#scope= package - на весь пакет(пакет это папка где есть init файл)
#autouse= True - фикстура будет выполняться автоматически для всех тестов, без необходимости явно указывать ее в параметрах тестов. Если autouse= False, то фикстура будет выполняться только для тех тестов, которые явно указаны в ее параметрах. Можно комбинировать со scope


@pytest.fixture(autouse=True)
def send_analytics():
    print("[AUTOUSE] Отправляем данные в сервис аналитики")

@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Инициализируем настройки автотестов")

@pytest.fixture(scope="class")
def user():
    print("[CLASS] Создаеем данные пользователя один раз на тестовый класс")

@pytest.fixture
def users_client(settings): #можно инициализировать фикстуру в фикстуре, тогда она будет выполняться до нее. В данном случае, при выполнении users_client, сначала выполнится settings, так как она указана в параметрах. Передается закэшированная, которая уже была выполнена, так как scope= session
    print("[Function] Создаем API клиент на каждый автотест")

class TestUserFlow:
    def test_user_can_login(self, settings, user, users_client):
        ...

    def test_user_create_course(self, settings, user, users_client):
        ...


class TestAccountFlow:
    def test_user_account(self, settings, user, users_client):
        ...

@pytest.fixture
def user_data() -> dict:
    print("Создаем пользователя для теста(setup)") #выполнили код до теста
    yield  {
        "username": "test_user",
        "email": "test@example.com"
    }  #выполнили код во время теста
    print("Удаляем пользователя после теста(teardonw)") #выполнили код после теста

def test_user_email(user_data: dict):
    print(user_data)
    assert user_data['email'] == 'test@example.com'

def test_user_username(user_data: dict):
    print(user_data)
    assert user_data['username'] == 'test_user'