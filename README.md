# 🏠 Домашнє завдання №3 — Flask + Docker + JSON

## 📌 Опис проєкту

У цьому проєкті реалізовано простий вебзастосунок на базі Flask, який дозволяє:
- надсилати повідомлення через HTML-форму;
- зберігати їх у JSON-файлі;
- переглядати всі повідомлення на окремій сторінці.

Застосунок обгорнуто у Docker-контейнер із використанням volumes для збереження даних поза межами контейнера.

---

## 🛠 Використані технології

- Python 3.11
- Flask
- Docker
- Docker Compose
- HTML, CSS (Bootstrap)
- JSON

---

## ▶️ Інструкція з запуску

1. Клонуйте репозиторій:

- git clone https://github.com/твій-логін/goit-pythonweb-hw-03
- cd goit-pythonweb-hw-03

2. Зберіть та запустіть контейнер:
- docker-compose down -v
- docker-compose up --build

3. Відкрийте браузер:
👉 Перейдіть за адресою: http://localhost:3000
✉️ Надішліть повідомлення → перегляньте його на сторінці /read.

---

### 🗂 Структура проєкту

- app.py — логіка Flask-додатку
- templates/ — HTML-шаблони з підтримкою Jinja2
- static/ — стилі та логотип
- storage/data.json — збережені повідомлення
- Dockerfile — конфігурація образу
- docker-compose.yml — запуск з volume
- requirements.txt — залежності Python
- README.md 

---

### 📝 Примітка
Дані зберігаються у storage/data.json і не губляться при перезапуску контейнера, завдяки підключеному volume.

---

### 👤 Автор
Олександр Ребенок

GitHub: https://github.com/999Ralex999


