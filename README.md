# MVP_BackEnd
 ```
 O objetivo é a entrega do MVP que tem como escopo a implementação de um backEnd, com 4x rotas de API e uma tabela de roupas para cadastro, busca, deleção e edição.
 ```
 
```
  Para executar o container do Docker do Back-end:
  - Abra o terminal na pasta do do projeto, e use os comandos.
  - docker build -t backend
  - docker run -p 5000:8000 backend
```

```
Para executar os comandos estamos utilizando um ambiente virtual env.
```
 
 (env)$ pip install -r requirements.txt
```
Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
