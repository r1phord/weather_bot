import re

import requests
from bs4 import BeautifulSoup


def get_30_days_weather():
    response = requests.get('https://yandex.ru/pogoda/yaroslavl/month')
    return response.content


def parse(date):
    weather = get_30_days_weather()
    soup = BeautifulSoup(weather, features='html.parser')
    cell = soup.find('h6', text=re.compile(date.lower()))
    if not cell:
        return 'Проверьте правильность введённой даты. \n Прогноз доступен только на ближайшие 30 дней. Пример ' \
               'правильного ввода: 1 января '
    cell = cell.parent

    data = []
    for tag in cell:
        if tag.name == 'table':
            for tr in tag.findAll('td', attrs={'class': 'climate-calendar-day__detailed-data-table-cell '
                                                        'climate-calendar-day__detailed-data-table-cell_value_yes'}):
                data.append(tr.text)
        else:
            data.append(tag.text)

    data[3] = 'Давление ' + data[3]
    data[4] = 'Влажность ' + data[4]
    data[5] = 'Ветер ' + data[5]
    return '\n'.join(data[:-1])


date = '2 Август'
print(parse(date))