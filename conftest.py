import pytest
import requests

from configuration import SERVICE_URL
from src.generators.player import Player


@pytest.fixture
def get_player_generator():
    return Player()

@pytest.fixture
def get_users():
    response = requests.get(SERVICE_URL)
    return response
