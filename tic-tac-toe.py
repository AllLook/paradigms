from kivy.app import App  # для создания приложения

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button  # класс кнопка
from kivy.config import Config
#Задаем конфиг окна
Config.set("graphics", "resizable", "0")# 0 означает что размер не изменяется
Config.set("graphics", "width", "300")  # высота и ширина окна
Config.set("graphics", "height", "300")


class MainApp(App):
    def __init__(self):
        self.switch = True# переключатель положения игры
        super().__init__()  # наследование функционала класса App

    def build(self):  # переназначенная функция из самого App
        self.title = "Крестики-нолики"  # название окна

        root = BoxLayout(orientation="vertical", padding=5)  # вертикальный бокс с  отступами 5

        grid = GridLayout(cols=3)  # c 3 колонками

        self.buttons = []

        for _ in range(9):
            button = Button(
                color=[0, 0, 0, 1],
                font_size=24,  # отрисовка кнопки
                disabled=False,
                on_press=self.tic_tac_toe
            )
            self.buttons.append(button)  # добавление кнопки в список
            grid.add_widget(button)  # добавление кнопки виджета в колонки

        root.add_widget(grid)#добавляем виджеты в бокс

        root.add_widget(
            Button(
                text="Restart",
                size_hint=[1, .1],
                on_press=self.restart
            )
        )# создание кнопки для сброса

        return root #возврат кнопок в программу

    def restart(self, arg):
        self.switch = True  # возврат к началу игры

        for button in self.buttons:
            button.color = [0, 0, 0, 1]
            button.text = ""  # стираем все из кнопок
            button.disabled = False  # снова можно сделать рестарт

    def tic_tac_toe(self, arg):
        arg.disabled = True  # сброс кнопки для повторного нажатия
        arg.text = 'X' if self.switch else 'O'  # в кнопку поместить текст если не Х то 0
        self.switch = not self.switch  # переключение кнопки для новых ходов
        coordinate = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # по оси X
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # по оси Y
            (0, 4, 8), (2, 4, 6),  # по диагонали D
        )  # возможные комбинации

        vector = lambda item: [self.buttons[x].text for x in item]

        win = False
        color = [0, 1, 0, 1]  # Зеленый
        for item in coordinate:
            if vector(item).count('X') == 3 or vector(item).count('O') == 3:
                win = True
                for i in item:
                    self.buttons[i].color = color#подсвечиваем зеленым символ который выиграл
                    break

            if win:#если есть выигрыш
                for button in self.buttons:
                    button.disabled = True #блокируем игру(кнопки)


if __name__ == "__main__":
    MainApp().run() #запускаем приложение
