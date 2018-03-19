# adjust-deeplink

Генератор adjust ссылок для Wheely

## Установка и запуск

Установка без virtualenv, хотя лучше с ним

```sh
$ sudo apt-get install nginx supervisor python-pip python
$ sudo pip install -r requirements.txt 
$ sudo cp conf/nginx.conf /etc/nginx/servers/deeplink.conf
$ sudo cp conf/supervisor.conf /etc/nginx/supervisor/conf.d/deeplink.conf
$ sudo service nginx reload
```

Перезапуск supervisor

```sh
$ sudo supervisorctl
supervisorctl> reread
supervisorctl> update
supervisorctl> status
```

