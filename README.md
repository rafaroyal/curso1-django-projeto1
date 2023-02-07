# curso1-django-projeto1

# ANOTAÇÕES
...

## CRIAR NOVO PROJETO PYTHON
python -m venv venv

## INICIAR AMBIENTE VIRTUAL WINDOWS
.\venv\Scripts\activate

## INTALAÇÕES NECESSÁRIAS
### DJANGO: pip install django
### UPDATES: pip install pip --upgrade
### UPDATES: pip install pip setuptools wheel --upgrade
### TESTES: ...


## PARA CRIAR NOVO PROJETO DJANGO
django-admin startproject {coloca o nome do projeto qualquer} .

## PARA INICIAR UM SERVDOR LOCAL
python manage.py runserver

## PARA CRIAR UMA APLICAÇÃO (OU NOVA URL)
python manage.py starapp {colocar o nome do app qualquer}

## PARA CRIAR TABELAS NO BANCO DE DADOS SQL LITE
python manage.py migrate

## PARA PROPAGAR ALTERAÇÕES FEITAS NO MODELS.PY
python manage.py makemigrations

## PARA CRIAR UM USUÁRIO ADMIN DO DJANGO
python manage.py createsuperuser

## PARA CRIAR NAMESPACE DE ARQUIVO STATIC
python manage.py collectstatic


  # COMANDOS VISUAL STUDIO CODE
  ...
  
  ## ABRIR O INTERPRETADOR
  CTRL + SHIFT + P
  
  
  # COMANDOS GIT
  git config --global user.name "nome do usuário"
  git config --global user.email "seu email"
  
  git config --global init.defaultBranch main
  
  git init
  
  criar chave ssh: ssh-keygen
  
  git add *
  
  git commit -m "mensagem"
  
  git push
  
  
  
  
