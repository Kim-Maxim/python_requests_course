from src.baseclasses.response import Response
from src.schemas.user import User
from src.schemas.computer import Computer
from examples import computer


def test_getting_users_list(get_users):
    # print(response.__getstate__()) #Вывести всю информацию из запроса
    Response(get_users).assert_status_code(200).validate(User)


def test_pydantic_object():
    comp = Computer.model_validate(computer)
    # print(comp.detailed_info.physical.photo.host) #Получаем любой объект из json с помощью pydantic
    print(comp.model_json_schema())  # Получаем свалидированный объект через json_schema
