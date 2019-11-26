# Docker demo

Nessa demo vamos criar um servidor simples em python, 
construir uma imagem para a aplicação e criar um contêiner
baseado nessa imagem.

# Passos

```
docker build --tag docker-demo .

docker run --name docker-demo1 -p 5000:5000 docker-demo
```
