# crud_postgreSQL

para que o CRUD funcione você precisa primeiro instalar o postegreSQL ( https://www.postgresql.org/download/ ).


após a instalação do postgre você precisará acessar o psql via usuário postgre ( será criado automáticamente a instalação do postgreSQL ),


acesse o terminal e use o comando:  psql (ferramenta de banco do postgre ) -U (usuario -> ) postgres -d template1 (banco)


o cursor estiver : template1=# . significa que o comando acima foi reconhecido, em seguida de o comando : CREATE DATABASE "nome do banco sem as "" ";


feito isso basta se atentar aos comentários do proprio código e alterar o mesmo para o seu caso. 
