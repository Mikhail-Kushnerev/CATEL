# CATEL

Сервис морфологического разбора

## Описание

Сервис предоставляет возможность: 
- склонять по падежам первое слово всех частей речи (глаголы только в настоящем времени);
- выдавать нормальную последнего слова.  
см. <a href="#table">результат работы</a>

## Содержание

- [Технологии](#технологии)
- <a href="#structure">Структура проекта</a>
- [Запуск](#запуск)
- <a href="#table">Результат работы</a>
- [Авторы](#авторы)

## Технологии

- Python
- Socket
- Pymorphy2

<details>
  <summary>
    <h2 id="structure">Структура проекта</h2>
  </summary>

```python
CATEL:.
|   .gitignore
|   constant.py  <-- Значения по умолчанию
|   LICENSE
|   README.md
|   try_me.py  <-- Тестирование собственных запросов
|           
+---handler
|   |   view.py  <-- Обработчик запроса
|   |   __init__.py
|           
+---server
|   |   connect.py  <-- Запуск сервера
|   |   __init__.py
|           
+---service
|   |   exceptions.py  <-- Кастомные исключения
|   |   utils.py  <-- Проверка запроса
|   |   __init__.py
|           
+---src
|   |   main.py  <-- Точка входа
|   |   __init__.py
|       
+---tests
|   |   test_ziax.py
|   |   __init__.py

```
</details>

## Запуск

- Установите и активируйте виртуальное окружение
```python
python -m venv venv
(win) source venv/Scripts/activate
(linux) source venv/bin/activate
```

- Установите зависимости

```python
pip install -r requirements.txt
```

- Из директории **src/** (см. <a href="#structure">дерево проекта</a>) запустите `main.py` файл

- В главной директории добавлен файл (см. <a href="#structure">дерево проекта</a>) для тестирования личных запрос.  
Запросы также можно тестировать в **Postman**, указав **Headers** ключ.

[содержание](#содержание)



<table
  id="table"
  align="center"
>
  <thaed>
    <tr>
      <th colspan="2">
        Результат работы
      </th>
    </tr>
  </thaed>
  <tbody>
    <tr>
      <td align="center">
        <code>try_me.py</code>
      </td>
      <td align="center">
        <h5>Postman</h5>
      </td>
    </tr>
      <td>
        <code >
          requests: {
              "sentence": "любой текст который сюда напишем"
          }
        </code>
        <br><br>
        <img
          src="https://raw.githubusercontent.com/Mikhail-Kushnerev/image/main/CATEL/try_me.png"
        >
      </td>
      <td>
        <code>
          requests: {
              "sentence": "багю по дому от устали в пижаме"
          }
        </code>
        <br><br>
        <img
          align="center"
          src="https://raw.githubusercontent.com/Mikhail-Kushnerev/image/main/CATEL/postman.png"
        >
      </td>
    <tr>
    </tr>
  </tbody>
</table>

[содержание](#содержание)
____
## Авторы

- Автор: [САТЕЛ](https://satel.org/)
- Разработчик: [Mikhail Kushnerev](https://github.com/Mikhail-Kushnerev)