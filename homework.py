import datetime as dt
from typing import List, Optional, Tuple, Union, Dict


class Record:

    date_format = '%d.%m.%Y'
    def __init__(self, amount: int, comment: str, date:Optional[str]= None) -> None:
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today() 
        else:
            self.date = dt.datetime.strptime(date, self.date_format).date()


class Calculator:

    def __init__(self, limit:int)-> None:
        self.limit = limit
        self.records:List = []  
 
    def add_record(self, record:int)-> None:
        self.records.append(record)

    def get_today_stats(self) -> int:
        today_stats = 0 
        for record in self.records: 
            if record.date == dt.date.today(): 
                today_stats += record.amount 
        return today_stats

    def get_week_stats(self)->int:
        period = dt.timedelta(days=7)
        today = dt.date.today()
        last_week = today - period
        week_stats = 0
        for record in self.records:
            if dt.date.today() >= record.date > last_week: 
                week_stats += record.amount
        return week_stats

    def get_today_remainder(self)-> float:
        return self.limit - self.get_today_stats()

class CashCalculator(Calculator):

    USD_RATE:float = 60.00
    EURO_RATE:float = 70.00
    RUB_RATE: float = 1.00

    def get_today_cash_remained(self, currency):
        rates = {
            'rub': ('руб', self.RUB_RATE),
            'usd': ('USD', self.USD_RATE),
            'eur': ('Euro', self.EURO_RATE)
        }
        cash = 0
        cash = self.get_today_remainder() / rates[currency][1]
        cash = round(cash, 2)
        if cash > 0:
            return (
                'На сегодня осталось '
                f'{abs(cash)} '
                f'{rates[currency][0]}'
            )
        elif cash < 0:
            return (
                'Денег нет, держись: твой долг - '
                f'{abs(cash)} '
                f'{rates[currency][0]}'
            )
        elif cash == 0:
            return 'Денег нет, держись'
        else:
            return 'Выберите другую валюту'
            


class CaloriesCalculator(Calculator):


    def get_calories_remained(self):
        calorie = self. get_today_remainder()
        if calorie > 0 and calorie < self.limit:
            return (
                'Сегодня можно съесть что-нибудь ещё,' 
                f'но с общей калорийностью не более {calorie} кКал') 
        else:
            return 'Хватит есть!' 