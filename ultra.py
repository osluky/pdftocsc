import os #BIBLIOTECA PARA OPEAÇÕES NO SISTEMA OPERACIONAL EM PYTHIN
import tabula #Biblioteca de converção de PDF em CSV
import csv

# O método init é um método especial para classes. O init é um método construtor, ele inicializa o estado de um objeto.
# O método init é invocado a cada nova instância de uma classe é criada. Na verdade não estamos apenas definindo o método init mais sobrescrevendo o
# init da classe base. O método init na classe Complex é definido assim:
class ultra():
    def __init__(self,arqdir,arqout): #Inicializando class
        a = f"{arqdir}.pdf"
        b = f"{arqout}.csv"
        pasta = f"{os.path.dirname(os.path.realpath(__file__))}/{a}"
        out = f"{os.path.dirname(os.path.realpath(__file__))}/{b}"
        self.__arq = pasta #Diretorio do arquivo PDF a ser convertido
        self.__out = out #Diretorio de saida do documento tratado
        self.__vetor = [] #Variável onde será armazenado as informações dos dados a serem tratados ou já tratados do programa.

    def convert(self): #Converte a planilha PDF em CSV e gera o arquivo output.csv
        try:
            print("Convertendo PDF em CSV")
            tabula.convert_into(self.__arq, "output1.csv", output_format="csv", pages='all', encoding='UTF-8')  # Converte arquivo PDF em CSV
        except IOError:
            print("Não foi possível abrir o arquivo: \n Arquivo não existe ")
        else:
            print("Converção Realizada com sucesso")

    def tratamento(self): # Trata o arquivo output.csv e coloca em uma lista
        try:
            print("Realizando Tratamento de Arquivo: OP-01/04.")
            arq = open('output1.csv', 'r', encoding='utf-8')
            arquivo = []  # Criando Lista Auxiliar
            for coluna in arq:
                sib = [] #Lista auxiliar para tratamento dos contatos linha por linha
                sib = coluna.split(";") #sib[ID,ST,CEP]
                ID = int(sib[0].replace(",","").replace(";","").replace('"',"").strip())
                NOME = sib[1].replace(",", "").replace(";", "").replace('"', "").strip()
                END = sib[2].replace(",", "").replace(";", "").replace('"', "").strip().upper()
                ST = sib[3].replace(",", "").replace(";", "").replace('"', "").strip().upper()
                CEP = sib[4].replace(",", "").replace(";", "").replace('"', "").strip()
                arquivo.append([ID,NOME,END,ST,CEP])
        except IOError:
            print("Não foi possível realizar o tratamento do arquivo. Contate o Desenvolvedor: OP-01/03.")
        else:
            arq.close()
            self.__vetor = arquivo
            print("Tratamento Realizado com sucesso")

    def tratamentoDados(self): #Tratamenot de informações necessarias
        try:
            print("Realizando Tratamento de Arquivo: OP-02/04.")
            for i in range(len(self.__vetor)):
                if self.__vetor[i][2].find('AVENIDA')==False:
                    self.__vetor[i][2]=self.__vetor[i][2].replace('AVENIDA','AV.')
                elif self.__vetor[i][2].find('JARDIM')==False:
                    self.__vetor[i][2]=self.__vetor[i][2].replace('JARDIM','JDS.')
                elif self.__vetor[i][2].find('ALAMEDA')==False:
                    self.__vetor[i][2]=self.__vetor[i][2].replace('ALAMEDA','AL.')
                elif self.__vetor[i][2].find('RESIDENCIAL')==False:
                    self.__vetor[i][2]=self.__vetor[i][2].replace('RESIDENCIAL','RES.')
                elif self.__vetor[i][2].find('RUA')==False:
                    self.__vetor[i][2]=self.__vetor[i][2].replace('RUA','RUA.')
                elif self.__vetor[i][2].find('APARTAMENO')==False:
                    self.__vetor[i][2]=self.__vetor[i][2].replace('APARTAMENTO','APT.')
                elif self.__vetor[i][2].find('CASA')==False:
                    self.__vetor[i][2]=self.__vetor[i][2].replace('CASA','CS.')
                elif self.__vetor[i][2].find('SALA')==False:
                    self.__vetor[i][2]=self.__vetor[i][2].replace('SALA','SL.')
                elif self.__vetor[i][2].find('JARDIM')==False:
                    self.__vetor[i][2]=self.__vetor[i][2].replace('JARDIM','JDS.')
                elif self.__vetor[i][2].find('EDFICIO')==False:
                    self.__vetor[i][2]=self.__vetor[i][2].replace('EDFICIO','ED.')
                elif self.__vetor[i][2].find('BLOCO')==False:
                    self.__vetor[i][2]=self.__vetor[i][2].replace('BLOCO','BL.')
                elif self.__vetor[i][2].find('QUADRA')==False:
                    self.__vetor[i][2]=self.__vetor[i][2].replace('QUADRA','QD.')
                elif self.__vetor[i][2].find('CACHOEIRA')==False:
                    self.__vetor[i][2]=self.__vetor[i][2].replace('CACHOEIRA','CACHO.')
                elif self.__vetor[i][2].find('LOTE')==False:
                    self.__vetor[i][2]=self.__vetor[i][2].replace('LOTE','LT.')
        except:
            pass
        else:
            print("Tratamento Realizada com sucesso")

    def posTratamento(self):
        try:
            #Deletar Output
            print("Realizando Tratamento de Arquivo: OP-03/04.")
            dire = f"{os.path.dirname(os.path.realpath(__file__))}/output1.csv"
            #os.remove(dire)
        except IOError:
            print(f"Não foi possível realizar o tratamento do arquivo \n Contate o Desenvolvedor: OP-03/03.")
        else:
            print("Tratamento Realizado com sucesso")

    def final(self,b):
        try:
            print("Realizando Tratamento de Arquivo: OP-04/04.")
            print("Gravando arquivo")
            arq = open(self.__out, 'w', newline="")  # Criando novo arquivo Ultra
            planilha = csv.writer(arq) #Criando planilha CSV no arquico Ultra
            planilha.writerow(['ID','NOME','END','BAIRRO','CEP'])
            for i in range(len(self.__vetor)):
                planilha.writerow(self.__vetor[i])
        except IOError:
            print(f"Não foi possível gravar o arquivo \n Contate o Desenvolvedor.")
        else:
            print("Gravação Realizado com sucesso")


a = ultra('clientesUltra',"ClientesTUltra")
a.convert()
a.tratamento()
a.tratamentoDados()
a.posTratamento()
a.final()