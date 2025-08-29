# Время потраченное на проект 1ч
import random
from words import words_dict
from man import draws

def new_game():
    print("Начать новую игру?  д/н")
    answ = input()

    if answ.lower() == "д":
        word = words_dict[random.randint(1, 1001)]
        word_mask = " " + "_ " * len(word)
        used_ch = ''
        flag = True
        i_word, i_man = 0, 0
        lw = len(word)
        while flag == True:
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
                print('''ERROR input:
                        Oh no, bro, u can't do so.
                        You can only write one previously unused letter.''')
            elif i_man == 6:
                flag = False
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


        if flag == True:
            print(f"Congratulations!")
            new_game()
        else:
            print(f"Oops. Looks like you lost. Загаданное слово было {word}")
            new_game()
        

    elif answ.lower() == "н":
        return
    
    else:
        print("Error: The answer can only be 'д' or 'н'")
        new_game()

new_game()