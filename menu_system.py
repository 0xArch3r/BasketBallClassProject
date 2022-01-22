from time import sleep
import os

class menu:
    def __init__(self,name):
        self._options = []
        self._name = name

    def add_to_menu(self, option):
        self._options.append(option)

    def header(self):
        x = os.system('clear||cls')
        print("""
        ╭━━━╮╱╱╱╭╮╭╮╱╱╱╱╱╱╱╱╭━━━━╮╱╱╱╱╭╮╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╭╮╱╱╱╭╮╱╭━━━╮
        ┃╭━╮┃╱╱╭╯╰┫┃╱╱╱╱╱╱╱╱┃╭╮╭╮┃╱╱╱╱┃┃╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱┃┃╱╱╭╯╰╮┃╭━╮┃
        ┃╰━╯┣╮╱┣╮╭┫╰━┳━━┳━╮╱╰╯┃┃┣┻━┳━━┫╰━┳━╯┣━━┳━━┳━┳━━┳━━╮┃┃╱┃┣━╮┣╮╭╯╰╯╭╯┃
        ┃╭━━┫┃╱┃┃┃┃╭╮┃╭╮┃╭╮╮╱╱┃┃┃┃━┫╭━┫╭╮┃╭╮┃┃━┫╭╮┃╭┫┃━┫┃━┫┃┃╱┃┃╭╮╋┫┃╱╭━╯╭╯
        ┃┃╱╱┃╰━╯┃╰┫┃┃┃╰╯┃┃┃┃╱╱┃┃┃┃━┫╰━┫┃┃┃╰╯┃┃━┫╰╯┃┃┃┃━┫┃━┫┃╰━╯┃┃┃┃┃╰╮┃┃╰━╮
        ╰╯╱╱╰━╮╭┻━┻╯╰┻━━┻╯╰╯╱╱╰╯╰━━┻━━┻╯╰┻━━┻━━┻━╮┣╯╰━━┻━━╯╰━━━┻╯╰┻┻━╯╰━━━╯
        ╱╱╱╱╭━╯┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
        ╱╱╱╱╰━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯""", "\n")
        print(f'Menu: {self._name}\n')
        print(f'     Your options are:')

    def display_menu(self):
        self.header()
        for index, opt in enumerate(self._options):
            print(f'          {index + 1}) {opt}')
