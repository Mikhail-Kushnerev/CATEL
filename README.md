# CATEL

## Описание

<details>
  <summary>
    <h2 id="structure">Структура проекта</h2>
  </summary>

```python
CATEL:.
|   .gitignore
|   constant.py
|   LICENSE
|   README.md
|   test.py
|   tree.txt
|           
+---handler
|   |   view.py
|   |   __init__.py
|           
+---server
|   |   connect.py
|   |   __init__.py
|           
+---service
|   |   exceptions.py
|   |   utils.py
|   |   __init__.py
|           
+---src
|   |   main.py
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

- В главной директории добавлен файл (см. <a href="#structure">дерево проекта</a>) для тестирования личных запрос.  
Запросы также можно тестировать в **Postman**, указав **Headers** ключ.

</details>
