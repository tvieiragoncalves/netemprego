#coding=utf-8
#Bibliotecas necessarias
import requests
import bs4
#Onde o scraper vai buscar a info -função get
input = str(raw_input("Que pesquisa queres fazer ? \n"))
canon = str('http://www.net-empregos.com/')
fonte = requests.get(canon + input)
print(canon + input)

#Transformar em soup object e escolher o html parser- neste caso usamos lxml
soup = bs4.BeautifulSoup(fonte.text, 'lxml')

#For loop para selecionar a tag que queremos (neste caso selecionamos a tag a debaixo de div)
for paragrafo2 in  soup.select('div font')[0:700]:
    print(paragrafo2.text)


#combinar múltiplas linhas de array para poder alinhar mensagem Cada unidade da tabela que aparece no site 

#Definimos a variável como string mas depois temos o problema do unicode encode ...

##for paragrafo in  soup.select('div font'): - o resto da info necessária (zona, local etc..)





# To-do - combinar mais dados (área geográfica e empresa)
#Save to - file, feed etc..
# Combinar com serviço sms / notificações sempre que surje nova entrada