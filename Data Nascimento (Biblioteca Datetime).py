import datetime

nascimento = input('Entre com a data (dd/mm/aaaa): ')
nasc_list = nascimento.split('/')
nasc_data = datetime.date(
    int(nasc_list[2]),
    int(nasc_list[1]),
    int(nasc_list[0])
)

print(nasc_data)
print(type(nasc_data))