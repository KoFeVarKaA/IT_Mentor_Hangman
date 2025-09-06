# Победа/ поражение/ перезапуск
class EndRestart():
    def endrestart_game(is_win, word):
        if is_win:
            print(f"Congratulations!")
        else:
            print(f"Oops. Looks like you lost. Загаданное слово было '{word}'")