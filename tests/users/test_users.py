from src.baseclasses.response import Response
from src.schemas.user import User
from src.generators.player import Player


def test_getting_users_list(get_users):
    # print(response.__getstate__()) #Вывести всю информацию из запроса
    Response(get_users).assert_status_code(200).validate(User)
