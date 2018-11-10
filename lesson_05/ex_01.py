# Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала для каждого предприятия. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.
# Примечание: 4 квартала - это 4 разных прибыли ;-)

from collections import namedtuple

Company = namedtuple('Company', 'name all_profit')

quantity = int(input("Введите количество предприятий"))

company_list = []
for i in range(quantity):
    company_list.append(Company(input("Название предприятия"), (
                                int(input("Прибыль 1 квартала")) +
                                int(input("Прибыль 2 квартала")) +
                                int(input("Прибыль 3 квартала")) +
                                int(input("Прибыль 4 квартала")))))
all_companies_profit = 0
for i in range(quantity):
    all_companies_profit += company_list[i].all_profit

middle_profit = all_companies_profit / quantity

print("Прибыль выше среднего")
for i in range(quantity):
    if company_list[i].all_profit > middle_profit:
        print(company_list[i].name)

print("*" * 50)
print("Прибыль ниже среднего")
for i in range(quantity):
    if company_list[i].all_profit <= middle_profit:
        print(company_list[i].name)
