#Na agricultura tem-se o uso de 3 nutrientes básicos, Nitrogênio, Fósforo e Potássio.
#Esse pequeno script calcula a relação entre 3 doses de nutrientes informados gerando
#Após calcular a relação entre ele é calculada a dose que atende as necessidades informadas.

#Primeira parte, solicitação do Usuário
nutri = "N","P","K"
quantidades = list()
quantidadesordem = []
menor = 0
formulado = list()
possivel = 0
for c, i in enumerate(nutri):
    quantidades.append(int(input(f'Digite a necessidade de {i} em kg/ha: ')))
#segunda parte, organização das entradas.
quantidadesordem = sorted(quantidades)
if quantidadesordem[0] == 0:
  menor = quantidadesordem[1]
else:
  menor = quantidadesordem[0]
for c, i in enumerate(quantidades):
    formulado.append(quantidades[c]/menor)
#Após a entradas estarem organizadas e a menor quantidade selecionada passamos
#aos cáculos
teste = range(1,30)
possivel= []
mult = []
temp = 0
combina = []
todos = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
for cc in teste:
    if (formulado[0]*cc)%1 == 0:
        if (formulado[1]*cc)%1 ==0:
            if (formulado[2]*cc)%1 ==0:
                possivel.append(cc)
if len(possivel) == 0:
    print('Não é possível um formulado com essas concentrações')
else:
    for c in possivel:
        for i in formulado:
            temp += c*i
        if 30<= temp <= 60:
            mult.append(c)
        temp = 0
    for i, c in enumerate(mult):
        for da in formulado:
            combina.append((c*da))
        todos[i] = combina[:]
        combina.clear()
    print(f'As opções de formuldados NPK são:\n')
    for q in todos:
        if len(q) > 1:
           print(f'{q}, a dose é {quantidades[1]*(q[1]/100):.0f} kg/ha \n')

