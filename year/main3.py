def is_leap_year():
    year = int(input("Введите год: "))
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f"Год {year} - високосный")
    else:
        print("Это год не високосный")
        