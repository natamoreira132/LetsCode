class Investidores():
    # método construtor
    def __init__(self,k,no_class,data):
        
        self.k=k
        self.no_class=no_class
        self.data=data
    
    def distancia(self,n):
        """ 
        método que faz o calculo de todas as carteiras. A cada no_class[i][2]
        vai ser feito o calculo por todos os data[i][2], logo após uma lista 
        será criada irá armazenar esses calculos, irá enumerar cada calculo e 
        ordenar a lista de forma crescente
        """
        calculo=0
        lista_calculo=[]
        y=self.no_class[n][2]
        for i in range(len(self.data)):
            lista=[]
            lista_calculo.append(lista)
            x=self.data[i][2]
            calculo=(sum([(a - b)**2 for a, b in zip(y, x)]))**(0.5)
            lista.append(calculo)
        lista2=[]
        for indice,distancia in enumerate(lista_calculo):
            posiçao=distancia,indice
            lista2.append(posiçao)
            lista2.sort()
        return lista2
    
    def vizinhos(self,k,lista2):
        """
        método que utiliza a lista ordenada criada pelo método anterior,
        utilizando o valor de  k informado o método retira os numero de k
        vizinhos mais proximos da lista, separa em uma lista somente o indice 
        busca na lista data pelo indice os investidores, pega somente o perfil
        desses investidores e coloca em uma lista e com um if/elif conta os 
        perfis e uma variavel atribui o mais frequente
        """
        lista=[]
        for i in range(self.k):
            posiçao=lista2[i][1]
            lista.append(posiçao)
        perfil=[]
        for p in lista:
            perfil_i=self.data[p][1]
            perfil.append(perfil_i)
        a = perfil.count('Conservador')
        b = perfil.count('Moderado')
        c = perfil.count('Agressivo')
        if a > b and a > c:
            perfil_d=('Conservador')
        elif b > a and b > c:
            perfil_d=('Moderado')
        elif c > a and c > b:
            perfil_d=('Agressivo')
        return perfil_d

    def dicionario(self):
        """
        método que utiliza todos os métodos criados e cria um dicionário. Com um
        for em no_class o método percorre e classifica cpf por cpf em no_class com 
        o perfil de acordo com o valor de k informado e os adiciona a um dicionário
        """
        investidores_definidos={}
        for n in range(len(self.no_class)):
            resultado=self.distancia(n)
            investidores_definidos[self.no_class[n][0]]=self.vizinhos(self.k,resultado)
        return investidores_definidos