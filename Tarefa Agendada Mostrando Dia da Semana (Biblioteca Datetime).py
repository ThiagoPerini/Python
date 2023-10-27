import datetime

def dia_da_semana(valor):
    dia = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo']
    return dia[valor]

hoje = datetime.datetime.now()
amanha = hoje + datetime.timedelta(days=1)
meia_noite = datetime.time()
tarefa = datetime.datetime.combine(amanha, meia_noite)
print(tarefa)
print(type(tarefa))
print(repr(tarefa))
print(dia_da_semana(tarefa.weekday()))
