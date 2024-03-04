class Carro:

    #Construtor inicial da classe
    def __init__(self, marca, modelo, cor, ano, valor, marcha):
       self.marca = marca
       self.modelo = modelo
       self.cor = cor
       self.ano = ano
       self.valor = valor
       self.marcha = marcha

    #Métodos da Classe
    def ligar(self):
        print("Carro ligado")

    def desligar(self):
        print("Carro desligado")

    def acelerar(self):
        print("Acelerando")

    def freiar(self):
        print("Freiando")

    def trocar_marcha(self, nova_marcha):
        print("Acionando atuador")

        def _trocar_marcha():
            if nova_marcha > self.marcha:
                print("Marcha trocada")
                self.marcha = nova_marcha


    #Método de acesso as informações das instâncias da classe
    def __str__(self):
        return f"{self.__class__.__name__}:{[f'{chave}={valor}'for chave, valor in self.__dict__.items()]}"

#Instanciando a Classe
carro_01= Carro("VW","TCross","Branco", 2022, 105, 1)
carr0_02= Carro("Jeep","Compass","Prata", 2016, 106, 1)

carro_01.ligar()
carro_01.acelerar()
carro_01.trocar_marcha(2)
carro_01.acelerar()
carro_01.trocar_marcha(3)
carro_01.trocar_marcha(2)
carro_01.freiar()
carro_01.desligar()
print(carr0_02)