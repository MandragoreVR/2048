from textual_2048 import *
from io import StringIO
import sys

#Méthode de test 1 (en mettant le contenu de l'input à l'aide de monkeypatch)
def test_read_player_command(monkeypatch):
    monkeypatch.setattr(sys, 'stdin', StringIO('g'))
    assert read_player_command() == 'g'


#Méthode de test 2 (en remplaçant la fonction input utilisée par notre fonction read_player_command par une fonction mock)
def mock_return_function(_):
    return 'g'
def test_read_player_command_2(monkeypatch):
    monkeypatch.setattr('builtins.input', mock_return_function)
    assert read_player_command() == 'g'
