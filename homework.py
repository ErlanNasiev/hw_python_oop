import datetime as dt
from typing import Dict, List, Optional, Tuple


class Record:
    DATE_FORMAT = '%d.%m.%Y'

    def __init__(self, amount: int, comment: str,
                 date: Optional[str] = None) -> None:
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, self.DATE_FORMAT).date()


class Calculator:

    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.records: List[Tuple[int, str, Optional[str]]] = []

    def add_record(self, record: float) -> float:
        self.records.append(record)

    def get_today_stats(self) -> float:
        date_today = dt.date.today()
        return sum(record.amount for record in self.records if record.date
                   == date_today)

    def get_week_stats(self) -> float:
        period = dt.timedelta(days=7)
        today = dt.date.today()
        last_week = today - period
        week_stats = 0
        for record in self.records:
            if today >= record.date > last_week:
                week_stats += record.amount
        return week_stats

    def get_today_remainder(self) -> float:
        return self.limit - self.get_today_stats()


class CashCalculator(Calculator):

    USD_RATE: float = 60.00
    EURO_RATE: float = 70.00
    RUB_RATE: float = 1.00

    def get_today_cash_remained(self, currency) -> float:
        rat: Dict[str, Tuple[int, str]] = {
            'rub': ('руб', self.RUB_RATE),
            'usd': ('USD', self.USD_RATE),
            'eur': ('Euro', self.EURO_RATE)
        }
        cash = self.get_today_remainder() / rat[currency][1]
        cash = round(cash, 2)
        result = (rat[currency][0])
        if cash == 0:
            return 'Денег нет, держись'
        if cash > 0:
            return (
                'На сегодня осталось '
                f'{cash} '
                f'{result}')
        if cash < 0:
            debt = abs(cash)
            return (
                'Денег нет, держись: твой долг - '
                f'{debt} '
                f'{result}'
            )


class CaloriesCalculator(Calculator):

    def get_calories_remained(self) -> float:
        today_remained = self.get_today_remainder()

        if today_remained > 0:
            return (
                'Сегодня можно съесть что-нибудь ещё, '
                f'но с общей калорийностью не более {today_remained} кКал')
        return 'Хватит есть!'
