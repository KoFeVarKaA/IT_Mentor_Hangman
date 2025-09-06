from app.data.man import draws


class Render():
    def render_game(variables):
        print(f'''
                {draws[variables["indx_man"]]}
                {variables["word_mask"]}
                Использованные буквы: {variables["used_letters"].upper()}
                Ошибок:{variables["indx_man"]}
                Введите букву:''', end=' '
            )