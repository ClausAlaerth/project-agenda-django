# Projeto Agenda

Um aplicativo web simples, com o intuito de observar meu progresso utilizando o framework Django. A aplicação é capaz de armazenar contatos com seus respectivos dados, vinculando-os a uma conta, que por ventura pode ser criada no próprio domínio. Em desenvolvimento, a aplicação utilizou SQLite3 para armazenamento dos dados de teste, migrando para o PostgreSQL em produção. O arquivo "settings.py" foi adaptado para importar um arquivo chamado "local_settings.py", para mudanças como a troca do banco de dados padrão, SQLite3, para o PostgreSQL em produção, crie este último arquivo apenas se quiser, sua ausência não afetará o aplicativo, que funcionará com os padrões do framework.

Para utilizar o aplicativo em desenvolvimento, lembre-se de instalar as dependências presentes em "requirements.txt" e executar os seguintes comandos, para que o Django sirva sua aplicação localmente:

```
python(sua-versao) manage.py makemigrations
python(sua-versao) manage.py migrate
python(sua-versao) manage.py runserver
```

