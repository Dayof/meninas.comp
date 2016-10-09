Webapp do meninas.comp
=============

Web application do meninas.comp.

### Instalação
```
$ cd meninas.comp
$ . env/bin/activate
$ export MENINASCOMP_SETTINGS=config.py
$ pip install --editable .
$ export FLASK_APP=meninascomp
$ flask initdb
```

### Executar
```
$ flask run
```
A aplicação estará ativa no endereço http://localhost:5000/ .

### Environment

Iniciar
```
$ . env/bin/activate
```

Sair
```
$ deactivate
```

### Testes
```
$ cd meninas.comp
$ . env/bin/activate
$ python setup.py test
```

### Autoria
- @Dayof
	- Dayanne Fernandes da Cunha
	- dayannefernandesc@gmail.com
