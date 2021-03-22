import datetime as dt


class Record:


    def __init__(self, amount: int, comment: str, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.now().date()
        else:

            self.date = dt.datetime.strptime(date, "%d.%m.%Y").date()
   
class Calculator:


    def __init__(self, limit):
        self.limit = limit
        self.records = []
    def add_record(self, record):
        self.records.append(record)
    def get_today_stats(self):
        today_stats = 0
        for record in self.records:
            if record.date == dt.date.today():
                today_stats += record.amount
        return today_stats
    def get_week_stats(self):
        week_stats = 0
        self.week = dt.timedelta(days=7)
        self.last_week = dt.date.today() - self.week
        for record in self.records:
            if dt.date.today() >= record.date > self.last_week:
                week_stats += record.amount
        return week_stats

class CashCalculator(Calculator):


    USD_RATE = 60.00
    EURO_RATE = 70.00
    RUB_RATE = 1.00
 
    
    def get_today_cash_remained(self, currency):
        if currency == 'rub':
            today_cash = self.limit - self.get_today_stats()
            if today_cash > 0:
                return f'На сегодня осталось {abs(today_cash)} руб'
            elif today_cash == 0:
                return "Денег нет, держись"
            
            else:

                return f"Денег нет, держись: твой долг - {abs(today_cash)} руб"
        elif currency == 'usd':
            today_cash = round(
                (self.limit - self.get_today_stats()) / self.USD_RATE, 2)
           
            if today_cash > 0:
                return f'На сегодня осталось {abs(today_cash)} USD'
           
            elif today_cash == 0:
                return "Денег нет, держись"
           
            else:
                return f"Денег нет, держись: твой долг - {abs(today_cash)} USD"
 
        elif currency == 'eur':  
            today_cash = round((self.limit - self.get_today_stats())
             / self.EURO_RATE, 2)
            
            if today_cash > 0:
                return f"На сегодня осталось {abs(today_cash)} Euro"
           
            elif today_cash == 0:
                return "Денег нет, держись"
           
            else:
                return f"Денег нет, держись: твой долг - {abs(today_cash)} Euro"
      
 
 
class CaloriesCalculator(Calculator):

    
    def get_calories_remained(self):
        calorie_store = self.limit - self.get_today_stats()
        if calorie_store > 0:
            return f"Сегодня можно съесть что-нибудь ещё," \
                   f" но с общей калорийностью не более {calorie_store} кКал"
        else:
            return "Хватит есть!"



#для Cashcalculator

r1 = Record(amount =145, comment='Безудержный шопинг', date='08.03.2019' )
r2 = Record(amount =1568, comment='Наполнение потребительской корзины', 
date='09.03.2019' )
r3 = Record(amount =691, comment='Катание на такси', date='08.03.2019' )


#Для CaloriesCalculator

r4 = Record(amount =1186, comment='Кусок тортика. И еще один', 
date='08.02.2019' )
r5 = Record(amount =84, comment='Йогурт', date='09.02.2019' )
r6 = Record(amount =1140, comment='Баночка чипсов', date='08.02.2019' ) 


cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment='кофе'))
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
cash_calculator.add_record(Record(amount=3000,
                                  comment='бар в Танин др',
                                  date='08.11.2019'))
 
print(cash_calculator.get_today_cash_remained('rub'))
