# Page Object Model — UI тесты (Selenium + Pytest)

Учебный проект по автоматизации тестирования сайта [saucedemo.com](https://www.saucedemo.com/)  
В проекте используется **Page Object Model (POM)** для удобства поддержки тестов.

---

## 📂 Структура проекта

page_object_model/
├── conftest.py # фикстуры pytest (настройка браузера)
├── pages/ # Page Object классы
│ └── login_page.py
├── tests/ # тесты
│ └── test_login.py
├── requirements.txt # список зависимостей
└── README.md # документация проекта


---

## 🚀 Запуск тестов

1. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   
2. Запустить тесты:
   ```bash
    pytest -v --tb=short

3. Для запуска конкретного теста:
   ```bash
    pytest tests/test_login.py::test_login_success -v
