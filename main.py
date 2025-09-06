# Время потраченное на проект 1ч
import random

from app.data.words import words
from app.stages.GameEndRestart import EndRestart
from app.stages.GamePlay import Play
from app.stages.GameStart import Start


while True:
    # Выбираем слово
    word = words[random.randint(1, len(words))]
    if Start.start_game():
        is_win = Play.play_game(word)
        EndRestart.endrestart_game(is_win, word)
    else:
        break
        