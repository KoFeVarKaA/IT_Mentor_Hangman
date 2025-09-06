from app.errors import Errors


class Start():
    def start_game() -> bool:
        while True:
            print("Начать новую игру? д/н")
            answer = input().lower()
            
            if answer == "д":
                return True
            elif answer == "н":
                return False
            else:
                Errors.wrong_answer()