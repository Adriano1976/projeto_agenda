# Projeto Agenda

 Nesse projeto foi usado o Framework Django no Pycharm. Com isso, foram criadas alguns models, urls e views seguindo as aulas online do Prof. Luiz Otávio Miranda em seu curso de Pytnon na Udemy. Depois foi feito deploy no heroku.
 
 ## Fazendo Deploy no Heroku 
 
* ATENÇÃO: Tudo o que estiver entre [], seve ser trocado pelo nome do seu projeto e aplicação.						

### 1ª PARTE - Estrutura Django utilizada na aplicação.
	pip install django
	django-admin.py startproject [my-project] 
	django-admin.py startapp [my-app]
	python manage.py makemigrations [my-app]
	python manage.py migrate
	python manage.py createsuperuser
	ATTENTION: if you're getting ready to put it on heroku, don't change this line.
		STATIC_URL = '/static/'

### 2ª PARTE - Criar my-project no Heroku.

### 3ª PARTE - Instalar heroki-cli:
	heroku --version


### 4ª PARTE - Fazer login e associar o projeto local com o remoto:
	git init
	git status
	heroku git:remote -a [my-app]

### 5ª PARTE - Preparando as dependências para instalar no Heroku:
	pip freeze
	pip freeze > requirements.txt

### 6ª PARTE - Instalando o Gunicorn para servir a aplicação no Heroku e django-on-heroku:
	pip install gunicorn
	pip freeze > requirements.txt
	
### 7ª PARTE - Determinando a versão do python executada no Heroku:	
	https://devcenter.heroku.com/articles/python-support "python-3.10.3"
	Criar na raiz do my-project: runtime.txt > python-3.10.3

### 8ª PARTE - Configurando o arquivo Procfile + Dica extra:
	Criar na raiz do my-project: Procfile > web: gunicorn [my-app].wsgi --log-file -	

### 9ª PARTE - Fazendo o Deploy:
	Criar na raiz do my-project: .gitignore > .idea/ e db.sqlite3 / .env
	pip install django-on-heroku
	pip freeze > requirements.txt
	settings.py: import django_on_heroku
	settings.py: django_on_heroku.settings(locals())
	* git status
	* git add .
	* git commit -am "Carga inicial"
	* git push heroku master
	Obs1: Para repositórios existentes: heroku git:remote -a [my-app]
	Obs2: Se a aplicação não funcionar: heroku logs e revise as etapas anteriores.

### 10ª PARTE - Executando o migrate e criar um superuser:
	heroku run python manage.py migrate
	heroku run python manage.py createsuperuser

### 11ª PARTE - Desacoplando variáveis específicas de ambiente com o python-decouple.
	pip install python-decouple
	pip freeze > requirements.txt
	Criar na raiz do my-project: .env > DEBUG = True
	Criar na raiz do my-project: .env > SECRET_KEY = 'django-insecure-cyq_tc=x=da245@tbi6pw5n8y4y@=#^4z0*kb2tq4yqkt2(247'
	Criar na raiz do my-project: .env.example > DEBUG = False
	Criar na raiz do my-project: .env.example > SECRET_KEY = 'senha do projeto no settings.py'
	settings: from decouple import config
	settings: DEBUG = config('DEBUG', cast=bool, default=False)
	Adicionando variável no Heroku: DEBUG = False
	Adicionando variável no Heroku: SECRET_KEY = 'django-insecure-cyq_tc=x=da245@tbi6pw5n8y4y@=#^4z0*kb2tq4yqkt2(247'
	git add .
	git commit -am "Python Decouple"
	git push heroku master

### 12ª PARTE - Conectando no banco postgres externamente se tiver usando ele.
	No site Heroku: Overview -> Heroku Postgres -> settings -> view credentials
	No pgAdmin local: General -> Create-Server
	Nome: Heroku
	Host: ec2-54-173-77-184.compute-1.amazonaws.com
	Port: 5432
	Database: db8i8fafbmfr1s
	User: gedxgfdkvqiyon
	Password: b8cbd694469a40128d91f0fee93831e2b5cd148d7a8a85b9f184e6712425aa5b
	pgAdmin -> Heroku -> Properties -> Advanced -> DB restriction -> db8i8fafbmfr1s



