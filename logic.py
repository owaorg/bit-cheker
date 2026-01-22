from rich.table import Table
import aiohttp, asyncio
from rich.console import Console
from rich.live import Live
import os

path = os.path.join(os.path.dirname(__file__), "proxy-list.txt")
path2 = os.path.join(os.path.dirname(__file__), "work-proxy.txt")

async def anc_checker():
    with open(path,'r', encoding='utf-8') as file:
        a=file.read().splitlines()

    table=Table(title='checker proxy')
    table.add_column("Статус")
    table.add_column("http код")
    table.add_column("Запись")

    with Live(refresh_per_second=1) as live:

        async with aiohttp.ClientSession() as session:
            for i in a:
                try:
                    correct_proxy = f'http://{i}'
                    async with session.get("https://google.com", proxy=correct_proxy, timeout=1) as response:

                        if response.status == 200:

                            with open(path2, 'a', encoding='utf-8') as file:
                                b = file.write(i + "\n")

                                table.add_row("Работает", str(response.status), "Записан")
                                live.update(table)

                except Exception as error:

                    table.add_row("Не работает", str(error), "Не записал")
                    live.update(table)
            
