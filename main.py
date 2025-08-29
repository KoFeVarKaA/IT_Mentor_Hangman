# Время потраченное на проект 1ч
import random
from data.words import words
from data.man import draws
from errors import Errors

def new_game():
    print("Начать новую игру?  д/н")
    answ = input()

    if answ.lower() == "д":
        word = words[random.randint(1, len(words))]
        word_mask = " " + "_ " * len(word)
        used_ch = ''
        is_win = True
        i_word, i_man = 0, 0
        lw = len(word)
        while is_win:
            if i_word == lw:
                break
            print(f'''
                {draws[i_man]}
                
                {word_mask}
                
                Использованные буквы: {used_ch.upper()}
                Ошибок:{i_man}
                Введите букву:''', end=' '
            )
            ch = input().lower()
            if ch in used_ch or len(ch) > 1:
                Errors.incorrect_input()
            elif i_man == 6:
                is_win = False
            elif ch in word:
                i_word += word.count(ch)
                for i in range(len(word)):
                    if ch == word[i]:
                        word_mask = list(word_mask)
                        word_mask[i*2+1] = ch
                        word_mask = ''.join(word_mask)
                word.replace(ch, "")
            else:
                i_man += 1
            if ch not in used_ch:
                used_ch = used_ch + ch + ', '


        if is_win == True:
            print(f"Congratulations!")
            new_game()
        else:
            print(f"Oops. Looks like you lost. Загаданное слово было {word}")
            new_game()
        

    elif answ.lower() == "н":
        return
    
    else:
        Errors.wrong_answer()
        new_game()

new_game()