from collections import defaultdict, OrderedDict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    today = datetime.today().date()
    if today.weekday() == 0:  #якщо сьогодні понеділок, поточний день зміщуємо назад на 2 дні, і функція виведе імена тих, у кого був день народження на попередніх вихідних, а не на наступних.
        today -= timedelta(days=2)
    else: #якщо сьогодні не понеділок, функція виведе імена тих, у кого день народження на наступних вихідних, у наступний понеділок
        for user in users:
            name = user["name"]
            birthday = user["birthday"].date()
            birthday_this_year = birthday.replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year+1)
            delta_days = (birthday_this_year - today).days
            if delta_days < 7:
                birthday_weekday = birthday_this_year.strftime('%A')
                if birthday_weekday in ["Saturday", "Sunday"]:
                    birthday_weekday = "Monday"
                birthdays_per_week[birthday_weekday].append(name)
      
    sorted_birthdays_per_week = OrderedDict(sorted(birthdays_per_week.items()))
    for day, names in sorted_birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")
