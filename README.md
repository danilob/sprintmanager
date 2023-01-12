# Sprint Manager

Este projeto usa como base o docker para execução mais rápida e tem uma base de dados criada no ato da criação do container.

---

# Como instalar?

Para executar o projeto de preferência utilize docker.

- Copie o exemplo de configuração de .env:

```
cp backend/contrib/env-sample .env
```

- Gere sua SECRET_KEY e coloque no .env:

```
python3 backend/contrib/generate_secret_key.py
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

Uma base de dados inicial será criada ao iniciar o projeto, com um usuário admin e senha admin. Caso prefira desconsiderar essa criação comente as seguintes linhas no arquivo `entrypoint.sh`:

```
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
python manage.py loaddata dataset/all.json
```

- Para criar um super usuário use o seguinte comando:

```
(sudo) chmod +x run
./run manage createsuperuser
```

- Caso use o windows nativo para executar o docker utilize (com o comando docker ps você irá descobrir o ID do container que deve ser substituido no código):

```
docker exec -it <container_id> python manage.py createsuperuser
```

- Para parar realizar migrações e comandos diretamente no container, você deverá acessá-lo,
  e realizar os comandos. O primeiro comando irá listar todos os containers ativos, localize o `container_id``
  para realizar a execução do comando.

```
docker ps
docker exec -it <container_id> python manage.py <action>
```
