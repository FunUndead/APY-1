from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees



def main():
    y = int(input("Введите число: "))
    print(datetime.now())
    x = calculate_salary(y)
    z = get_employees(x)
    print(z)


if __name__ == '__main__':
    main()
