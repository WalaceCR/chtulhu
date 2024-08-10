'''
Atualmente, o valor padrão é True, mas na versão 1.5 será alterado para 'auto'. Isso significa que, se você não especificar o parâmetro dual ao chamar a função LinearSVC, ele usará o valor padrão.

Se você quiser suprimir esse aviso, pode explicitamente definir o valor de dual ao chamar a função LinearSVC. Por exemplo:

model = LinearSVC(dual=True)
Copiar código
ou

model = LinearSVC(dual=False)

Por favor, note que a escolha entre True e False para o parâmetro 
dual pode ter impacto no desempenho do algoritmo, dependendo do número de 
amostras e de características. De acordo com a documentação do sklearn, dual=False 
é preferível quando n_samples > n_features (o número de amostras é maior que o número 
de características).
'''

from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
#laranja ?
# #faz miau ?
#pata longa?

gato1 = [0, 1, 1]
gato2 = [1, 1, 0]
gato3 = [0, 1, 0]

cachorro1 = [0, 0, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 0, 0]

print(gato1)
print(cachorro1)

dados = [gato1, gato2, gato3, cachorro1, cachorro2, cachorro3]
#1 para gato, 1 para cachorro
classes = [1, 1, 1, 0, 0, 0]

print(dados)
print(classes)

modelo = LinearSVC(dual=False)
modelo.fit(dados, classes)#Robo aprende

animal_misterioso1 = [0, 0, 1]#Vou dar um animal misterioso, acho que ele errou

#Saida array([1]) = É um gato

animal_misterioso1 = [0, 0, 1]
animal_misterioso2 = [1, 0, 1]
animal_misterioso3 = [0, 1, 0]

testes = [animal_misterioso1, animal_misterioso2, animal_misterioso3]
modelo.predict([animal_misterioso1, animal_misterioso2, animal_misterioso3])#Comparar vários

previsoes = modelo.predict(testes)
testes_classes = [0, 0, 1] #Testes

comparacao = previsoes == testes_classes

#array([ True,  True,  True]) = #Saida 100% de acerto

taxa_de_acerto = accuracy_score(testes_classes, previsoes)
print("Taxa de acerto", taxa_de_acerto * 100)

#Sair 100


