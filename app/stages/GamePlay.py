
from app.errors import Errors
from app.render import Render

# Основная логика игры
class Play():
    def play_game(word: str) -> bool:
        # Задаем основные переменные
        word_mask = " " + "_ " * len(word)
        used_letters = ''
        indx_word, indx_man = 0, 0 # Индексы для количества угаданных букв и стадий рисунка
        len_word = len(word)

        while True:
            # Все слово угадано?
            if indx_word == len_word:
                return True
            
            variables = {
                "word_mask": word_mask,
                "used_letters": used_letters,
                "indx_word": indx_word, 
                "indx_man": indx_man,
            }
            Render.render_game(variables)
            ch = input().lower()

            # Если символ уже использовался или некорректный ввод
            if ch in used_letters or 0 >= len(ch) > 1:
                Errors.incorrect_input()
            # Если человечек польностью нарисован
            elif indx_man == 6:
                return False
            # Если буква угадана
            elif ch in word:
                indx_word += word.count(ch)
                for i in range(len(word)):
                    # Замена _ на букву
                    if ch == word[i]:
                        word_mask = list(word_mask)
                        word_mask[i*2+1] = ch
                        word_mask = ''.join(word_mask)
            # Если буква не угадана
            else:
                indx_man += 1

            # Добавляем символ в список использованных букв
            if ch not in used_letters:
                used_letters = used_letters + ch + ', '