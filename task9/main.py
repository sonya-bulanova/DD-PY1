salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 1000  # количество денег, чтобы прожить 10 месяцев

for i in range(months - 1):
    spend += spend*0.03
    need_money += spend - salary
    # print(spend)
# TODO Оформить решение

print(round(need_money))
