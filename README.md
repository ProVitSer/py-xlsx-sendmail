Скрипт позволяет сделать выгрузку из MySQL и отправлять полученные данные на почту в виде .xlsx вложения
### Требование

```shell
Python 2.7
pip
sendmail
```

### Установка

```shell
pip install mysql-connector-python smtplibaio openpyxl
```

###Если хотите использовать свой SMTP, а не локальный, расскоментируйте следующие строки и введите ваши данные
```python
    #server = smtplib.SMTP("SMTP IP", 25)
    #server.ehlo()
    #server.starttls()
    #server.esmtp_features['auth'] = 'LOGIN PLAIN'
    #server.login("username", "password")
```	

### Добавим в crontab для запуска
```shell
38 17 * * * /usr/bin/python2.7 /usr/src/report.py
```
