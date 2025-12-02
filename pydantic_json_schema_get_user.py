from clients.users.public_users_client import get_public_users_client
from clients.users.private_users_client import get_private_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from clients.private_http_builder import AuthenticationUserSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

def script_user() -> None:
    public_client_init = get_public_users_client()

    request = CreateUserRequestSchema(
        email = fake.email(),
        password="12345",
        first_name="Po",
        last_name="Example",
        middle_name="Python"
    )

    created_user = public_client_init.create_user(request)
    user_id = created_user.user.id
    print(user_id)


    auth_user = AuthenticationUserSchema(
        email=request.email,
        password=request.password
    )
    private_client_init = get_private_users_client(auth_user)

    response = private_client_init.get_user_api(user_id)
    data = response.json()
    print("Ответ get_user_api:", data)

    schema = GetUserResponseSchema.model_json_schema()

    validate_json_schema(instance=data, schema=schema)
    print("Валидация прошла успешно")


if __name__ == "__main__":
    script_user()

