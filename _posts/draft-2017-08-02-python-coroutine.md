---
title: "Fluent Python: coroutine"
date: 2017-08-03
tags:
 - links
 - notes
 - fluent-python
category:
 - python
---

Сопрограммы (coroutine) на основе генератора.

Вот хоть я уже и не сетевой инженер, а никуда не денешься от того, что при изучении новых тем, в голове рождаются примеры использования для сетей :)

Следующий раздел [Fluent Python](http://shop.oreilly.com/product/0636920032519.do) - сопрограммы.

> В книге Fluent Python используется Python 3.4. В версиях 3.5 и 3.6 были внесены изменения связанные с сопрограммами. В этой заметке вся информация основывается на разделе coroutines в книге Fluent Python.

## Сопрограмма

Сопрограмма - часть программы, которая взаимодействует с вызывающем ее кодом, генерируя и получая данные.

> Более полное определение в [википедии](https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0)

С точки зрения синтаксиса, сопрограмма выглядит как генератор.
Однако, в сопрограмме, yield как правило находится с правой стороны выражения: ```command = yield```.

При этом генерация значения опциональна:

* Если после yield находится выражение, генератор отдает его
* иначе, отдается значение None

Сопрограмма может не только генерировать данные, но и принимать их.
Для этого используется метод send.

### Базовый пример сопрограммы. Передача данных сопрограмме

Пример сопрограммы:
```python
In [1]: def basic_coroutine1(start):
   ...:     print('Start value:', start)
   ...:     first = yield
   ...:     print('First received:', first)
   ...:     second = yield
   ...:     print('Second received:', second)
   ...:
```

Вызываем функцию, чтобы получить генератор:
```python
In [2]: bc1 = basic_coroutine1(100)

In [3]: bc1
Out[3]: <generator object basic_coroutine1 at 0xb598abfc>
```

Теперь, чтобы получить возможность отправлять данные сопрограмме, надо ее инициировать.
Это делается вызовом next:
```python
In [4]: next(bc1)
Start value: 100
```

Сопрограмма выполнила весь код до первого yield и остановилась.
Теперь у нас есть возможность отправить данные, используя метод send:
```python
In [5]: bc1.send(200)
First received: 200
```

Сопрограмма получила данные, присвоила их в переменную first, вывела сообщение "First received: 200" и остановилась на следующем yield.

Теперь можно снова отправить данные:
```python
In [6]: bc1.send(300)
Second received: 300
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-5-62309180db70> in <module>()
----> 1 bc1.send(300)

StopIteration:
```

Тут аналогично: сопрограмма получила данные, присвоила их в переменную second, вывела сообщение "Second received: 300".
Но, так как на этом функция-генератор закончилась, возвращается исключение StopIteration.

Вернемся к загадочной строке ```next(bc1)```.
Эта инициация необходима, чтобы отпарвлять данные сопрограмме.
сли снова вызвать функцию и сразу попытаться отправить данные, возникнет исключение:
```python
In [8]: bc1 = basic_coroutine1(100)

In [9]: bc1.send(200)
------------------------------------------------------------
TypeError                  Traceback (most recent call last)
<ipython-input-9-11b40b565caa> in <module>()
----> 1 bc1.send(200)

TypeError: can't send non-None value to a just-started generator
```

По описанию исключения понятно, что инициировать сопрограмму можно и по-другому, отправив ```send(None)```:
```python
In [10]: bc1 = basic_coroutine1(100)

In [11]: bc1.send(None)
Start value: 100
```

### Базовый пример сопрограммы. Оператор return

В сопрограмме можно использовать оператор return для завершения работы генератора и возврата данных.

Например:
```python
In [50]: def basic_coroutine2():
    ...:     collection = []
    ...:     while True:
    ...:         item = yield
    ...:         if item is None:
    ...:             return collection
    ...:         collection.append(item)
    ...:
```

Инициация генератора и отправка данных выполняется аналогично:
```python
In [51]: bc2 = basic_coroutine2()

In [52]: next(bc2)

In [53]: bc2.send(100)

In [54]: bc2.send(200)
```

При отправке None, сопрограмма завершает работу.
В этом случае, по-прежнему генерируется исключение StopIteration, но, кроме этого, данные возвращаются как атрибут исключения:
```python
In [55]: bc2.send(None)
------------------------------------------------------------
StopIteration              Traceback (most recent call last)
<ipython-input-55-ef77f9d8836c> in <module>()
----> 1 bc2.send(None)

StopIteration: [100, 200]
```

Для получения данных в переменную, надо получить значение атрибута value:
```python
In [56]: bc2 = basic_coroutine2()

In [57]: next(bc2)

In [58]: bc2.send(100)

In [59]: bc2.send(200)

In [60]: bc2.send(300)

In [61]: try:
    ...:     bc2.send(None)
    ...: except StopIteration as e:
    ...:     result = e.value
    ...:

In [62]: result
Out[62]: [100, 200, 300]
```

### Базовый пример сопрограммы. Получение данных с yield

В этом примере yield не просто приостанавливает выполнение сопрограммы, а еще и возвращает данные:
```python
In [68]: def basic_coroutine3(items):
    ...:     collection = [i for i in items]
    ...:     while True:
    ...:         item = yield collection
    ...:         collection.append(item)
    ...:
```

Еще одно небольшое изменение - сопрограмма создана с параметром items.
Это значит, что ей можно передавать аргументы:
```python
In [70]: bc3 = basic_coroutine3([1,2,3])

In [71]: next(bc3)
Out[71]: [1, 2, 3]
```

После инициации сопрограммы, ей можно передавать данные.
Теперь после каждой передачи данных, возвращается содержимое списка collection:
```python
In [72]: bc3.send(100)
Out[72]: [1, 2, 3, 100]

In [73]: bc3.send(200)
Out[73]: [1, 2, 3, 100, 200]
```

Раз содержимое возвращается, его можно присвоить в переменную:
```python
In [74]: result = bc3.send(300)

In [75]: result
Out[75]: [1, 2, 3, 100, 200, 300]
```

В этой сопрограмме нет условия для завершения цикла while.
Это значит, что она будет принимать данные и возвращать результат до тех пор, пока сопрограмма используется.
Но у сопрограммы есть метод close, который позволяет в любой момент завершить ее:
```python
In [76]: bc3.close()
```

Теперь, при обращении к сопрограмме, будет возвращаться исключение StopIteration:
```python
In [77]: bc3.send(400)
------------------------------------------------------------
StopIteration              Traceback (most recent call last)
<ipython-input-77-1d704bd03fe8> in <module>()
----> 1 bc3.send(400)

StopIteration:
```

## Пример использования сопрограммы с netmiko

С помощью сопрограммы можно создать соединение SSH с устройством, которое ожидает команды.
А, после получения команды, возвращает результат.

Первый вариант сопрограммы:
```python
In [1]: def send_show_command(device_params):
   ...:     print('Opening connection to IP: {}'.format(device_params['ip']))
   ...:     conn = netmiko.ConnectHandler(**device_params)
   ...:     conn.enable()
   ...:     result = None
   ...:     while True:
   ...:         command = yield result
   ...:         result = conn.send_command(command)
   ...:
```

Для подключения по SSH с помощью netmiko, надо создать словарь с параметрами подключения:
```python
In [2]: import netmiko

In [3]: r1 = {'device_type': 'cisco_ios',
   ...:       'ip': '192.168.100.1',
   ...:       'username': 'cisco',
   ...:       'password': 'cisco',
   ...:       'secret': 'cisco' }
   ...:
```

Теперь можно вызывать сопрограмму и инициировать ее:
```python
In [5]: ssh = send_show_command(r1)

In [6]: next(ssh)
Opening connection to IP: 192.168.100.1
```

При инициации сопрограммы, выполняется весь код до yield - выводится сообщение, выполняется подключение к устройству и netmiko переходит в режим enable.
После этого, управление останавливается на yield.

Теперь, если передать сопрограмме команду, она запишет ее в переменную command, выполнит ее с помощью метода send_command и, так как цикл пошел на следующую итерацию, вернет результат выполнения команды и остановится:
```python
In [7]: ssh.send('sh ip arp')
Out[7]: 'Protocol  Address          Age (min)  Hardware Addr   Type   Interface\nInternet  19.1.1.1                -   aabb.cc00.6520  ARPA   Ethernet0/2\nInternet  192.168.100.1           -   aabb.cc00.6500  ARPA   Ethernet0/0\nInternet  192.168.100.100        37   aabb.cc80.c900  ARPA   Ethernet0/0\nInternet  192.168.200.1           -   0203.e800.6510  ARPA   Ethernet0/1\nInternet  192.168.200.100        28   0800.27ac.1b91  ARPA   Ethernet0/1\nInternet  192.168.230.1           -   aabb.cc00.6530  ARPA   Ethernet0/3'
```

Отправка еще одной команды, но только теперь результат сохраняется в переменную:
```python
In [8]: result = ssh.send('sh ip int br')

In [9]: print(result)
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
Ethernet0/2                19.1.1.1        YES NVRAM  up                    up
Ethernet0/3                192.168.230.1   YES NVRAM  up                    up
```

Если сопрограмма больше не нужна, можно остановить ее, с помощью метода close:
```python
In [10]: ssh.close()
```

Но, в данном случае, после завершения работы сопрограммы, сессия SSH остается открытой на оборудовании.
Более корректно было бы завершать сессию, когда сопрограмма завершает работу.

Это достаточно легко сделать, так как вызов метода close, генерирует внутри сопрограммы исключение GeneratorExit.
А значит, можно перехватить его и закрыть сессию.

Финальный пример сопрограммы send_show_command с закрытием сессии (файл netmiko_coroutine.py):
```python
import netmiko

def send_show_command(device_params):
    print('Open connection to: '.rjust(40, '#'),
          device_params['ip'])
    conn = netmiko.ConnectHandler(**device_params)
    conn.enable()
    result = None
    while True:
        try:
            command = yield result
            result = conn.send_command(command)
        except GeneratorExit:
            conn.disconnect()
            print('Connection closed'.rjust(40, '#'))
            break


r1 = {'device_type': 'cisco_ios',
      'ip': '192.168.100.1',
      'username': 'cisco',
      'password': 'cisco',
      'secret': 'cisco' }

commands = ['sh ip int br', 'sh ip arp']

ssh = send_show_command(r1)
next(ssh)

for c in commands:
    result = ssh.send(c)
    print(result)

ssh.close()
```

Результат выполнения:
```
 $ python netmiko_coroutine.py
####################Open connection to:  192.168.100.1
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
Ethernet0/2                19.1.1.1        YES NVRAM  up                    up
Ethernet0/3                192.168.230.1   YES NVRAM  up                    up
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  19.1.1.1                -   aabb.cc00.6520  ARPA   Ethernet0/2
Internet  192.168.100.1           -   aabb.cc00.6500  ARPA   Ethernet0/0
Internet  192.168.100.100        54   aabb.cc80.c900  ARPA   Ethernet0/0
Internet  192.168.200.1           -   0203.e800.6510  ARPA   Ethernet0/1
Internet  192.168.200.100         2   0800.27ac.1b91  ARPA   Ethernet0/1
Internet  192.168.230.1           -   aabb.cc00.6530  ARPA   Ethernet0/3
#######################Connection closed
```

## yield from
The yield from syntax enables complex generators to be refactored into smaller,
nested generators while avoiding a lot of boilerplate code previously required for a
generator to delegate to subgenerators.


## Дополнительные материалы


Документация:

* [Generator-iterator methods](https://docs.python.org/3/reference/expressions.html#generator-iterator-methods)
* [PEP 342 -- Coroutines via Enhanced Generators](https://www.python.org/dev/peps/pep-0342/)
* [PEP 380 -- Syntax for Delegating to a Subgenerator](https://www.python.org/dev/peps/pep-0380/)

Статьи:

* [Generator Tricks for Systems Programmers](http://dabeaz.com/generators/)
* [A Curious Course on Coroutines and Concurrency](http://dabeaz.com/coroutines/). [Видео](https://www.youtube.com/watch?v=Z_OAlIhXziw)

Ответ на stackoverflow:

* [What does the “yield” keyword do?](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do) и [перевод этого ответа](https://habrahabr.ru/post/132554/)


Fluent Python:

* [Fluent Python. Chapter 16 Coroutines](http://shop.oreilly.com/product/0636920032519.do)
* [Примеры из книги](https://github.com/fluentpython/example-code/tree/master/)

Презентация:

* [gevent](http://mauveweb.co.uk/presentations/gevent-talk/#1)
