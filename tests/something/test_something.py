import pytest

from src.generators.player import PlayerLocalization


@pytest.mark.parametrize("status", [
    "ACTIVE",
    "INACTIVE",
    "BANNED",
    "DELETED"
])
def test_check_status(status, get_player_generator):
    print(get_player_generator.set_status(status).build())

@pytest.mark.parametrize("balance", [
    "100",
    "0",
    "-100",
    "abc"
])
def test_check_balance(balance, get_player_generator):
    print(get_player_generator.set_balance(balance).build())

@pytest.mark.parametrize("delete_key", [
    "account_status",
    "balance",
    "localize",
    "avatar"
])
def test_delete_key(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)

def test_update_localize(get_player_generator):

    object_to_send = get_player_generator.update_inner_generator(
        "localize", PlayerLocalization('fr_FR').set_number(15)
        ).build()
    print(object_to_send)