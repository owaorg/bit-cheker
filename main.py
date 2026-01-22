from rich.console import Console
from rich.align import Align
import os
import asyncio

con = Console()
path = os.path.join(os.path.dirname(__file__), 'proxy-list.txt')

def main():
    con.print(Align.center(
        """Инструкция:

        1. Загрузите ваши прокси в файл proxy-list.txt
        2. Запустите Инструмент

        Формат:
        
        Прокси:Порт
        Прокси:Порт
        Прокси:Порт 
        """
        ))

    with open(path,'r',encoding='utf-8') as file:
        proxyes = file.read().splitlines()

        if not proxyes:
            con.print("Файл пустой, загрузите ваши прокси в файл")
        else:
            from logic import anc_checker
            asyncio.run(anc_checker())
            