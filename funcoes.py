import re


def convert (valor):
    valor = valor
    valor1 = valor.replace('R$','')
    valor = valor1.replace('.','')
    valor = int(valor)
    return valor


def faixametragem(area_util):
    area_util = area_util
    if area_util <= 50:
        faixa = "A:1-50m²"
        return faixa
    elif (area_util <= 100) and (area_util >50):
        faixa = "B:51-100m²"
        return faixa
    elif (area_util <= 200)  and (area_util >100):
        faixa = "C:101-200m²"
        return faixa
    elif area_util > 200:
        faixa = "D:+200m²"
        return faixa
    
# pega só os numeros
def pegar_num(p):
	num = int(re.search(r'\d+', p).group())	
	return num

def transforma(area_util):
    area_util = area_util.replace(",",".")
    area_util = float(area_util)
    return (area_util)

def transforma2(area_util):
    area_util = int(area_util)
    return (area_util)

# revomeve acentos e deixa tudo minusculo
import unicodedata
def acentos(result):
    new = unicodedata.normalize('NFD', result)
    return new.encode('ascii','ignore').decode('utf8').casefold()

#remove os de do enreço
def remove_de(result):
    lista = result.split(' ')
    for i in lista:
        if i == "de":
            lista.remove("de")
        if i == "do":
            lista.remove("do")
        if i == "dos":
            lista.remove("dos")
        if i == "da":
            lista.remove("da")
        if i == "das":
            lista.remove("das")
        if i == "e":
            lista.remove("e")
    new = ' '.join(lista)
    return new

def nome_rua(p):
    # divide a string, aqui por um delimitador de virgula, poderia ser qlqr outro, e pega a primeira q foi delimitado. q é o q eu quero
    #condominio_nome = p.split('-')[0]
    rua = p.split('.')[0]
    bairro = p.split('.')[1]
    bairro = bairro.split('-')[0]
	#rua = rua.split('-')[0]
    # aqui remove os numeros da string
    result = ''.join(i for i in rua if not i.isdigit())
    #remove todos os espaços do final da string
    rua = "".join(result.rstrip()) 
    rua = acentos(rua)
    rua = remove_de(rua)
    rua = rua.replace(",","")
    rua = ' '.join(rua.split())
    return rua , bairro