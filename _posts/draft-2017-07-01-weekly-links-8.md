---
title: "Weekly links. Выпуск 8"
date: 2017-07-01
tags:
 - links
category:
 - weekly-links
---

В этом выпуске: Clojure, Python


### Что такое Tail Call и Tail Call Optimization. И как с этим обстоят дела в Clojure и Python

Как же это легко и заманчиво, прочитать "Because recur does not consume stack space (thereby avoiding stack overflow errors), recur is critical when implementing certain recursive algorithms." и сказать, что все понятно и очевидно (это из книги Clojure Programming).
Или, что дальше разберусь.

Но нет, надо поймать себя на этом моменте и понять, что на самом деле не так уж понятно и очевидно.
И что надо бы разобраться с этим прямо сейчас.

Для начала, терминология:

* [What Is Tail Call Optimization?](https://stackoverflow.com/questions/310974/what-is-tail-call-optimization)
* [What methods are there to avoid a stack overflow in a recursive algorithm?](https://softwareengineering.stackexchange.com/questions/194646/what-methods-are-there-to-avoid-a-stack-overflow-in-a-recursive-algorithm)

Clojure recur, tail call, tail call optimization:

* [Clojure - using recur vs plain recursive function call](https://stackoverflow.com/a/34097339) - и надо опять себя не обмануть и почитать и документацию и вопросы на которые стоят ссылки :)
  * [Why can't tail calls be optimized in JVM-based Lisps?](https://stackoverflow.com/questions/19462314/why-cant-tail-calls-be-optimized-in-jvm-based-lisps)
  * [Why no tail call optimization (Clojure)](https://groups.google.com/forum/#!msg/clojure/4bSdsbperNE/tXdcmbiv4g0J)
* [Why is tail recursion optimisation not implemented in languages like Python, Ruby, and Clojure? Is it just difficult or impossible?](https://www.quora.com/Why-is-tail-recursion-optimisation-not-implemented-in-languages-like-Python-Ruby-and-Clojure-Is-it-just-difficult-or-impossible)

Clojure TCO:

* [Clojure Tail Call Optimizer (CTCO)](https://github.com/cjfrisz/clojure-tco) - это на будущее попробовать разобраться
* [TCO - Chris Frisz](https://www.youtube.com/watch?v=RLqqGSthmC0&list=PLZdCLR02grLoyWsKpovatiBYJyf-RKx0c&index=20)

Python:

* [Does Python optimize tail recursion?](https://stackoverflow.com/questions/13591970/does-python-optimize-tail-recursion)
* [Tail Call Optimization for Python (модуль)](https://github.com/baruchel/tco). [Блог автора модуля](http://baruchel.github.io/)
* [Tail call recursion in Python](http://www.kylem.net/programming/tailcall.html)


В итоге, через 3-4 часа понимаешь, что вроде и стало понятней, но по дороге родились еще 20 вопросов :)


### Clojure

* [The Ultimate Guide To Clojure REPLs](https://lambdaisland.com/guides/clojure-repls)
* [The Roots of Lisp](http://languagelog.ldc.upenn.edu/myl/ldc/llog/jmc.pdf)


* [Clojure Hangouts](https://www.youtube.com/user/niquolaj/videos)
* [Web Development with Clojure, Second Edition](https://pragprog.com/book/dswdcloj2/web-development-with-clojure-second-edition)



### General

* [The Trap You Set For Yourself](https://blog.codinghorror.com/the-trap-you-set-for-yourself/)
* [Being Honest with Yourself is Hard](https://www.scotthyoung.com/blog/2015/06/04/self-honesty/)
* [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)



* [Slack Slash Commands as a Service](https://sscaas.eu/)
* [slack-overflow](https://github.com/karan/slack-overflow)
* [programmingexcuses.com](http://www.programmerexcuses.com/)
