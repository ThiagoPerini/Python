import datetime

hoje = datetime.datetime.now()
regra = datetime.timedelta(days=3)
data_boleto = hoje + regra
print(hoje)
print(regra)
print(data_boleto)
