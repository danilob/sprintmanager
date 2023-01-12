# Sprint Manager
## SISTEMA DE GESTÃO DE PARTICIPAÇÃO REMOTA EM AÇÕES EXTENSIONISTAS
IMPORTANTE: Estamos usando Python 3.9.7, Django 3.2.8 e PostgreSQL neste projeto

# Como instalar?

Antes, verifique se você tem esses pacotes instalados (os pacotes abaixo são do Ubuntu):

```
sudo apt-get install build-essential python3-dev python3-venv python3-pip
```

Crie um virtualenv com python 3.9:

- linux
```
virtualenv -p python3 venv
```

- windows
```
python -m venv venv
```

Ative o virtualenv:

- linux
```
source venv/bin/activate
```

- windows
```
venv\bin\activate
```

Instale as dependencias com o comando abaixo:

```
pip install -r requirements.txt
```

Copie o exemplo de configuração de .env:

```
cp contrib/env-sample .env
```

Gere sua SECRET_KEY:

```
python contrib/generate_secret_key.py
```

Adicione a sua SECRET_KEY gerada com o comando acima no arquivo .env na variavel correspondente:

[Link](https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e) para ajudar na criação do banco de dados postgresql

Execute as migrações do projeto:

```
python manage.py migrate
```

Inicie o projeto:

```
python manage.py runserver
```

# Como usar o sistema?

Crie um superuser:

```
python manage.py createsuperuser
```

Com o sistema rodando (`python manage.py runserver`) acesse `http://127.0.0.1:8000/admin` informe seu usuário e senha criados anteriormente no login para conseguir acessar o admin do django.

### Usando Docker


- Copie o exemplo de configuração de .env:

```
cp contrib/env-sample .env
```

- Gere sua SECRET_KEY e coloque no .env:

```
python3 contrib/generate_secret_key.py
```

- Para subir a aplicação execute o comando

```
docker-compose up --build
```
ou

```
sudo docker-compose up --build
```

- Para parar a aplicação execute o comando

```
docker-compose down
```

- Para criar um super usuário use o seguinte comando: 

```
(sudo) chmod +x run
./run manage createsuperuser
```

- Caso use o windows nativo para executar o docker utilize (com o comando docker ps você irá descobrir o ID do container que deve ser substituido no código):
````
docker exec -it <container_id> python manage.py createsuperuser
```


- Para parar realizar migrações e comandos diretamente no container, você deverá acessá-lo,
e realizar os comandos. O primeiro comando irá listar todos os containers ativos, localize o `container_id``
para realizar a execução do comando.

```
docker ps
docker exec -it <container_id> python manage.py <action>
```