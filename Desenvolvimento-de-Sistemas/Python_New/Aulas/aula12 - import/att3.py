import calendar
from datetime import datetime

ano_atual = datetime.now().year
dia_atual = datetime.now().day
mes_atual = datetime.now().month
hora_atual = datetime.now().hour

print(f'Você está no ano de {ano_atual}\nmês: {mes_atual} \ndia: {dia_atual}\nhora: {hora_atual}')
print(calendar.calendar(ano_atual))