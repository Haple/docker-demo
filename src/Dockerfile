# Esse arquivo é a receita
# para criar uma imagem da 
# nossa aplicação.

# Aqui dizemos que vamos
# construir nossa imagem
# nos baseando em outra já
# pronta. Essa que vamos nos
# basear é um Linux minimalista
# com a versão 3.7 do Python
# instalada nele.
FROM python:alpine3.7

# O comando copy recebe como
# parâmetros o caminho do que
# deve ser copiado, e o caminho 
# do destino. Nesse caso, estamos
# copiando todo o nosso código para
# a pasta /app dentro do contêiner
COPY . /app

# Aqui dizemos que a pasta /app
# é onde vamos trabalhar agora
WORKDIR /app

# Aqui estamos executando o comando
# para instalar as dependências da 
# nossa aplicação dentro do nosso 
# contêiner
RUN pip install -r requirements.txt

# Será através da porta 5000
# que vamos conseguir se comunicar
# com a aplicação dentro do
# contêiner. É a mesma porta que 
# deixamos nossa aplicação 'ouvindo'
# quando escrevemos o código
EXPOSE 5000

# Diz ao contêiner qual o comando
# principal para executar a aplicação
CMD python ./index.py
